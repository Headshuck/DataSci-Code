import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as linear  ## linalg is Linear Algebra 
from itertools import cycle
## K-means clustering by Tande Mungwa


def cluster(datapoints, clusterpoints): # datapoints,clusterpoints must set of equally-dimensioned coordinate pairs
	

	clusters = [] # below for requires pre-existent list
	# adjust = np.array([ ])

	#for i in range(len(clusterpoints)): # instantiates each cluster dictionary
		# clusters.append( {'clusterpoint' : clusterpoints[i], 'members': [] }  )

	adjust = []	


	clusterIndex = None; 
	color = [];
	for i in range(0,len(datapoints)):
		distanceMatrix = abs(clusterPoints - datapoints[i]) # subtract each data point from the cluster point array 
															# abs means all distances are positive - so min can be used later on

		if len(distanceMatrix[1].shape) == 0: # if distance matrix elements are numbers instead of vectors 
			clusterIndex = np.argmin(distanceMatrix) # cluster index = index of smallest distance integer 
		
		else: # data-points are two dimensional or higher -- ACCOUNT FOR 3d.. 4d.. and so on 

			multiDimDiff = np.sqrt(distanceMatrix[:,0]**2 + distanceMatrix[:,1]**2)
		
			# conceptualize points as a matrix with the column 0 being the x-axis and column 1 being the y-axis
			# different rows being different points altogether
			# this squares all of the first column rows, returning an array of integers, and


			clusterIndex = np.argmin(multiDimDiff) # Recall cluster is list, so the only way to
			# correspond the difference matrix to the cluster list is by index, so the 

		if clusterIndex == 0:
			color.append('r')

		elif clusterIndex == 1:
			color.append('b')

		elif clusterIndex == 2:
			color.append('g')
		
		elif clusterIndex ==3:
			color.append('c')



		adjust.append([clusterIndex, 1]) # each data point will add to the list of adjustments -- this is not python and not numpy fxn 



	print color
	adjust_new =  np.asarray(adjust) # turns adjust LIST into VERTICAL NUMPY ARRAY 
	color_new = np.asarray(color)

	return np.concatenate((datapoints,adjust_new), axis = 1) # returns a COPY of the datapoints with the adjustments concatenated




clusterPoints = np.array([[2,5], [1,1], [4,1],[7,7]])
dataPoints = np.array([[1,5], [3,4], [3,5], [1,2], [3,1], [4,5], [8,3], [9,1], [2,3] ])

final = cluster(dataPoints, clusterPoints)

print final ## PRINTPRINTPRINTPRINTPRINTPRINTPRINTPRINTPRINT

colors = ['r', 'r', 'r', 'b', 'g', 'r', 'c', 'g', 'r']

x_t = final[:,0]
y_t = final[:,1]
plt.scatter(x_t, y_t, c = colors)



	
	## print len(dat['members'])g
	## if len(dat['members']) < 2:
		## color = 'r'
	## else:
		## color = 'b'

plt.scatter(clusterPoints[:,0],clusterPoints[:,1], color = 'k')


plt.show()



### After finding the minimum index, you will have to add the color of that index the corresponding data point.
### The data point list should be of the form [x, y, cluster_number, color of cluster number] after exiting the cycle. 
### Upon graphing, you will use a color cycler with the color column as the cycle.



