#Usage
#python3 tnorm_len2wei.py [input filename] [output filename]
#
#Input
#[input filename]: length matrix csv file
#[output filename]: save weighted matrix as the argv

import sys
import numpy as np
import networktools

input_filename=sys.argv[1]
output_filename=sys.argv[2]

matrix=np.loadtxt(input_filename, delimiter=',')

matrix=networktools.shortest_path_length(matrix)
matrix=(matrix+1)**(-1)

for i in range(matrix.shape[0]):
	matrix[i, i]=0

np.savetxt(output_filename, matrix, delimiter=',')
