from scholarly import scholarly
import json

# Replace with your Google Scholar Profile ID
scholar_id = "GSCldEoAAAAJ"

# Fetch profile
author = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["publications"])

# Extract publication details
publications = []
for pub in author['publications']:
    # print(pub) 
    pub_details = {
        "title": pub.get('bib', {}).get('title', 'N/A'),
        "year": pub.get('bib', {}).get('pub_year', 'N/A'),
        "venue": pub.get('bib', {}).get('citation', 'N/A'),
        "link": f"https://scholar.google.com/citations?view_op=view_citation&hl=en&user={scholar_id}&citation_for_view={pub['author_pub_id']}"
    }
    publications.append(pub_details)

# Save as JSON
with open("_data/publications.json", "w") as f:
    json.dump(publications, f, indent=4)

   # {'container_type': 'Publication', 'source': <PublicationSource.AUTHOR_PUBLICATION_ENTRY: 'AUTHOR_PUBLICATION_ENTRY'>,
   #  'bib': {'title': 'Time-aware deep neural networks for needle tip localization in 2D ultrasound', 
   #          'pub_year': '2021', 'citation': 'International Journal of Computer Assisted Radiology and Surgery 16, 819-827, 2021'},
   #  'filled': False, 'author_pub_id': 'GSCldEoAAAAJ:u-x6o8ySG0sC', 'num_citations': 29, 
   #  'citedby_url': 'https://scholar.google.com/scholar?oi=bibs&hl=en&cites=7448870732632863848', 'cites_id': ['7448870732632863848']}
