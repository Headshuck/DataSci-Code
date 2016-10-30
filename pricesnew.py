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


teamDict = soccer.idList('430') #  retrieves TeamName:TeamId list given leagueCode 

teamNames = [] # team names will be appended to this 
priceStdDev = [] # upper and lower stdDeviations will be appended as 2-D lists corresponding to team names 
priceMean = [] #means for each team name is added here 

for teamName in teamDict: 
	teamId =  teamDict[teamName] #get id given teamName
	squad = soccer.getPlayers(teamId) #get squadlist given teamid
	prices = np.array([]) # instantiate price array

	for player in squad: 
		try:
			price = player['marketValue'].split(' ')[0].split(',') #remove unicode dollar symbol
			price = int(''.join(price)) # rejoins array to form original number
			prices = np.append(prices, price) # appends to price to the team prices

		except:
			pp.pprint (player['name'] + ': No price') # if marketValue is None, it doesn't have .split method

	if prices !=  []: # entire team with no marketvalue throws error, otherwise
		mean = statistics.mean(prices)	# calculate mean of all players prices

		lowerThanAverage = np.where(prices < mean)
		higherThanAverage = np.where(prices > mean)

		lowerMean = statistics.mean(-1*(prices[lowerThanAverage] - mean)) #mean of lower price differences
		higherMean = statistics.mean(prices[higherThanAverage] - mean)  #....... higher price differences

		extra = ['AFC','FC', 'CF']
		for i in extra:
			try:
				teamName = teamName.split(i)
				teamName = ''.join(teamName)
			except:
				pass

		teamNames.append(teamName)
		priceStdDev.append([lowerMean,higherMean])
		priceMean.append(mean)
	else:
		print 'prob'

teamNames = np.array(teamNames)
priceStdDev = np.array(priceStdDev)
priceMean = np.array(priceMean)



#DATA POINTS
lowerError = priceStdDev[:,0]
upperError = priceStdDev[:,1]
assymError = [lowerError/1e6, upperError/1e6]

#negStd = priceStdDev[:,0]
#posStd = priceStdDev[:,1]
#x = range(len(posStd))
x = range(len(priceMean))


#PLOT
fig = plt.figure()
ax = plt.subplot(111)
#line1 = ax.barh(x, -1* negStd / 1e6, color='r', tick_label = playerNames, align = 'center')
line2 = ax.bar(x, priceMean / 1e6, color='g', tick_label = teamNames, align = 'center')
ax.errorbar(x, priceMean/1e6, yerr=assymError, fmt='o')
tick = plt.xticks(x, teamNames, rotation='vertical')
ax.grid(True)
loc = plticker.MultipleLocator(base=5.0)
ax.yaxis.set_major_locator(loc)

#Legend 
#handles = (line1, line2)
handle = line2, line2
label = 'Average Price',
pos = 'upper right'
plt.figlegend(handle, label,pos)

#X-Label
plt.ylabel('\u20ac (Millions)', rotation = 'vertical')

plt.show()



