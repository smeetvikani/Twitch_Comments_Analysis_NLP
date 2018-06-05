var color = d3.scaleOrdinal(d3.schemeCategory10);
var result = [];
json_data = globalData2['outcome'];
for (var i in json_data) {
    result.push([parseInt(i), parseInt(json_data[i])]);
}
var dataset = result;
var w = 800,
    h = 300,
    pad = 50;

var svg = d3.select("#plot")
    .append("svg")
    .attr("height", h)
    .attr("width", w);

var xScale = d3.scaleLinear()
    .domain([0, d3.max(dataset, function(d) {
        return d[0];
    })])
    .range([pad, w - 0]);

var yScale = d3.scaleLinear()
    .domain([0, d3.max(dataset, function(d) {
        return d[1]+2;
    })])
    .range([h - pad, pad]);

var rScale = d3.scaleLinear()
    .domain([0, d3.max(dataset, function(d) {
        return 20;
    })])
    .range([1, 30]);

var xAxis = d3.axisBottom(xScale);
var yAxis = d3.axisLeft(yScale);
var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
        return "<strong>X,Y:</strong> <span style='color:red'>" + d[0] + ", " + d[1] + "</span>";
    });
svg.call(tip);
var circ = svg.selectAll("circle")
    .data(dataset)
    .enter()
    .append("circle")
    .attr("cx", function(d) {
        return xScale(d[0]);
    })
    .attr("cy", function(d) {
        return yScale(d[1]);
    })
    .attr("r", function(d) {
        return rScale(3);
    })
    .style('fill', function(d) {
        return color(d[1]);
    }).attr("opacity", 0.7)
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide);


svg.append("g")
    .attr("class", "axis")
    .attr("transform", "translate(0," + (h - pad) + ")")
    .call(xAxis);

svg.append("g")
    .attr("class", "axis")
    .attr("transform", "translate(" + pad + ", 0)")
    .call(yAxis);


// Add Y axis Label
svg.append("text")
    .attr("class", "y label")
    .attr("text-anchor", "end")
    .style("font-size", "15px")
    .attr("y", 3)
    .attr("x", -60)
    .attr("dy", ".75em")
    .attr("transform", "rotate(-90)")
    .text(" Unsupervised ML Topics");


                            svg.append("text")
                                .attr("class", "y label")
                                .attr("text-anchor", "end")
                                .style("font-size", "15px")
                                .attr("y", 220)
                                .attr("x",500)
                                .attr("dy", ".75em")
                                .text("Bins of 30s Inverval");

    var color_hash = {  '0' : '0 : Pawned!',
                        '8' : '8: Fail!',
                        '10' : '10: GG!Clap!',
                      }
  // add legend
  var legend = svg.append("g")
    .attr("class", "legend")
    .attr("x", w - 65)
    .attr("y", 25)
    .attr("height", 100)
    .attr("width", 100);

  var legend_colous_array=[];
  var count_legend=6;
  legend.selectAll('g').data(dataset)
      .enter()
      .append('g')
      .each(function(d, i) {


        if (jQuery.inArray(d[1] ,legend_colous_array) == -1){
            var g = d3.select(this);
          g.append("rect")
          .attr("x", w - 180)
          .attr("y", count_legend*25)
          .attr("width", 10)
          .attr("height", 10)
          .style("fill", color(d[1]));

        g.append("text")
          .attr("x", w - 160)
          .attr("y", count_legend* 25 + 8)
          .attr("height",30)
          .attr("width",100)
          .style("fill", color(d[1]))
          .text(color_hash[d[1]]);
          legend_colous_array.push(d[1]);
          count_legend = count_legend+1;
        }


      });
