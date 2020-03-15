import requests
from bs4 import BeautifulSoup, Comment
import csv
import constants

# Basketball Reference's homepage for team data
BASE_URL = 'https://www.basketball-reference.com'

def scrapePlayer(name):
    flName = name.strip().lower().split()
    # Have to figure out how to check for players with same names (eg. Gary Payton)
    nameUrl = '/'.join([BASE_URL, 'players', flName[1][0], flName[1][:5] + flName[0][:2] + '01.html'])
    request = requests.get(nameUrl)
    soup = BeautifulSoup(request.content, 'html.parser')

    perGameElem = soup.find('div', id='all_per_game')
    perGameStatRow = perGameElem.find('tbody').findAll('tr')
    





def scrapeSeason(year):
    print('aa')



