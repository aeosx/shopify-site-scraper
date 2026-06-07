# shopify-site-scraper

Basic info:
uses the private javascipt endpoint by just adding ".js" to the end of a shopify store link
then it filters through the data to reach the variants and read their availibility

Limitations:
Has not been tested on many shopify sites, may not work on all.
Has been tested on:

coldcultureworldwide.com

More will be added.

Usage
Personal Computer:
1. Download the personal pyscraper.py file and default selectstock.json and stock.json files and run. Place all files in the same folder.
2. Replace webhookurl variable with your discord webhook URL
3. Enter item URL (ex: https://coldcultureworldwide.com/products/curved-tee-eclipse  DO NOT ADD .js)
4. Select size
5. Press ESC to cancel scan

Server side file is only for servers, and not good to use on pc.
