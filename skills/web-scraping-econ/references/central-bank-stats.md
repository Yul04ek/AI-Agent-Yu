# Central Bank Statistics Pages

## Description
Many central banks publish macroeconomic indicators (interest rates, reserve requirements, balance-of-payments reports, etc.) in HTML tables or PDFs. When APIs are unavailable, parse their statistics pages with careful requests and HTML parsing.

## Notes
- Start with `requests.Session()` to set headers (User-Agent, Accept) and sensible timeouts; always check `robots.txt` first.
- Feed the fetched HTML into BeautifulSoup (e.g., `BeautifulSoup(resp.text, "html.parser")`) and target the `<table>` or `<div>` containers that hold series data.
- Track pagination or date filters through query parameters, caching tokens, or `data-*` attributes when reconstructing historical series.
- Throttle loops (e.g., `time.sleep(1)`) and honor `Retry-After` to avoid overwhelming the server.

## Example Targets
1. Federal Reserve: https://www.federalreserve.gov/releases.htm (tables with release calendars).  
2. European Central Bank: https://www.ecb.europa.eu/stats/html/index.en.html.  
3. Bank of England: https://www.bankofengland.co.uk/statistics.

## Parsing Tips
- Use BeautifulSoup selectors (`select_one`, `select`) instead of brittle string splits to isolate rows and columns.
- Normalize dates to ISO format and cast numeric strings to `float` or `Decimal`; treat `-` or `—` as missing values.
- Document the scraped URL, timestamp, and any applied filters for reproducibility.
