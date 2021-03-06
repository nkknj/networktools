#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
pi=np.pi

data=sys.argv[1]
data=np.loadtxt(data, delimiter=',')
n=data.shape[0]
theta=np.arange(0, 2*pi, 2*pi/n)
if n%2==0:
	theta+=pi/n

data=(data+data.T)/2

for i in range(n):
	data[i, i]=0

for i in range(n):
	plt.plot(np.sin(theta[i]), np.cos(theta[i]), marker='o', color=cm.Blues(np.sum(data, axis=1)[i]/np.max(np.max(data))))

maxlw=np.max(data)
T=np.linspace(0, 1, 21)
i=0
while i<n-1:
	j=i+1
	while j<n:
		p0=np.array([np.sin(theta[i]), np.cos(theta[i])])
		p2=np.array([np.sin(theta[j]), np.cos(theta[j])])
		x=p0[0]*(1-T)**2+p2[0]*T**2
		y=p0[1]*(1-T)**2+p2[1]*T**2
		plt.plot(x, y, 'b-', lw=data[i, j]/maxlw)
		j+=1
	i+=1

plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)

fig=plt.gcf()
fig.gca().set_aspect('equal')
plt.show()

