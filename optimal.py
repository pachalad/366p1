import blackjack

from numpy import *
from random import *
from scipy import *
from sys import *
numEpisodes = 1000000
numStates = 182
numActions= 2
q = zeros((numStates, numActions))   




def Policy(s):
    epsilon=.1
    b=randint(0,100)/100
    if (b<epsilon):
        a=randint(0,1)
    else:
        a=argmax(q[s, :])
    return a
def ShowOneGame(i,j):  
    y = j/100
    alpha=i/100
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=Policy(s);
        r,sp=blackjack.sample(s,a)
        turn+=1
        q[s,a]=q[s,a]+alpha*(r+y*max(q[sp, :])-q[s,a])
        s=sp
        G=G+r
    return G

returnSum = 0.0
bestAlpha=0
bestY=0
runningSum=-100
for i in range(50,100,5):
    for j in range(0,50,5):
        returnSum = 0.0
        time=datetime.time
        q = zeros((numStates, numActions))   
        for episodeNum in range(numEpisodes):
            G=ShowOneGame(i,j)
            returnSum = returnSum + G
            if (returnSum/numEpisodes)>runningSum:
                runningSum=returnSum/numEpisodes
                bestAlpha=i
                bestY=j
        print(datetime.time-time)
print("Best Alpha ",bestAlpha/100,"best y ",bestY/100,"Running sum",runningSum)