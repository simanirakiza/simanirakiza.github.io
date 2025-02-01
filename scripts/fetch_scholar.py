from scholarly import scholarly
import json

# Replace with your Google Scholar Profile ID
scholar_id = "GSCldEoAAAAJ&hl=en"

# Fetch profile
author = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["publications"])

# Extract publication details
publications = []
for pub in author['publications']:
    pub_details = {
        "title": pub.get('bib', {}).get('title', 'N/A'),
        "year": pub.get('bib', {}).get('pub_year', 'N/A'),
        "link": f"https://scholar.google.com/citations?view_op=view_citation&hl=en&user={scholar_id}&citation_for_view={pub['author_id']}"
    }
    publications.append(pub_details)

# Save as JSON
with open("_data/publications.json", "w") as f:
    json.dump(publications, f, indent=4)
