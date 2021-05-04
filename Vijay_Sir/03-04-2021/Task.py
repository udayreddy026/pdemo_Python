import requests
from bs4 import BeautifulSoup

req = requests.get("https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)")
text = BeautifulSoup(req.content)

file = open('E:/pdemo_Python/Vijay_Sir/03-04-2021/demo.txt', 'a')
file.writelines(text.get_text())
file.close()

