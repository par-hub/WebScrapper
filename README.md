# WebScrapper

A small Python web-scraping example that requests an Amazon India product-search page, parses product links with Beautiful Soup, visits product pages, and collects selected product fields into a CSV.

## What it extracts
- Product title
- Displayed price
- Rating
- Review-count text
- Availability text

The current example URL and HTML selectors are hard-coded in `project 1.py`; the exact data returned depends on the page markup and the site's response.

## Requirements
Python 3.10+ is recommended.

~~~bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install requests beautifulsoup4 lxml pandas numpy
~~~

## Run

~~~bash
python "project 1.py"
~~~

The script writes a CSV file named `amazon_data.csv` when the expected product fields can be extracted.

## Notes
- This is an educational example, not a production crawler.
- Product-page HTML and CSS selectors can change, and automated requests may be rate-limited or blocked.
- Review the target site's terms and applicable rules before scraping; keep request volume low and do not bypass access controls.
- Consider moving the URL and output path into command-line arguments before extending the script.
