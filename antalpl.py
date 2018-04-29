from bs4 import BeautifulSoup
import requests
import re

a = {}


def antal_pl(link, name=''):
    try:
        page_response = requests.get(link, timeout=10).text
        page_content = BeautifulSoup(page_response, 'lxml').find(class_='header').find_next_sibling().text.strip()
        rm_str = re.sub( '[^0-9]', '', page_content )

        new_entry = {
            name: int(rm_str)
        }

    except:

        new_entry = {
            name: 0
        }

    a.update(new_entry)

def antal_scrap():
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Accountancy', 'Accontancy')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Actuaries', 'Actuaries')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Administration+Support', 'Administration Supoort')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Banking%2C+Financial+Services+%26+Investment', 'Banking, Financial services & Investment')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Consulting', 'Consulting')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Design%2C+Construction', 'Design, Construction')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Engineering', 'Engineering')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Fashion', 'Fashion')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=General+Management%2C+Board', 'General Management, Board')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Health%2C+Safety%2C+Environment', 'Health, Safety, Environment')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Human+Resources', 'Human Resources')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=IT+%26+Telecom+Technical', 'IT & Telecom Technical')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Law%2C+Legal', 'Law, Legal')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Logistics%2C+Suply+chain', 'Logistic, suply chain')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Media', 'Media')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Operations', 'Operations')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Procurement%2C+Purchasing', 'Procurement, Purchasing')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+.NET', 'Programista .NET')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Android', 'Programista Android')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+aplikacji+mobilnych', 'Programista aplikacji mobilnych')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+ASP.net', 'Programista ASP.net')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+C%23', 'Programista C')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+C%2B%2B', 'Programista C ++')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Front-End', 'Programista Front-End')
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+iOS', 'Programista iOS' )
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+JAVA', 'Programista JAVA')
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Programista+perl', 'Programista Perl')
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+PHP', 'Programista PHP' )
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Python', 'Programista Python' )
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Rails', 'Programista Rails' )
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Public+Sector%2C+Education%2C+Health', 'Public Sector, Education, Health' )
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=R%26D%2C+Clinical%2FHealthcare%2C+Pharma', 'R&D, Clinical/Healthcare, Pharma' )
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Sales%2C+Marketing%2C+PR', 'Sales, Marketing, PR')
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Telekomunikacja', 'Telekomunikacja' )
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Testowanie', 'Testownie' )
    antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Training', 'Training' )
    antal_pl('https://antal.pl/oferty-pracy?s=&sid=&did=Zarz%C4%85dzanie+IT&bid=&wid=&mid=&pid=&pr=50&maps=&lat=51.919438&lng=19.14513599999998', 'Zarzadzanie IT')
