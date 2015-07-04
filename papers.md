---
layout: page
title: Selected papers
nav: papers
---

<div class="row" markdown="1">
# Most representative, recent, or cool papers from the lab.<br />[But we have more](/allpapers/)!
</div>

{% for p in site.papers %}{% if p.featured %}
<div class="row">

<div class="col-md-9">
<span class="badge">{{forloop.rindex}}</span> <b>{{p.title}}</b><p />
{% for a in p.authors %}<span class="author {{a.type}}">{{ a.name }}</span>{% if forloop.last %}{% else %}, {% endif %}{% endfor %}
<br />{{ p.date }}{% if p.in %}; <em>{{ p.in }}</em>{% else %}{% if p.preprint %}; preprint{% endif %}{% endif %}
</div>

<div class="col-md-3">
{% if p.pdf %}<a href="/pdf/{{p.pdf}}" title="{{p.title}}"><span class="label label-success">Full text PDF</span></a>{% endif %}

{% if p.preprint %}<a href="http://dx.doi.org/{{p.doi}}"><span class="label label-info">Citable preprint</span></a>{% endif %}

{% if p.in %}{%if p.doi %} <a href="http://dx.doi.org/{{p.doi}}"><span class="label label-warning">Journal version</span></a>{% endif %}<p />{% endif %}</div>
</div>
<hr/>
{% endif %}{% endfor %}
