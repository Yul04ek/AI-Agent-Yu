---                                                           
 name: web-scraping-econ
 description: Load this skill when an economist needs to gather data from economic websites not covered by ready-made downloads.
---                                                                                                                                                                                         
                                                           
 * Match the user’s target to one of the reference modules:
 * `references/central-bank.md` for central bank statistics portals.
 * `references/exchanges.md` for stock, bond, or FX exchange feeds (note when JavaScript rendering blocks requests+BeautifulSoup). 
 * `references/news-portals.md` for news/press sources used for sentiment or event data. 
 * Follow the outlined workflow in the selected reference, customizing selectors, headers, and retries for the specific page layout.
 * When feasible, collect structured rows (date + value) and explain the data collection steps in the response so the economist can verify provenance. 
