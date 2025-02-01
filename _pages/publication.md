---
layout: archive
title: "Publications"
permalink: /publication/
author_profile: true
---

## Publications

{% for pub in site.data.publications %}
- **{{ pub.title }}** ({{ pub.year }})  
  [View on Google Scholar]({{ pub.link }})
{% endfor %}
