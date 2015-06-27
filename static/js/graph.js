var data = [
    {mag: 20},
    {mag: 50},
    {mag: 60},
    {mag: 92},
    {mag: 70}
];

var ndx = crossfilter(data);

var totalDim = ndx.dimension(function(d){return d.mag});

var total_20 = totalDim.filter(20);

var magnitudeChart = dc.barChart("#dc-magnitude-chart");
