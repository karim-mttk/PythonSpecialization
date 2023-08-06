from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Find all span tags and extract their text content
span_tags = soup.find_all('span')
total = 0

for span in span_tags:
    # Convert text content to integer and add to total
    content = span.text
    try:
        number = int(content)
        total += number
    except ValueError:
        print('Invalid number:', content)

print('Sum of numbers in span tags:', total)
