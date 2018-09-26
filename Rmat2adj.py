#Usage
#python3 Rmat2adj.py [input filename] [output filename] [number of sample] [significance level]
#
#Input
#[input filename]: Input csv filename (correlation coefficient matrix)
#[output filename]: Output csv filename
#[number of sample]: Number of samples to calculate each correlation coefficient
#[significance level]: significance level (usually 0.05)
#
#Output
#[output filename]: adjacency matrix filled with 0 or 1

import sys
import numpy as np
import scipy.stats

filename=sys.argv[1]
output_filename=sys.argv[2]
n_sample=np.int(sys.argv[3])
alpha=np.float(sys.argv[4])

#load inputfile
matrix=np.loadtxt(filename, delimiter=',')
matrix[np.isnan(matrix)]=0

#prepare outputfile
output=np.zeros(matrix.shape)

#get T-value matrix by correlation coefficient matrix
Tmat=np.abs(matrix)*pow(n_sample-2, 1/2)/((1-matrix**2)**(1/2))

#get T threshold for significance
T_sig=-1*scipy.stats.t.ppf(q=[alpha/2], df=n_sample-2)

#compare T-value matrix and the threshold
output[Tmat>T_sig]=1

#Output
np.savetxt(output_filename, output, delimiter=',')
