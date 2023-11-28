import sys
import configparser

# Azure Text Analytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

from flask import Flask, request, abort
from linebot.v3 import(
    WebhookHandler
)
from linebot.v3.exceptions import(
    InvalidSignatureError
)
from linebot.v3.webhooks import(
    MessageEvent,
    TextMessageContent,
)
from linebot.v3.messaging import(
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)

#Config Parser
config = configparser.ConfigParser()
config.read('config.ini')

#Config Azure Analytics
credential =AzureKeyCredential(config['AzureLanguage']['API_KEY'])
app =Flask(__name__)

channel_access_token=config['Line']['CHANNEL_ACCESS_TOKEN']
channel_secret=config['Line']['CHANNEL_SECRET']

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

handler =WebhookHandler(channel_secret)

configuration = Configuration(
    access_token=channel_access_token
)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature =request.headers['X-Line-Signature']
    # get request body as text
    body =request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # parse webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return'OK'



@handler.add(MessageEvent, message=TextMessageContent)
def message_text(event):
    sentiment_result=azure_sentiment(event.message.text)
    with ApiClient(configuration) as api_client:
        line_bot_api=MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=sentiment_result)]
            )
        )

def azure_sentiment(user_input):
    text_analytics_client = TextAnalyticsClient(
        endpoint=config['AzureLanguage']['END_POINT'],
        credential=credential)

    documents = [user_input]
    response = text_analytics_client.analyze_sentiment(
        documents,
        show_opinion_mining=True,
        language="zh-Hant")

    print(response)

    docs = [doc for doc in response if not doc.is_error]
    if docs:
        doc = docs[0]
        print(f"Document text: {user_input}")
        print(f"Overall sentiment: {translate_sentiment(doc.sentiment)}")

        if hasattr(doc, 'sentences') and doc.sentences:
            for sentence in doc.sentences:
                print(f"Sentence: {sentence.text}")
                print(f"Sentiment: {translate_sentiment(sentence.sentiment)}")

                if hasattr(sentence, 'mined_opinions') and sentence.mined_opinions:
                    aspect_text = "未找到主詞"
                    for mined_opinion in sentence.mined_opinions:
                        if mined_opinion.target and hasattr(mined_opinion.target, 'text'):
                            aspect_text = mined_opinion.target.text
                            break  # 只取第一個主詞

                    print(f"Opinions: {aspect_text}")
                else:
                    print("Opinions not found in the sentence.")

        highest_scores = {
            "positive": max(doc.confidence_scores.positive for doc in docs),
            "neutral": max(doc.confidence_scores.neutral for doc in docs),
            "negative": max(doc.confidence_scores.negative for doc in docs)
        }

        print(f"Highest Scores: {highest_scores}")

        return f"主詞: {aspect_text}。情感: {translate_sentiment(doc.sentiment)}。分數: {max(highest_scores.values())}"

    return "未找到有效分析結果"


def translate_sentiment(sentiment):
    if sentiment == "positive":
        return "正向"
    elif sentiment == "neutral":
        return "中性"
    elif sentiment == "negative":
        return "負向"
    else:
        return sentiment


if __name__ =="__main__":
    app.run()