import json 
import pprint as pp
import requests
import collections, soccer 
from tabulate import tabulate

# Champions League ScoreBoard
# Champions League is tourament consisting of the best teams(clubs) from various countries around the world.
# This is the single biggest intercountry club tourament in the world. 
# This tool groups CL teams by country (league essentially), and monitors performances of each country(league) in the tournament.
# Only teams in the country's best league are sent. i.e Premiere League from England, La Liga from Spain
# Henceforth, a country in the program really represents the best league from that country.
# Countries can send more than one team. The number of teams they send varys according to offical FIFA coefficent.

# Enjoy

base = 'http://api.football-data.org'
add = '/v1/competitions/440/fixtures'
url = base + add
item = requests.get(url,  headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})
item = item.json()


scores = {} # items are country records in the form .... 'country' : [Wins, Loses, Draws] 
tableData = [['Country (League)', 'Wins', 'Losses', 'Draws', 'Points Per Game']] # header for table
checkedTeams = soccer.giveList() #the soccer module contains a list of teams with their corresponding 
use = 0


for match in item['fixtures']:
	if match['status'] == "FINISHED":
		winner = None
		loser = None
		homeTeamGoals = match['result']['goalsHomeTeam']
		awayTeamGoals = match['result']['goalsAwayTeam']
		countryOne = None
		countryTwo = None

		if homeTeamGoals > awayTeamGoals:
			winner = 'home'
			loser = 'away'

		elif awayTeamGoals > homeTeamGoals:
			winner = 'away'
			loser = 'home'


		else: # TIE CASE
			countryOne = soccer.clubCountry(match['awayTeamId']) 
			countryTwo = soccer.clubCountry(match['homeTeamId'])
			use += 1 # to document API calls
			soccer.score(countryOne, countryTwo, scores, True)

		try: # Place-holder for now. I will find a more efficient way to do this
			winningTeamName = match[winner + 'TeamName']  # homeTeamName 
			losingTeamName = match[loser + 'TeamName']

			if  winningTeamName  in checkedTeams:  # We already have the team's country 
				winningCountry = checkedTeams[winningTeamName] 

			else:
				winningCountry = soccer.clubCountry(match[winner + 'TeamId']) # Else, retrieve the team country
				use  +=  1
				checkedTeams[winningTeamName] = winningCountry #Add team, country to checked teams

			if  losingTeamName  in checkedTeams:
				losingCountry = checkedTeams[losingTeamName]

			else:
				losingCountry = soccer.clubCountry(match[loser + 'TeamId' ])
				use += 1 
				checkedTeams[losingTeamName] = losingCountry

			scores = soccer.score(winningCountry, losingCountry, scores)
				

		except:
			print 'Error - ' + str(winner) # Just a checking mechanism 
		#print (checkedTeams) # checking.
		#print 'USE: ' + str(use)

		
for country, record in scores.iteritems():
	points = float(record[0]*3 + record[2])
	games = float(sum(record[0:3]))
	record.append("%.2f" % (points/games))
	tableData.append([country, record[0], record[1], record[2], record[3]])	

print '          Champions League 2016/2017 Group Stage'
print tabulate(tableData)

