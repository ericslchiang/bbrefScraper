import requests
from bs4 import BeautifulSoup, Comment
import csv
import constants
import pandas as pd
import pprint

# Basketball Reference's homepage for team data
BASE_URL = 'https://www.basketball-reference.com'
pp = pprint.PrettyPrinter(indent=4)

def scrapePlayer(name):
    flName = name.strip().lower().split()
    # Have to figure out how to check for players with same names (eg. Gary Payton)
    nameUrl = '/'.join([BASE_URL, 'players', flName[1][0], flName[1][:5] + flName[0][:2] + '01.html'])
    request = requests.get(nameUrl)
    soup = BeautifulSoup(request.content, 'html.parser')

    perGameElem = soup.find('div', id='all_per_game')
    perGameStats = [] 
    for category in perGameElem.find('thead').findAll('th'):
        perGameStats.append(category.getText())
    perGameStatRow = perGameElem.find('tbody').findAll('tr')

    rowData = []
    for row in perGameStatRow:
        temp = []
        for child in row.children:
            temp.append(child.getText())
        rowData.append(temp)
    
    data = pd.DataFrame(data=rowData, columns=perGameStats)
    data.to_excel('output.xlsx')

    





def scrapeSeason(year):
    print('aa')



