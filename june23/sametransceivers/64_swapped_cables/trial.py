# http://stackoverflow.com/questions/10640759/how-to-get-the-cumulative-distribution-function-with-numpy

import numpy as np
import matplotlib.pyplot as plt
import pylab

N = 100
data = np.loadtxt('64_general.out')
#Z = np.random.normal(size = N)
# method 1
H,X1 = np.histogram( data, bins = 10, normed = True )
dx = X1[1] - X1[0]
F1 = np.cumsum(H)*dx
#method 2
X2 = np.sort(data)
F2 = np.array(range(N))/float(N)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')

plt.plot(X1[1:], F1)
pylab.savefig('foo.png')

#pylab.savefig('foo.png', bbox_inches='tight') # Use this to remove spaces around the corners
#plt.plot(X2, F2)
#plt.show()  # To show as a pop up 

