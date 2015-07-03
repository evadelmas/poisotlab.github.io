---
layout: page
title: Papers
nav: papers
---

# Selected papers

These are the most representative, recent, or cool papers from the lab. [But we have more](/allpapers/)!

{% for p in site.papers %}{% if p.featured %}<div class="bibitem">
{{forloop.rindex}}. <span class="title">{{p.title}}</span> ({{ p.date }}{% if p.preprint %}; preprint{% endif %})<p /><span class="authors">{% for a in p.authors %}
<span class="author {{a.type}}">{{ a.name }}</span>{% if forloop.last %}{% else %}, {% endif %}{% endfor %}</span><p />
{% if p.pdf %}<span class="fulltext"><a href="/pdf/{{p.pdf}}" title="{{p.title}}">Full text PDF</a>{% if p.preprint %} &mdash; <a href="http://dx.doi.org/{{p.doi}}">Citable preprint</a>{% endif %}</span><p />{% endif %}
{% if p.in %}Published in <em>{{ p.in }}</em>{%if p.doi %} <a href="http://dx.doi.org/{{p.doi}}">journal version</a> &mdash; <code>{{p.doi}}</code>{% endif %}<p />{% endif %}</div>{% endif %}{% endfor %}
