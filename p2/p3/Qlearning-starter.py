import mountaincar
from Tilecoder import numTilings, tilecode
from pylab import *
import datetime

numTilings=4
numTiles= 4*9*9
numRuns = 50
numEpisodes = 200
alpha = 0.05/numTilings
gamma = 1
lmbda = 0.9
epsilon = 0
n = numTiles * 3
zerovec = zeros(n)
F = [-1]*numTilings
Fprime=[-1]*numTilings
actions=[0,1,2]
runSum = 0.0
Q=[0,0,0]
A=-1
S=()
G=0
R=0
run=0
averages=[0]*200
def getMaxFeature(P,V,F,Q):
	F0 = [-1]*numTilings
	F1 = [-1]*numTilings
	F2 = [-1]*numTilings
	Fi=[F0,F1,F2]
	tilecode(P,V,F0)
	F1[0],F1[1],F1[2],F1[3]=F0[0]+numTiles,F0[1]+numTiles,F0[2]+numTiles,F0[3]+numTiles
	F2[0],F2[1],F2[2],F2[3]=F1[0]+numTiles,F1[1]+numTiles,F1[2]+numTiles,F1[3]+numTiles

	Q[0]=sum(w[F0])
	Q[1]=sum(w[F1])
	Q[2]=sum(w[F2])
	A=Q.index(max(Q))

	for i in range(4):
		F[i]=Fi[A][i]
	return A
def writeF():
	fout = open('value', 'w')
	F = [0]*numTilings
	steps = 50
	for i in range(steps):
		for j in range(steps):
			tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
			height = -1*max(w[F])
			fout.write(repr(height) + ' ')
		fout.write('\n')
	fout.close()
def writeAverages(filename,averages):
	savetxt(filename,averages)
for run in range(numRuns):
	w = randint(1,size=n)
	w=w*.01
	zerovec = zeros(n)
	returnSum = 0.0
	print(run)
	for episodeNum in range(numEpisodes):
		G=0
		R=0
		S=(0,0)
		P,V=mountaincar.init()
		while (S!=None):
			A=getMaxFeature(P,V,F,Q)
			R,S=mountaincar.sample((P,V),A)
			G=G+R
			var=R-Q[A]
			for i in F:
				zerovec[i]=1
			if (S==None):
				for i in range(n):
					if (zerovec[i]!=0):
						w[i]=w[i]+alpha*var*zerovec[i]
				continue
			P,V=S[0],S[1]
			A=getMaxFeature(P,V,Fprime,Q)
			var=var+Q[A]
			for i in range(n):
				if (zerovec[i]!=0):
					w[i]=w[i]+alpha*var*zerovec[i]
					zerovec[i]= lmbda*zerovec[i]
		averages[episodeNum]=averages[episodeNum]+G		    
		print("Episode: ", episodeNum, "Return: ", G)
		returnSum = returnSum + G
	print("Average return:", returnSum/numEpisodes)
	runSum += returnSum
print("Overall average return:", runSum/numRuns/numEpisodes)
for i in range(50):
	averages[i]=averages[i]/50
writeAverages("ave",averages)


