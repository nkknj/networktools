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

def shortest_path_length(lengthmat):
    n=lengthmat.shape[0]
    shortest_path_length=np.zeros((n, n))
    for i_start_node in range(n):
        i_length=np.zeros(n)+inf
        candidate=np.zeros(n)+inf
        candidate[i_start_node]=0
        
        while np.min(candidate)!=inf:
            i_length[np.argmin(candidate)]=np.min(candidate)

            candidate=i_length.reshape(n, 1)+lengthmat
            candidate=np.min(candidate, axis=0)
            candidate[i_length!=inf]=inf
        
        shortest_path_length[i_start_node]=i_length
        
    return shortest_path_length

def characteristic_path_length(lengthmat, glo=True):
    n=lengthmat.shape[0]
    shortest_path_length_mat=shortest_path_length(lengthmat)
    characteristic_path_length=np.sum(shortest_path_length_mat, axis=0)/(n-1)
    
    if glo==True:
        characteristic_path_length=np.mean(characteristic_path_length)
        
    return characteristic_path_length

def clustering_coefficient(weightedmat, glo=True):
    triangles=triangle(weightedmat)
    k=np.sum(wei2unwei(weightedmat), axis=0)
    k*=(k-1)
    k[k==0]=1
    clustering_coefficient=2*triangles/k
    
    if glo==True:
        return np.mean(clustering_coefficient)
    
    return clustering_coefficient

def wei2unwei(mat):
    n=mat.shape[0]
    adjacency=np.zeros((n, n))
    adjacency[mat>0]=1
    return adjacency    
    
def triangle(weightedmat):
    n=weightedmat.shape[0]
    triangles=np.zeros(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp=weightedmat[i, j]*weightedmat[j, k]*weightedmat[k, i]
                triangles[i]+=pow(temp, 1/3)
        
    
    triangles/=2
    return triangles
