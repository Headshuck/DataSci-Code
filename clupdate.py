import json 
import pprint as pp
import requests
import collections, soccer 
from tabulate import tabulate

base = 'http://api.football-data.org'
add = '/v1/competitions/440/fixtures'
url = base + add
item = requests.get(url,  headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})
item = item.json()

scores = {}
tableData = [['Country (League)', 'Wins', 'Losses', 'Draws', 'Points Per Game']]

checkedTeams = soccer.giveList()
use = 0
#teamdata = requests.get('http://api.football-data.org/v1/competitions/440/teams', headers = { 'X-Auth-Token': '732c6cba888e45809a463888b61f0bb3', 'X-Response-Control': 'minified'})
#teamdata =teamdata.json()


#for team in teamdata['teams']:
	#country = soccer.clubCountry(team['id'])
def score(winningCountry, losingCountry, draw = None):	
	if draw == 1:

		try: 
			scores[winningCountry][2] += 1

		except:
			scores[winningCountry] = [0,0,1]

		try:
			scores[losingCountry][2] += 1

		except:
			scores[losingCountry] = [0,0,1]

		return None

	try: 
		scores[winningCountry][0] += 1

	except:
		scores[winningCountry] = [1,0,0]

	try:
		scores[losingCountry][1] += 1

	except:
		scores[losingCountry] = [0,1,0]

for i in item['fixtures']:
	if i['status'] == "FINISHED":
		winner = None
		loser = None
		homeGoals = i['result']['goalsHomeTeam']
		awayGoals = i['result']['goalsAwayTeam']
		countryone = None
		countrytwo = None

		if homeGoals > awayGoals:
			winner = 'home'
			loser = 'away'

		elif awayGoals > homeGoals:
			winner = 'away'
			loser = 'home'


		else: # TIE CASE
			countryone = soccer.clubCountry(i['awayTeamId'])
			countrytwo = soccer.clubCountry(i['homeTeamId'])
			use += 1 
			score(countryone, countrytwo, 1)
			#print i['awayTeamName'] + ' ' + str(awayGoals) + '|' + str(homeGoals) + ' '  +i['homeTeamName']


		try:
			#print i[winner + 'TeamId']
			if  i[winner + 'TeamName']  in checkedTeams:
				#print 'Good'&&*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				winningCountry = checkedTeams[i[winner + 'TeamName']]

			else:
				winningCountry = soccer.clubCountry(i[winner + 'TeamId'])
				use  +=  1
				checkedTeams[i[winner + 'TeamName']] = winningCountry

			if  i[loser + 'TeamName']  in checkedTeams:
				#print 'Good$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				losingCountry = checkedTeams[i[loser + 'TeamName']]

			else:
				losingCountry = soccer.clubCountry(i[loser + 'TeamId' ])
				use += 1 
				checkedTeams[i[loser + 'TeamName']] = losingCountry
			#print i[winner + 'TeamName'] + ' - ' + country
			score(winningCountry, losingCountry)
				

		except:
			print 'Error - ' + str(winner) #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

		#print (checkedTeams)
		#print 'USE: ' + str(use)

		
for country, record in scores.iteritems():
	points = float(record[0]*3 + record[2])
	games = float(sum(record[0:3]))
	record.append("%.2f" % (points/games))
	tableData.append([country, record[0], record[1], record[2], record[3]])	

print '          Champions League 2016/2017 Group Stage'
print tabulate(tableData)

#pp.pprint (scores)

#INJURY RATE 
#TYPES OF INJURY 
