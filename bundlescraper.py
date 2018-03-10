#!/usr/bin/info python

import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/code-your-own-games-books"

tier_dict = {}

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

# Bundle Tiers (.dd-game-row)
tiers = soup.select(".dd-game-row")

for tier in tiers:
	# Only for sections that have a headline
	if tier.select(".dd-header-headlines"):
		# Grab tier name (and price)
		tiername = tier.select(".dd-header-headlines")[0].text.strip()
		
		# Grab tier product names
		product_names = tier.select(".dd-image-box-caption"
		product_names = [prodname.text.strip() for prodname in product_names]
		
		# Add one product tier to datastructure
		tier_dict[tiername] = { "products": product_names }

## Common access pattern	 
for tiername, tierinfo in tier_dict.items():
	  print(tiername)	
	  print("#########################")
	  print("\n".join(tierinfo['products']))
	  print("\n\n")


# Old Teirs (.dd-header-headline)
#tier_headlines = soup.select(".dd-header-headline")
#stripped_headlines = [tier.text.strip() for tier in tier_headlines]


## Product Names (.dd-image-box-caption)
#pruduct_names = soup.select(".dd-image-box-caption")
#stripped_product_names = [prodname.text.strip() for prodname in pruduct_names]


## This is the datastructure used to store bundle info
# tiers = {
#	"tier1": {
#		"price": 500,
#		"products": [
#			"name1",
#			"name2"
#		]
#	},
#	"tier2": {
#		"price": 500,
#		"products": [
#			"name1",
#			"name2"
#		]
#	}
# }


## DATA STRUCTURE IDEA
# -tier1 name and price
#	- product 1
#	- product 2
# -tier2  name and price
#	- product 1
#	- product 2