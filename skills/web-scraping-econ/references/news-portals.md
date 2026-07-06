# News Portals for Sentiment/Event Data

## Description
News websites aggregate policy announcements, central bank speeches, and macro event coverage. Scrapers extract headlines, timestamps, authors, and article text for sentiment or event tagging when ready-made feeds are unavailable.

## Notes
- Fetch pages with `requests` (Session + headers) and parse the returned HTML with BeautifulSoup to anchor on stable article containers (e.g., `<article>`, list items, `<h2>` tags).
- Prefer RSS feeds or JSON endpoints (often at `/newsfeed` or `/api`) before scraping rendered pages.
- Capture metadata (`published_at`, `category`, `source`) and normalize timestamps to UTC for consistent labeling.
- Verify compliance with `robots.txt` and limit requests (e.g., sleep 1–2 seconds) to avoid throttling or IP bans.

## Example Targets
1. Reuters Economics: https://www.reuters.com/markets/economy/ (inspect data attributes for metadata).  
2. Financial Times: use `/world/economics` without scraping paywalled content.  
3. Central bank release newsrooms (e.g., https://www.bis.org/press/pres.htm).

## Parsing Tips
- Normalize timestamps to UTC; handle relative times like “2 hours ago.”  
- Extract clean text by joining `<p>` elements inside the article body and removing navigation noise.  
- Rate limit to avoid IP bans and cite robots.txt restrictions before each run.
