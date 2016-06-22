#!/usr/bin/python

import sys, getopt
import numpy as np
import os

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   #print 'Input file is "', inputfile
   #print np.mean(data) + ' ' + np.median(data) + ' ' + np.var(data) + ' ' + np.std(data) + ' ' + np.min(data) + ' ' + np.max(data)
   data = np.loadtxt(inputfile)
   print os.path.splitext(inputfile)[0], np.min(data), np.max(data), np.mean(data), np.median(data), np.var(data), np.std(data)
#   print data.mean(axis=0)
#   print data.median(axis=0)   
#   print data.var(axis=0)
#   print data.std(axis=0)



if __name__ == "__main__":
   main(sys.argv[1:])

