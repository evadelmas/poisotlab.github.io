---
layout: page
title: Papers
nav: papers
featured:
  - pois14sei
  - pois15ppi
  - pois15sdc
  - pois15spn
sorted: []
---

<!-- NOTE this block will assign the empty page.sorted array to a new array
called pubs, then add references sorted in reverse chronological order to it.
The rest of the page will iterate over pubs, which will therefore be sorted. -->

{% assign pubs = page.sorted %}
{% for pubyear in (2005..2020) reversed %}
{% for p in site.data.bib %}
{% if p.issued.date-parts[0][0] == pubyear %}
{% assign pubs = pubs | push: p %}
{% endif %}{% endfor %}
{% endfor %}

# Selected papers

{% for p in pubs %}
{% if page.featured contains p.id %}
{% include bibentry.html %}
{% endif %}{% endfor %}

# Preprints and reports

{% for p in pubs %}{% if p.type == "report" %}
{% include bibentry.html %}
{% endif %}{% endfor %}

# Research articles

{% for p in pubs %}{% if p.type == "article-journal" %}
{% include bibentry.html %}
{% endif %}{% endfor %}

# Other publications

{% for p in pubs %}
{% if p.type == "reference-entry"%}
{% include bibentry.html %}
{% endif %}
{% if p.type == "chapter"%}
{% include bibentry.html %}
{% endif %}
{% endfor %}

{% comment %}

**T. Poisot** (2012) L'ABC de la spécialisation: apparition, biodiversité, conservation. *Le Prisme à Idées* 4, 49-52. Vulgarization paper in French for the special issue *From uncertainty to risk*. [pdf]( {{ site.url }}/reprints/poisot_prisme_abc.pdf).

P.&nbsp;Desjardins-Proulx, **T. Poisot**, & D. Gravel (2012). A simple algorithm to study phylogeographies & speciation patterns in space. *ArXiV*. [pdf]({{ site.url }}/reprints/phdp_arxiv_wagner.pdf). <i class="fa fa-unlock-alt"></i>

P.S. Jørgensen, V. Bonhomme, T.H.G. Ezard, R.A. Hayes, **T. Poisot**, R. Salguero-gomez, S. Vizzini, N. Zimmerman. (2011) A global network of next generation ecologists. *INTECOL Bulletin* 5 (2) 4-6. [pdf]({{ site.url }}/reprints/jorgensen_intecol_innge.pdf).

**T. Poisot** (2011) The digitize Package: Extracting Numerical Data from Scatterplots. *The R Journal* 3 (1) 25–26. [pdf]({{ site.url }}/reprints/poisot_rjournal_digitize.pdf), [R package](https://github.com/tpoisot/digitize). <i class="fa fa-unlock-alt"></i>

**T. Poisot**, A. Simková, P. Hyrsl & S. Morand (2009) Interactions between immunocompetence, somatic condition and parasitism in the chub *Leuciscus cephalus* in early spring. *Journal of Fish Biology* 75 (7) 1667-1682. [pdf]({{ site.url }}/reprints/poisot_jfishb_chub.pdf).

Hart et al.

Mattias phage thing

Morand Nunn

Desjardins Proulx arxiv

{% endcomment %}
