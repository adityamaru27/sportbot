import time
import webscraper_leagueInfo
from selenium import webdriver
from bs4 import BeautifulSoup

def findLeagues():
	soup = BeautifulSoup(driver.page_source, "html.parser")
	leagueNames = soup.find("div", {'class': "scorebar-league selected"})


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.espnfc.us/');
time.sleep(5) # Let the user actually see something!
dropdown = driver.find_element_by_xpath('//*[@id="scorebar-leagues"]/select/option[3]')
dropdown.click()
print(webscraper_leagueInfo.leagueMatches(driver.page_source))
time.sleep(5) # Let the user actually see something!
driver.quit()
