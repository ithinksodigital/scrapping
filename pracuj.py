from bs4 import BeautifulSoup
import requests
import re


def get_value(link):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='o__search_results_title_number')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)
        print(rm_str)
    except:
        print('Sorry, timeout. ')


print('Hays:')
get_value('https://www.pracuj.pl/praca/Hays%20Poland;en')
print('Grafton:')
get_value('https://www.pracuj.pl/praca/grafton;kw')
print('Randstad:')
get_value('https://www.pracuj.pl/praca/Randstad%20Polska;en')
print('Antal:')
get_value('https://www.pracuj.pl/praca/antal;en')
print('Manpower:')
get_value('https://www.pracuj.pl/praca/Manpower;en')
print('Devire:')
get_value('https://www.pracuj.pl/praca/devire;en')
print('HRK S.A')
get_value('https://www.pracuj.pl/praca/HRK%20S.A.;en')
