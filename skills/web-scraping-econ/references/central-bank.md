# Central bank statistics pages

1. **Confirm scraping is permitted.** Check `robots.txt` and any published APIs or data portals before scraping.
2. **Use `requests` with a session.** Set a realistic `User-Agent` header, handle timeouts, and respect rate limits or pagination cues the bank provides.
3. **Fetch the HTML and parse with BeautifulSoup.** Target known structures (tables, `div` with `data-*` attributes, etc.) rather than hard-coding full URLs.
4. **Extract rows carefully.** For tables, iterate `soup.select("table tbody tr")`, pull cells with `.get_text(strip=True)`, and map dates to values.
5. **Normalize dates/values.** Convert to `datetime.date` and `float` inside `try/except` blocks so malformed rows are skipped.
6. **Cache or store metadata.** Save the source URL/time and describe in your answer how the rate was computed, including any filters applied.

## Verified example: ECB exchange rates via SDMX API

For ECB exchange rate data, prefer the official SDMX REST API over HTML 
scraping — it returns structured JSON directly, no table parsing needed.

- **Base URL**: `https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A`
  (do NOT use the old `sdw-wsrest.ecb.europa.eu` domain — it is deprecated 
  and no longer resolves)
- **Path prefix**: must be `/service/data/...`, not `/api/data/...`
- **Query params**: `startPeriod` and `endPeriod` in `YYYY-MM-DD` format
- **Required header**: `Accept: application/vnd.sdmx.data+json;version=1.0.0-wd`
  (the `-wd` suffix is required — without it the server returns 406 Not Acceptable)
- **Response format**: SDMX-JSON. Parse via 
  `payload["dataSets"][0]["series"]` for observation values and 
  `payload["structure"]["dimensions"]["observation"][0]["values"]` for the 
  corresponding dates (matched by index).
- Swap the currency code in the key (`D.USD.EUR.SP00.A`) to fetch other 
  pairs, e.g. `D.GBP.EUR.SP00.A` for GBP/EUR.
