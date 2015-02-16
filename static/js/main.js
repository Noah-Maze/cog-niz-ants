console.log("Main JS was started");

// Declare a data loading function
function updateData() {
  console.log("Update Data was called");

  // Select the target svg
  var mySvg = d3.select("#ts_svg")

  // Get data from Flask
  d3.json("/botLocJson", function(error, botData) {

    // Get dimensions of svg
    svgW = mySvg.style("width")
    svgH = mySvg.style("height")

    // Scale everything so the circles are nicely positioned
    var x = d3.scale.linear()
      .range([0, svgW])
      .domain([0,1]);
    var y = d3.scale.linear()
      .range([0,svgH])
      .domain([0,1]);

    // Finally, add circles
		var feature = mySvg.selectAll("circle")
			.data(botData);

    feature.enter().append("circle")
			.style("stroke", "black")
			.style("fill", "red")
			.style("opacity", .6);

    feature.attr("cx", function(d) {return x(d.cx);})
      .attr("cy", function(d) {return y(d.cy);})
      .attr("r", function(d) {return d.r;});
  });
};

updateData();
var dataUpdate = setInterval(function() { updateData();}, 200);
