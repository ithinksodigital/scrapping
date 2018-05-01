from bs4 import BeautifulSoup
import requests

URL = "https://antal.pl/oferty-pracy?s=&sid=&did={}"

def antal_pl(name):
    res = requests.get(URL.format(name))
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find(class_='header').find_next_sibling().text.strip()
    print(data)

if __name__ == '__main__':
    antal_pl("Accountancy")