import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Set initial URL
url = "http://py4e-data.dr-chuck.net/known_by_Lucia.html"

for _ in range(7):
    # Read the HTML from the current URL
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    tags = soup('a')

    # Find the link at position 18 (index 17)
    link = tags[17].get('href')

    # Update the URL for the next iteration
    url = urllib.parse.urljoin(url, link)

# Print the last name retrieved
last_name = url.split('/')[-1]
print("Last Name:", last_name)
