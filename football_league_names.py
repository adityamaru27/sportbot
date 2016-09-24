import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
url = "http://www.espnfc.us/"

r = requests.get(url)
data = r.text

def f(data):
	leagueArray = []
	soup = BeautifulSoup(data, "html.parser")
	leagueNames = soup.find("select", {'class' : 'dropdown-select'})
	for x in leagueNames:
		leagueArray.append(x.string)
		leagueArray = [y for y in leagueArray if y != '' and y != '\n']
	print(leagueArray)

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.espnfc.us/');
time.sleep(5) # Let the user actually see something!
# dropdown = driver.find_element_by_xpath('//*[@id="scorebar-leagues"]/select/option[3]')
# dropdown.click()
f(driver.page_source)
time.sleep(5) # Let the user actually see something!
driver.quit()
	


