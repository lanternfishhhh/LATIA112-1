let barchart = document.getElementById('barchart');

// Trace 1
let trace1 = {
    type: "bar",
    name: "北部",
    x: [],
    y: [],
    text: [],
};

for (let i = 0; i < north_college.length; i++) {
    trace1.x[i] = north_college[i]['name'];
    trace1.y[i] = north_college[i]['count'];
    trace1.text[i] = north_college[i]['count'].toString();
}

// Trace 2
let trace2 = {
    type: "bar",
    name: "中部",
    x: [],
    y: [],
    text: [],
};

for (let i = 0; i < middle_college.length; i++) {
    trace2.x[i] = middle_college[i]['name'];
    trace2.y[i] = middle_college[i]['count'];
    trace2.text[i] = middle_college[i]['count'].toString();
}

// Trace 3
let trace3 = {
    type: "bar",
    name: "南部",
    x: [],
    y: [],
    text: [],
};

for (let i = 0; i < south_college.length; i++) {
    trace3.x[i] = south_college[i]['name'];
    trace3.y[i] = south_college[i]['count'];
    trace3.text[i] = south_college[i]['count'].toString();
}

// Trace 4
let trace4 = {
    type: "bar",
    name: "東部",
    x: [],
    y: [],
    text: [],
};

for (let i = 0; i < east_college.length; i++) {
    trace4.x[i] = east_college[i]['name'];
    trace4.y[i] = east_college[i]['count'];
    trace4.text[i] = east_college[i]['count'].toString();
}

// Trace 5
let trace5 = {
    type: "bar",
    name: "金門",
    x: [],
    y: [],
    text: [],
};

for (let i = 0; i < kinmen_college.length; i++) {
    trace5.x[i] = kinmen_college[i]['name'];
    trace5.y[i] = kinmen_college[i]['count'];
    trace5.text[i] = kinmen_college[i]['count'].toString();
}

let datab = [trace1, trace2, trace3, trace4, trace5];

let layout = {
    margin: { t: 0 },
};

Plotly.newPlot(barchart, datab, layout);
