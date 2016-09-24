import requests
from bs4 import BeautifulSoup

url = "http://www.espnfc.us/"

r = requests.get(url)


def leagueMatches(data):
	teamNameArray = []
	featuredMatches = []
	featuredMatchesScores = []
	scoreArray = []

	soup = BeautifulSoup(data, "html.parser")
	#scoreCompacts = soup.find_all("div", {"class": "score compact"})
	leagueSelection = soup.find("div", {'class': "scorebar-league selected"})
	for matches in leagueSelection.contents:
		#matchDetails = matches.contents[1]
		for scoreTeams in matches.find_all("div", {"class": "team-score"}):
			for scores in scoreTeams.contents:
				if scores.string != None:
					scoreArray.append(scores.string.strip())
				else:
					scoreArray.append("TBP")	
				scoreArray = [x for x in scoreArray if x != '']
		for teamName in matches.find_all("div", {"class": "team-name"}):
			for teams in teamName.contents:
				teamNameArray.append(teams.string.strip()) 
				teamNameArray = [x for x in teamNameArray if x != '']

	for i in range(0, len(teamNameArray) - 1, +2):
		gameOpponents = []
		gameOpponents.append(teamNameArray[i])
		gameOpponents.append(teamNameArray[i + 1])
		featuredMatches.append(gameOpponents)
	for j in range(0, len(scoreArray) - 1, +2):
		teamScores = []
		teamScores.append(scoreArray[j])
		teamScores.append(scoreArray[j+1])
		featuredMatchesScores.append(teamScores)
	return [featuredMatches, featuredMatchesScores]




