# Stock and Currency Exchange Data

## Description
Exchange websites provide price grids, bid/ask spreads, and historical trade data. Scraping may require parsing tables or JSON endpoints embedded in the page.

## Notes
- Start with the exchange’s official data API or download center; fallback to scraping if data is only rendered in the DOM.
- Use `requests` + BeautifulSoup to fetch and read HTML tables before escalating to more complex stacks.
- Inspect network activity to detect AJAX calls returning JSON; replicate those requests with appropriate headers (User-Agent, Accept) when tables are loaded asynchronously.
- Respect rate limits and session authentication; reuse session cookies if needed.
- Consider licensing restrictions—many exchanges disallow redistribution of live tick data.
- When pages rely on JavaScript rendering for prices (e.g., live dashboards), note that `requests` + BeautifulSoup alone may not capture the data; verify if a raw JSON endpoint exists before considering headless browsers.

## Example Targets
1. National Stock Exchange of India: https://www.nseindia.com/market-data/live-market-indices.  
2. Mercado de Valores in Latin America: numerous markets provide HTML price tables.  
3. ECB exchange rates table: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html.

## Parsing Tips
- Use `json.loads` when the page embeds JavaScript objects containing prices.
- For HTML tables, clean up thousands separators and convert to `float` or `Decimal`.  
- Document the currency pair, timestamp, and source URL for each scrape.
