#Usage
#python3 matrix_Z2R.py [input filename] [output filename]
#
#Input
#[input filename]: csv file (correlation coefficient matrix converted Z-score by Fisher's method)
#[output filename]: output filename
#
#Output
#[output filename]: raw correlation coefficient matrix 

import sys
import numpy as np

filename=sys.argv[1]
output=sys.argv[2]

matrix=np.loadtxt(filename, delimiter=',')
matrix=(np.exp(2*matrix)-1)/(np.exp(2*matrix)+1)

np.savetxt(output, matrix, delimiter=',')
