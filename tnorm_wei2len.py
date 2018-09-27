#Usage
#python3 get_length_matrix.py [input filename] [output filename]
#Input
#
#[input filename]: input weighted matrix csv filename
#[output filename]: output filename
#
#Output
#
#[output filename]: t-norm length matrix

import sys
import numpy as np
inf=np.inf

input_filename=sys.argv[1]
output_filename=sys.argv[2]

matrix=np.loadtxt(input_filename, delimiter=',')

matrix[matrix==0]=inf
matrix=matrix**(-1)
matrix-=1
matrix[matrix<0]=inf

np.savetxt(output_filename, matrix, delimiter=',')
