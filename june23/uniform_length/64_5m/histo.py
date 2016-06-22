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
      print 'histo.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'histo.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg


   N = 100
   data = np.loadtxt(inputfile)
#Z  np.random.normal(size = N)
# mthod 1


   plt.xlabel('Latency (in ns)')
   plt.ylabel('Frequency')
   plt.title('Frequency Vs latency values for DAG')
   plt.grid(True)
   plt.hist(data)
   pylab.savefig(outputfile)

#pylab.savefig('foo.png', bbox_inches='tight') # Use this to remove spaces around the corners
#plt.plot(X2, F2)
#plt.show()  # To show as a pop up 

if __name__ == "__main__":
   main(sys.argv[1:])

