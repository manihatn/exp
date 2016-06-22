# http://stackoverflow.com/questions/10640759/how-to-get-the-cumulative-distribution-function-with-numpy

import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys, getopt
import os

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'cdf.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'cdf.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg


   N = 100
   data = np.loadtxt(inputfile)
#Z  np.random.normal(size = N)
# mthod 1
   H,X1 = np.histogram( data, bins = 10, normed = True )
   dx = X1[1] - X1[0]
   F1 = np.cumsum(H)*dx
#mehod 2
   X2 = np.sort(data)
   F2 = np.array(range(N))/float(N)

   plt.xlabel('Latency (in ns)')
   plt.ylabel('CDF')
   plt.title('CDF Vs latency values for DAG')
   plt.grid(True)
   plt.plot(X1[1:], F1)
   pylab.savefig(outputfile)

#pylab.savefig('foo.png', bbox_inches='tight') # Use this to remove spaces around the corners
#plt.plot(X2, F2)
#plt.show()  # To show as a pop up 

if __name__ == "__main__":
   main(sys.argv[1:])

