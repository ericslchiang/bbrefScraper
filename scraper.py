import requests
from bs4 import BeautifulSoup
import pandas as pd

# Basketball Reference's homepage for team data
BASE_URL = 'https://www.basketball-reference.com'


def scrapePlayer(name):
    flName = name.strip().lower().split()
    # Have to figure out how to check for players with same names (eg. Gary Payton)
    nameUrl = '/'.join([BASE_URL, 'players', flName[1][0], flName[1][:5] + flName[0][:2] + '01.html'])
    try:
        request = requests.get(nameUrl)
        if request.status_code != 200:
            raise Exception('Error: Cannot find player')
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
    except Exception as ex:
        print(ex)


def scrapeSeason(year):
    yearUrl = '/'.join([BASE_URL, 'leagues', f'NBA_{year}_per_game.html'])

    try:
        request = requests.get(yearUrl)
        if request.status_code != 200:
            raise Exception('Error: Cannot find season')
        soup = BeautifulSoup(request.content, 'html.parser')

        dataTableElem = soup.find('div', id='all_per_game_stats')
        perGameStats = []
        for category in dataTableElem.find('thead').findAll('th'):
            perGameStats.append(category.getText())

        perGameStatRow = dataTableElem.find('tbody').findAll('tr', class_='full_table')
        rowData = []
        for row in perGameStatRow:
            temp = []
            for child in row.children:
                temp.append(child.getText())
            rowData.append(temp)

        data = pd.DataFrame(data=rowData, columns=perGameStats)
        data.to_excel('output.xlsx')
    except Exception as ex:
        print(ex)