---
layout: single
title: Publications
permalink: /publications/
---

{% assign my_name = "Ciccarino, C.J." %}
{% assign my_name_bold = "<strong>" | append: my_name | append: "</strong>" %}


{% assign preprints_by_year = site.data.preprints | group_by: "year" | sort: "name" | reverse %}

{% assign count = site.data.preprints.size %}

For a full list, see [Google Scholar](https://scholar.google.com/citations?user=KXi1HWMAAAAJ&hl=en). Equal contribution is denoted by <sup>★</sup>.

## Preprints
{% for year_group in preprints_by_year %}
{% assign pubs_sorted = year_group.items | sort: "month" | reverse %}
{% for pub in pubs_sorted %}
{{ count }}&#46; {{ pub.authors }}
"{{ pub.title }}."
_{{ pub.journal }}_,
{% if pub.volume %} **{{ pub.volume }}**, {% endif %} {% if pub.number %} {{ pub.number }}, {% endif %} {% if pub.pages %} {{ pub.pages }}, {% endif %} ({{ pub.year }}).
{% if pub.doi %} 🔗 [DOI]({{ pub.doi }}){% endif %} {% if pub.arxiv %} 📄 [arXiv]({{ pub.arxiv }}){% endif %}
{% assign count = count | minus: 1 %}
{% endfor %}
{% endfor %}


{% assign pubs_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

{% assign count = site.data.publications.size %}

## Publications
{% for year_group in pubs_by_year %}
{% assign pubs_sorted = year_group.items | sort: "month" | reverse %}
{% for pub in pubs_sorted %}
{{ count }}&#46; {{ pub.authors }} 
"{{ pub.title }}."
_{{ pub.journal }}_, 
{% if pub.volume %} **{{ pub.volume }}**, {% endif %} {% if pub.number %} {{ pub.number }}, {% endif %} {% if pub.pages %} {{ pub.pages }}, {% endif %} ({{ pub.year }}).
{% if pub.doi %} 🔗 [DOI]({{ pub.doi }}){% endif %} {% if pub.arxiv %} 📄 [arXiv]({{ pub.arxiv }}){% endif %}
{% assign count = count | minus: 1 %}
{% endfor %}
{% endfor %}



