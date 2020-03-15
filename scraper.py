import requests
from bs4 import BeautifulSoup
import pandas as pd

# Basketball Reference's homepage for team data
BASE_URL = 'https://www.basketball-reference.com'


def scrapePlayer(name):
    flName = name.strip().lower().split()
    #TODO check for players with same names (eg. Gary Payton)
    nameUrl = '/'.join([BASE_URL, 'players', flName[1][0], flName[1][:5] + flName[0][:2] + '01.html'])
    request = requests.get(nameUrl)
    try:
        if request.status_code != 200:
            raise Exception('Error: Cannot find player')
        
        soup = BeautifulSoup(request.content, 'html.parser')
        statCategories, rowData = [], []

        perGameElem = soup.find('div', id='all_per_game')
        for category in perGameElem.find('thead').findAll('th'):
            statCategories.append(category.getText())

        perGameStatRow = perGameElem.find('tbody').findAll('tr')
        for row in perGameStatRow:
            temp = []
            for child in row.children:
                temp.append(child.getText())
            rowData.append(temp)

        data = pd.DataFrame(data=rowData, columns=statCategories)
        data.to_csv(path_or_buf=f'./output/NBA_{name}.csv', index=False)
    except Exception as ex:
        print(ex)


def scrapeSeason(year):
    yearUrl = '/'.join([BASE_URL, 'leagues', f'NBA_{year}_per_game.html'])
    request = requests.get(yearUrl)

    try:
        if request.status_code != 200:
            raise Exception('Error: Cannot find season')
        
        soup = BeautifulSoup(request.content, 'html.parser')
        statCategories, rowData = [], []

        dataTableElem = soup.find('div', id='all_per_game_stats')
        for category in dataTableElem.find('thead').findAll('th'):
            statCategories.append(category.getText())

        perGameStatRow = dataTableElem.find('tbody').findAll('tr', class_='full_table')
        for row in perGameStatRow:
            temp = []
            for child in row.children:
                temp.append(child.getText())
            rowData.append(temp)

        data = pd.DataFrame(data=rowData, columns=statCategories)
        data.to_csv(path_or_buf=f'./output/NBA_{year}_Season.csv', index=False)
    except Exception as ex:
        print(ex)