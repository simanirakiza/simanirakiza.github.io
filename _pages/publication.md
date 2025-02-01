---
layout: archive
title: "Publications"
permalink: /publication/
author_profile: true
---

## Publications

{% for pub in site.data.publications %}
- **Title:** [{{ pub.title }}]({{ pub.link }})  
  **Year:** {{ pub.year }}  
  **Venue:** {{ pub.venue }}  
  **Authors:** {{ pub.authors | join: ', ' }}  
  [View on Google Scholar]({{ pub.link }})  
  ---
{% endfor %}
