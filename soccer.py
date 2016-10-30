import requests 
import json
import collections 
import pprint as  pp



def idList(competitionId):
	teamIds = {}
	z = getTeams(competitionId)
	for team in z['teams']:
		teamid = team['id']
		teamIds[team['name']] = teamid

	return teamIds


def getTeams(competitionId):
	teamList  =  requests.get('http://api.football-data.org/v1/competitions/' + str(competitionId) + '/teams',  headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})

	return teamList.json()


def getTeam( team_number ):
	teamData = requests.get('http://api.football-data.org/v1/teams/' + str(team_number), headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})

	teamData = teamdata.json()

	return teamData

def getPlayers(team_number):
	player_data = requests.get('http://api.football-data.org/v1/teams/' + str(team_number) + '/players/', headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})

	#player_data = player_data.json()

	return player_data.json()['players']

def clubCountry(team_number):
	if team_number == 65: # Manchester City 
		return 'England'
	countries = []
	player_data = getPlayers(team_number) 
	#player_data =player_data['players']
	if len(player_data) == 0:
		return 'Other Countries'
	for player in player_data:
		countries.append(player['nationality'])
	
	counter = collections.Counter(countries)
	counter = counter.most_common()

	return counter[0][0]


def giveList():

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