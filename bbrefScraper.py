import constants
import scraper

flag = True
player, year = '', ''
while (flag): 
    mode = input('Enter \'1\' to get a player\'s career statistics OR \'2\' to get the data of all players that year: \n')
    if mode == '1':
        player = input('Enter player\'s first and last name in that order (eg. Michael Jordan)\n')
        scraper.scrapePlayer(player)
        flag = False
    elif mode == '2':
        year = input('Enter season year\n')
        scraper.scrapeSeason(year)
        flag = False
    else:
        print('Invalid Option\n')
