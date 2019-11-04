from bs4 import BeautifulSoup
import requests

url = 'http://eventhubs.com/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content,"html.parser")
print (content)