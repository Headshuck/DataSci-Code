from __future__ import unicode_literals
import pprint as pp 
import requests 
import soccer
import statistics
from babel import numbers
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker as tick
import matplotlib.ticker as plticker

# The point of this program is to assess the price trends of teams in a particular league.
# Provided the leauge(leaugeId), the tool calculates mean player price for each team. This is the green bar
# It also calculates, how much, on average, players less expensive than the mean cost, and those more expensive
# than the mean. These are what the thin blue lines indicate. 

# Still making tweaks


leagueId = 430

def leaguePrice(leagueId):
	teamDict = soccer.idList(leagueId) #  retrieves TeamName:TeamId list given leagueCode  
	teamNames = [] # team names will be appended to this 
	meanList = [] # upper and lower means will be appended as 2-D lists corresponding to team names 
	teamMeanPrices = [] #means for each team name is added here 

	for teamName, teamId in teamDict.iteritems(): #Team names are the key
		#teamId =  teamDict[teamName] #get id given teamName - I could do this better.
		squad = soccer.getPlayers(teamId) #get squad list given teamid
		prices = np.array([]) 

		for player in squad: 
			try:
				price = player['marketValue'].split(' ')[0].split(',') #remove unicode dollar symbol
				price = int(''.join(price)) # recombines array to form original number
				prices = np.append(prices, price) # appends team price to list o fprices

			except:
				pp.pprint (player['name'] + ': No price') # if marketValue is None, it doesn't have .split method

		if prices !=  []: # entire team with no marketvalue throws error, otherwise
			mean = statistics.mean(prices)	# calculate mean of all players prices

			lowerThanAverage = np.where(prices < mean)
			higherThanAverage = np.where(prices > mean)

			lowerMean = statistics.mean(-1*(prices[lowerThanAverage] - mean)) #mean of price differences above mean player price
			higherMean = statistics.mean(prices[higherThanAverage] - mean)  # the same of price differences above the mean
			#How expensive, on average, are players that cost above and below the mean. 

			footballClub = ['AFC','FC', 'CF'] # so 'Real Madrid CF' becomes 'Real Madrid', 
											  # 'FC Barcelona' becomes 'Barcelona' etc.
			for i in footballClub:
				try:
					teamName = teamName.split(i)
					teamName = ''.join(teamName)
				except: # Works for now. I  know to avoid in the future.
					pass

			teamNames.append(teamName)
			meanList.append([lowerMean,higherMean])
			teamMeanPrices.append(mean)
		else:
			print 'Problem' #  just a checking mechanism. Doesn't indicate actual problem.

	teamNames = np.array(teamNames)
	meanList = np.array(meanList)
	teamMeanPrices = np.array(teamMeanPrices)

	#DATA POINTS
	lowerMeans = meanList[:,0]
	upperMeans = meanList[:,1]
	asymmetryBars = [lowerMeans/1e6, upperMeans/1e6] # 1e6 to so I can express in millions.

	x = range(len(teamMeanPrices)) # placeholder for team names

	#PLOT
	fig = plt.figure()
	ax = plt.subplot(111)
	line2 = ax.bar(x, teamMeanPrices/ 1e6, color='g', tick_label = teamNames, align = 'center')
	ax.errorbar(x, teamMeanPrices/1e6, yerr=asymmetryBars, fmt='o')
	tick = plt.xticks(x, teamNames, rotation='vertical')
	ax.grid(True)
	loc = plticker.MultipleLocator(base=5.0)
	ax.yaxis.set_major_locator(loc)

	handle = line2, line2
	label = 'Average Price', # I'm not sure why but I need a comma here.
	pos = 'upper right'
	plt.figlegend(handle, label,pos)

	#X-Label
	plt.ylabel('\u20ac (Millions)', rotation = 'vertical')
	plt.show()


leaguePrice(leagueId)
