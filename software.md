---
layout: page
title: Software
nav: software
---

# Packages

<div class="row">
{% for p in site.data.software %}
{% include software.html %}
{% endfor %}
</div>

# mangal.io

[mangal.io](http://mangal.io) is a database for species interaction networks. Or
more accurately, it is a platform to store data about species interactions, and
use it for network studies. It integrates with other biodiversity databases.
