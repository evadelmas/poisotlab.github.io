---
layout: page
title: People
nav: people
---

{% for p in site.data.people %}{% if p.pi %}
{% include people.html %}{% endif %}
{% endfor %}

# Current lab members

{% for p in site.data.people %}{% if p.current %}
{% include people.html %}{% endif %}
{% endfor %}

# Former lab members

{% for p in site.data.people %}{% if p.former %}
{% include people.html %}{% endif %}
{% endfor %}

[qcbs]: http://qcbs.ca/fr/membres/les-chercheurs/?profile=166
[dom]: http://chaire-eec.uqar.ca/
[skemb]: http://phylodiversity.net/skembel/index.html
[stouffer]: http://stoufferlab.org/
