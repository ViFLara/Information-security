from bs4 import BeautifulSoup
import requests

# site object receiving the content of the site's http request
site = requests.get('https://www.climatempo.com.br/').content

# soup object downloading the html from the website
soup = BeautifulSoup(site, 'html.parser')

# transform html into string
# print(soup.prettify())

temperature = soup.find(class_="lazyload")
print(temperature.string)

print(soup.text)
print(soup.a)
