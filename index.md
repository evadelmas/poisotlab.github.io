---
layout: page
title: Computational ecology
description: Département de Biologie, Université de Montréal
---


<div class="pure-u-2-3 copy landing" markdown="1">

**Why do species interact?** We study ecological interactions, their variation
through space and time, and their consequences on ecosystem properties. We use
numerical methods, computational tools, and close collaboration with empiricists
to address these questions.

You can read more about [our research](research), [who we are](people), or learn
about [current opportunities](opportunities). Oh, and we also [publish some papers](papers).

</div>

<div class="pure-u-1-3 graphlet d3">

</div>

<script type="text/javascript">
var links = [
  {source: "A", target: "B", type: "interaction"},
  {source: "A", target: "C", type: "interaction"},
  {source: "C", target: "D", type: "interaction"},
  {source: "D", target: "E", type: "interaction"},
  {source: "A", target: "E", type: "interaction"},
  {source: "D", target: "F", type: "interaction"},
  {source: "B", target: "G", type: "interaction"},
  {source: "B", target: "H", type: "interaction"},
  {source: "B", target: "C", type: "interaction"},
  {source: "G", target: "B", type: "interaction"},
];

var nodes = {};

// Compute the distinct nodes from the links.
links.forEach(function(link) {
  link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
  link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
});

var width = 300,
    height = 400;

var force = d3.layout.force()
    .nodes(d3.values(nodes))
    .links(links)
    .size([width, height])
    .linkDistance(60)
    .charge(-300)
    .on("tick", tick)
    .start();

var svg = d3.select(".graphlet").append("svg")
    .attr("width", width)
    .attr("height", height);

// Per-type markers, as they don't inherit styles.
svg.append("defs").selectAll("marker")
    .data(["interaction"])
  .enter().append("marker")
    .attr("id", function(d) { return d; })
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
  .append("path")
    .attr("d", "M0,-5L10,0L0,5");

var path = svg.append("g").selectAll("path")
    .data(force.links())
  .enter().append("path")
    .attr("class", function(d) { return "link " + d.type; })
    .attr("marker-end", function(d) { return "url(#" + d.type + ")"; });

var circle = svg.append("g").selectAll("circle")
    .data(force.nodes())
  .enter().append("circle")
    .attr("r", 6)
    .call(force.drag);

var text = svg.append("g").selectAll("text")
    .data(force.nodes())
  .enter().append("text")
    .attr("x", 8)
    .attr("y", ".31em")
    .text(function(d) { return ""; });

// Use elliptical arc path segments to doubly-encode directionality.
function tick() {
  path.attr("d", linkArc);
  circle.attr("transform", transform);
  text.attr("transform", transform);
}

function linkArc(d) {
  var dx = d.target.x - d.source.x,
      dy = d.target.y - d.source.y,
      dr = Math.sqrt(dx * dx + dy * dy);
  return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
}

function transform(d) {
  return "translate(" + d.x + "," + d.y + ")";
}

</script>
