---
layout: page
title: People
nav: people
---



<div class="row">

{% for p in site.data.people %}{% if p.pi %}
{% include people.html %}{% endif %}
{% endfor %}

</div>

# Current lab members

<div class="row">

{% for p in site.data.people %}{% if p.current %}
{% include people.html %}{% endif %}
{% endfor %}

<div class="col-xs-2 col-md-1">
<img src="/mugshots/cynthiagueveneuxjulien.png" class="img-circle" style="width: 70px; height: 70px"  />
</div>
<div class="col-xs-10 col-md-5" markdown="1">
**Cynthia Guéveneux-Julien** is an undergraduate research assistant, working on the spatial
dissimilarity of host-parasite interactions at the continental scale. Her
project is giving new insights on how the structure and dissimilarity of networks varies
at the margin of species distributions, and how to best identify which environmental
variables are driving this variation.
</div>

<div class="col-xs-2 col-md-1">
<img src="/mugshots/philippedesjardinsproulx.jpg" class="img-circle" style="width: 70px; height: 70px"  />
</div>
<div class="col-xs-10 col-md-5" markdown="1">
**Philippe Desjardins-Proulx** is a PhD student with Tim and [Dominique
Gravel][dom]. His research focuses on applying machine learning and deep
transfer knowledge to solve complicated ecological problems of all sorts, and
he has more informations about it on his [website](http://phdp.github.io/). He
talks about Haskell too much on [twitter](http://twitter.com/phdpqc/), and
does thing in esoteric programming languages on
[github](http://github.com/phdp/).
</div>

</div>

# Former lab members

<div class="row">

<div class="col-xs-2 col-md-1">
<img src="/mugshots/renaudmckinnon.png" class="img-circle" style="width: 70px; height: 70px"  />
</div>
<div class="col-xs-10 col-md-5" markdown="1">
**Renaud Mc Kinnon**
completed his MSc with Tim, [Dominique Gravel][dom] and [Steven
Kembel][skemb]. His research focused on interactions between trees from
experimental plantations and their microbial ectosymbionts, to understand how
different levels of biodiversity (interactions, functional traits, taxonomy)
shape ecosystem functioning.
</div>

<div class="col-xs-2 col-md-1">
<img src="/mugshots/ameliemuller.jpg" class="img-circle" style="width: 70px; height: 70px"  />
</div>
<div class="col-xs-10 col-md-5" markdown="1">
**Amélie Muller** was a master's student from Strasbourg University, doing a
6-months research stay in the group. Her work focused on understanding how
interactions with pollinators contribute to the persistence of plants at
different spatial scales, and how management programs could gain from relying on
the variability of interactions.
</div>

</div>


[qcbs]: http://qcbs.ca/fr/membres/les-chercheurs/?profile=166
[dom]: http://chaire-eec.uqar.ca/
[skemb]: http://phylodiversity.net/skembel/index.html
[stouffer]: http://stoufferlab.org/
