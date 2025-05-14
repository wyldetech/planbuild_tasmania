# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
elements = root.cssselect("div.wrapper div.row.advertisement-result-row")

for element in elements:
    print(element.text_content())

#






# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['council_reference'], 
#    data = {
#    "council_reference": "susan", 
#    "address": "software developer",
#    "description": "Description",
#    "on_notice_to": Date.today,
#    "date_scraped": Date.today,
#    "info_url": f"url{id}",
#    "comment_authority": "COH",
#    "comment_email": "representation@hobartcity.com.au"
#    }
#    )






#
# # An arbitrary query against the database
#scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
