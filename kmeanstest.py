import clusternew
import numpy as np
import matplotlib.pyplot as plt

clusterPoints = np.array([[2,5], [1,1], [4,1],[7,7]])  # initial guess for cluster centers.... length equals K 
													   # These will evolve over time.
dataPoints = np.array([[1,5], [3,4], [3,5], [1,2], [3,1], [4,5], [8,3], [9,1], [2,3]])

final = clusternew.cluster(dataPoints, clusterPoints)

#print final --- just a check

x_t = final[:,0] # this can probably be done better
y_t = final[:,1]
color = final[:,3]


plt.scatter(x_t, y_t, c = color, marker = 'D')

plt.scatter(clusterPoints[:,0],clusterPoints[:,1], color = 'y') # clusters centers are yellow


plt.show()





