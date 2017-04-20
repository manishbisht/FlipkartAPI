import urllib2
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Fk-Affiliate-Id': 'bestshopp',
	'Fk-Affiliate-Token': '21719d092a4c47bba14ee26dc9726988'
}
def lambda_handler(event, context):
    # TODO implement
    url = "https://affiliate-api.flipkart.net/affiliate/search/json?resultCount=10&query="+event['name'].replace(" ", '+')
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    content = page.read()
    return content
