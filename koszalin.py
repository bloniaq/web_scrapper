import requests
from bs4 import BeautifulSoup

starter_url = 'http://rj.mzk.koszalin.pl'
req_line = '8'


def get_line_url(line_number):
    r = requests.get(starter_url)
    soup = BeautifulSoup(r.text, "lxml")
    table = soup.find('table', {'class': 'linie'})
    lines = table.findAll('a')
    for line in lines:
        if line.contents[0] == line_number:
            href = line['href']
            break
    return starter_url + '/' + href


def print_direction(direction, table):
    stations = table.findAll('a')
    print('\n\nKIERUNEK ' + direction + '\n')
    for station in stations:
        dir_ = station['href'].split('&')
        if dir_[1] == 'kierunek=' + direction:
            try:
                print(station.contents[0])
            except IndexError:
                break


def get_line_schedule(line_number):
    line_url = get_line_url(line_number)
    r = requests.get(line_url)
    soup = BeautifulSoup(r.text, "lxml")
    table = soup.find('table', {'class': 'trasa'})
    print_direction('A', table)
    print_direction('B', table)


get_line_schedule(req_line)
