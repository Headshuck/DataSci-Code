import requests 
import json
import collections 
import pprint as  pp

# This is a repository for commands I commonly execute 


def idList(competitionId): #List of team ids for a competition
	teamIds = {}
	z = getTeams(competitionId)
	for team in z['teams']:
		teamid = team['id']
		teamIds[team['name']] = teamid

	return teamIds


def getTeams(competitionId): # Given competition id, get teams in that competition
	teamList  =  requests.get('http://api.football-data.org/v1/competitions/' + str(competitionId) + '/teams',  headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})

	return teamList.json()


def getTeam( teamNumber ): # Given teamNumber, get team
	teamData = requests.get('http://api.football-data.org/v1/teams/' + str(teamNumber), headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})

	teamData = teamdata.json()

	return teamData

def getPlayers(teamNumber): # provied teamNumber, give me list of players 
	player_data = requests.get('http://api.football-data.org/v1/teams/' + str(teamNumber) + '/players/', headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})

	return player_data.json()['players']

# Here is an example of a player dictionary:
# {
# name: "Cristiano Ronaldo",
# position: "Left Wing",
# jerseyNumber: 7,
# dateOfBirth: "1985-02-05",
# nationality: "Portugal",
# contractUntil: "2018-06-30",
# marketValue: "110,000,000 \u20ac"
# }

def clubCountry(teamNumber): # Provided a teamNumer (which the API corresponds to a team), give me the country of that team.

	# I employ this to retireve the country from which a team originates
	# In reality, most clubs are largely constitued of players from club's country
	# This explots that to find the country of the club from player information
	# Manchester City being the exception. Lots of Argentinians on an English Club
	
	if teamNumber == 65: # Manchester City 
		return 'England'

	countries = []
	playerData = getPlayers(teamNumber) 
	if len(playerData) == 0:
		return 'Other Countries'

	for player in playerData:
		countries.append(player['nationality']) # Append each player's nationality into a country list
	
	counter = collections.Counter(countries)
	counter = counter.most_common()

	return counter[0][0] #most common country among players is club's country

def score(countryOne, countryTwo, scores, draw = None):	# This is for the CLscoreboard.py
	
	# This looks hazardous... I will improve upon this 
	
	if draw == True:

		try: 
			scores[countryOne][2] += 1  # It is a tie, so add one to the tie

		except: 
			scores[countryOne] = [0,0,1] # if the country hasn't been scored yet, add it with one draw

		try:
			scores[countryTwo][2] += 1

		except:
			scores[countryTwo] = [0,0,1]

		return scores

	try: 
		scores[countryOne][0] += 1 # Winning country -- add one to its wins

	except:
		scores[countryOne] = [1,0,0] 

	try:
		scores[countryTwo][1] += 1 # loser, add one to its loss count

	except:
		scores[countryTwo] = [0,1,0] 

	return scores



def giveList():

# I've copied most of what the clupdate.py algorithm searches for (country of team's league)
# This is becuase the API would throttle and crash the program when I exceeded 50 requests per minute.
# This is difficult to program around due to the sheer number of champions league teams, and 
# consequently, clubCountry API requests to retrieve the country of those teams.

# So I copied most of the results to this module to circumvent having to make so many API calls, thereby 
# expediting development.
# this is obviously not permanent. 

	list1 = {'AS Monaco FC': 'France',
	 'Arsenal FC': 'England',
	 'Bor. M\xf6nchengladbach': 'German',
	 'Borussia Dortmund': 'Germany',
	 'Celtic FC': 'Other Countries',
	 'Club Atl\xe9tico de Madrid': 'Spain',
	 'Club Brugge': 'Other Countries',
	 'Dynamo Kyiv': 'Ukraine',
	 'FC Barcelona': 'Spain',
	 'FC Basel': 'Switzerland',
	 'FC Bayern M\xfcnchen': 'Germany',
	 'FC Copenhagen': 'Other Countries',
	 'FC Rostov': 'Other Countries',
	 'GNK Dinamo Zagreb': 'Croatia',
	 'Juventus Turin': 'Italy',
	 'Legia Warszawa': 'Other Countries',
	 'Leicester City FC': 'England',
	 'Ludogorez Rasgrad': 'Bulgaria',
	 'Manchester City FC': 'England',
	 'Olympique Lyonnais': 'France',
	 'PSV Eindhoven': 'Netherlands',
	 'Paris Saint-Germain': 'France',
	 'Real Madrid CF': 'Spain',
	 'SSC Napoli': 'Italy',
	 'Sevilla FC': 'Spain',
	 'Sporting CP': 'Portugal',
	 'Tottenham Hotspur FC': 'England'}

 	return list1