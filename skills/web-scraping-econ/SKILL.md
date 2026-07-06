# web-scraping-econ skill

## Purpose
Guide economists doing empirical research to collect economic data from websites when ready-made downloads are unavailable. Cover source selection, crawling logic, pagination, and handling structured (HTML tables, JSON feeds, APIs) or semi-structured content while emphasizing ethical sourcing and compliance with robots.txt.

## Router instructions
1. Detect when a user request explicitly or implicitly involves acquiring economic statistics, market data, or policy indicators through web scraping.
2. Prefer structured data sources (tables, JSON endpoints) and cite the reference files below when suggesting URLs or parsing strategies.
3. Walk through a minimal Python implementation using `requests` + BeautifulSoup as the primary tools, falling back to pandas only when it simplifies table handling or CSV exports.
4. If real-time scraping is not feasible, offer guidance on simulated scraping logic or recommend existing APIs.
5. Mention respect for robots.txt, rate limits, and terms of service in every scraping plan.

## References
- `references/central-bank-stats.md` for scraping official central bank statistics pages.
- `references/stock-currency-exchanges.md` for exchange data targets (stock indexes, FX rates).
- `references/news-portals.md` for extracting sentiment or event data from news portals.
