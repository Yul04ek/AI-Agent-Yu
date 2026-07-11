 # Stock, bond, and currency exchanges
                                                                                                                                                                                              
 1. **Identify whether the page renders data via plain HTML.** Prefer tables or list items delivered with the initial HTML; these can be handled with `requests` + `BeautifulSoup`.
 2. **If data loads through JavaScript (watch the Network tab or look for `fetch`/`XHR` calls), note that requests+BS4 cannot capture it directly.** In those cases, try to replicate the API 
 call that provides the data; if no API is exposed, explain to the user that a headless browser is required.
 3. **For HTML-accessible data:**
    * Fetch with `requests.get`.
    * Parse with `BeautifulSoup`.
    * Use CSS selectors to isolate rows (`soup.select("tbody tr")`, etc.). 
    * Build a list of `(timestamp, price)` tuples by parsing each cell, handling commas or currency symbols. 
 4. **Cross-check timestamps.** Exchanges often label in UTC or local timezone; convert to `datetime` and annotate how the timestamp relates to the user’s time zone.
 5. **Document limitations.** If the exchange refreshes via WebSockets or JS, explicitly flag the shortcoming in the response so the economist can plan for headless browsers or official APIs.
