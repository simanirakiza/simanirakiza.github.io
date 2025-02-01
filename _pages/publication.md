---
layout: archive
title: "Publications"
permalink: /publication/
author_profile: true
---

## Publications

{% for pub in site.data.publications %}
- **Title:** [{{ pub.title }}]({{ pub.link }})  
  {{ pub.venue }}, {{ pub.year }} 
  **Authors:** {{ pub.authors | join: ', ' }}  
  [View on Google Scholar]({{ pub.link }})  
  ---
{% endfor %}
