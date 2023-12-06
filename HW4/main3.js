let piechart = document.getElementById('piechart');

let trace1c = {};
trace1c.type = "pie";
trace1c.title = "國立大學";
trace1c.hole =0.5;
trace1c.labels =[];
trace1c.values =[];
trace1c.domain ={
    row:0,
    column:0
};

for(let x=0; x<national.length; x++){
    trace1c.labels[x] =national[x]['name'];
    trace1c.values[x] =national[x]['count'];
}


let trace2c = {};
trace2c.type = "pie";
trace2c.title = "私立大學";
trace2c.hole =0.5;
trace2c.labels =[];
trace2c.values =[];
trace2c.domain ={
    row:0,
    column:1
};


for(let x=0; x<private.length; x++){
    trace2c.labels[x] =private[x]['name'];
    trace2c.values[x] =private[x]['count'];
}

let datac = [];
datac.push(trace1c);
datac.push(trace2c);

let layoutc = {
    margin:{t:10,l:0,},
    grid:{rows:2,columns:2}
};

// 將散點圖繪製到容器中
Plotly.newPlot(piechart, datac, layoutc);
