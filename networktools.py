#!/usr/bin/python3

import os, sys
import numpy as np

def mat2list(mat):
	output=np.zeros((1, 3))

	#whether it's directed or undirected
	temp=mat.copy()
	directed=True
	if np.sum(temp==temp.T)==(temp.shape[0]*temp.shape[1]):
		#undirected
		directed=False

	for i in range(temp.shape[0]):
		temp[i, i]=0

	if np.sum(temp*temp.T)==0:
		undirected=False


	#convertion
	if directed:
		i=0
		while i<mat.shape[0]:
			j=0
			while j<mat.shape[1]:
				if mat[i, j]!=0:
					output=np.r_[output, np.array([i, j, mat[i, j]]).reshape(1, 3)]
				j+=1
			i+=1
	else:
		i=0
		while i<mat.shape[0]:
			j=i
			while j<mat.shape[1]:
				if mat[i, j]!=0:
					output=np.r_[output, np.array([i, j, mat[i, j]]).reshape(1, 3)]
				j+=1
			i+=1

	output=output[1:]	#delete first row coming from np.zeros((1, 3))
	return output

def list2mat(list, n, directed=True):
	output=np.zeros((n, n))

	for i in range(list.shape[0]):
		output[list[i, 0], list[i, 1]]=list[i, 2]

	output=output+output.T
	return output

