# News portals for sentiment or event data                                                                                                                                                   
                                                                                                                                                                                              
 1. **Review the site layout and constraints.** Many news portals provide archive pages with consistent headlines/timestamps; locate a container (e.g., `.article-list`).
 2. **Fetch the listing page(s) with `requests`.** Parse with `BeautifulSoup`, then iterate each article block to extract date, headline, and a short summary. 
 3. **Normalize text fields.** Strip whitespace, replace newlines, and optionally limit the summary length before returning. 
 4. **Follow pagination if necessary.** Detect a “next page” anchor, update the URL, and continue until the desired date range is covered or a limit is reached.
 5. **Mention any dynamic loading.** If the portal uses infinite scroll or fetches more articles via JS, explain that requests+BS4 will only see the initial batch, so suggest capturing the API endpoint or using a browser automation tool.
