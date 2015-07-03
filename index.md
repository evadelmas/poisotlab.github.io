---
layout: page
nav: home
title: Computational ecology
---

**Why do species interact?** We study ecological interactions, their variation
through space and time, and their consequences on ecosystem properties. We use
numerical methods, computational tools, and close collaboration with empiricists
to address these questions.

<div class="graphlet d3"></div>

<script src="/resources/js/index-graph.js"></script>

## News

{% for post in site.posts limit:5%}
<b>{{ post.date | date: '%B %d, %Y' }}</b> :: <a href="{{ post.url }}">{{ post.title }}</a>
{% endfor %}
