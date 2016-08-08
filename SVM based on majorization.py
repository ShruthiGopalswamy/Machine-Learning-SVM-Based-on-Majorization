import numpy as np 
import random as r 
import math
from numpy import linalg as LA 

def lassoCalc(k,percentage): 
	X=np.random.randn(100,1) 
	for i in range(0,199): 
		x=np.random.randn(100,1)
		X=np.hstack((X,x)) 
	X=X/LA.norm(X)
	size=200 
	hz=int((percentage/100)*size) 
	value=int(200-hz) 
	theta=np.zeros((value,1)) 
	thetaMatrix=list() 
	thetarand=r.uniform(0.1,10) 
	for i in range(1,hz+1): 
		thetarand=r.uniform(0.1,10) 
		theta=np.vstack((theta,thetarand))
		
	y=np.dot(X,theta) 
	z=np.identity(200) 
	lamda=2
	thetaold=np.zeros((200,1)) 
	oldThetaDiff=0 
	while True:
		thetaCal=np.dot(np.mat((2*np.dot(X.T,X)+z)).I,(2*np.dot(X.T,y))) 
		ep=math.pow(10, -6) 
		for i in range(0,199):
			z[i][i]=1/(math.sqrt(thetaCal[i]*thetaCal[i]+ep)) 
		thetaDiff=np.amax(thetaCal-thetaold,0) 
		if thetaDiff-oldThetaDiff<math.pow(10, -6) :
			break 
		oldThetaDiff = thetaDiff
		
	errorSum=0 
	for i in range(0, 199):
		errorSum=errorSum+theta[i]*theta[i]-thetaCal[i]*thetaCal[i]

	errorSum=math.sqrt(errorSum) 
	print(repr(k) + " \t\t" + repr(errorSum))

percent=[10,30,50] 
for percentage in percent: 
	print("The observations for " + repr(percentage)+ "% sparsity :") 
	print("Trials\t\tError") 
	for k in range(1, 11):
		lassoCalc(k,percentage)