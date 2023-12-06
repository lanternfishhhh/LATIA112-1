let scatterchart = document.getElementById('scatterchart');

let trace1a = {};
trace1a.mode = "lines+markers";
trace1a.type = "scatter";
trace1a.name = "國立大學";

trace1a.x = [];
trace1a.y = [];

for (let i = 0; i < national.length; i++) {
    trace1a.x[i] = national[i]['name'];
    trace1a.y[i] = national[i]['count'];
}

let trace2a = {};
trace2a.mode = "lines+markers";
trace2a.type = "scatter";
trace2a.name = "私立大學";

trace2a.x = [];
trace2a.y = [];

for (let i = 0; i < private.length; i++) {
    trace2a.x[i] = private[i]['name'];
    trace2a.y[i] = private[i]['count'];
}

let dataa = [];
dataa.push(trace1a);
dataa.push(trace2a);

let layouta = {
    margin: {t: 0}
};

// 將散點圖繪製到容器中
Plotly.newPlot(scatterchart, dataa, layouta);
