---
layout: page
title: Software
nav: software
---

<div class="row">
{% for p in site.data.software %}
{% include software.html %}
{% endfor %}
</div>
