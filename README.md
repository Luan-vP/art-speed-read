The goal is to create a RSVP-style art speedreader, scraping images from the Google Art and Culture databases, and presenting them serially, while scaled to make them easy to read. 

# Goals
- To be able to speed read any of the categories on the Google Art and Culture website

# Components
- Image scraper to download images to /tmp file - scrape_images.py
- - Adapt to page type
- Compile and view images - view_images.py
- Command-line interface to permit custom search term 

# Usage
- run scrape_images.py
- then run read_images.py from same directory