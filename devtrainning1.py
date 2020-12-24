import requests
from bs4 import BeautifulSoup


url = "http://45.79.43.178/source_carts/wordpress/wp-login.php"
payload = {'log': 'admin',
         'pwd': '123456aA'}
s = requests.session()
r = s.post(url,data=payload)
soup = BeautifulSoup(r.content, "html.parser")
print(soup.find('span',class_='display-name').text)


