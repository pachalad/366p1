import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 10000
numStates = 182
numActions= 2
q = zeros((numStates, numActions))    
 
#Question 2
def teachPolicy(s):
    epsilon=.1
    b=randint(0,100)/100
    if (b<epsilon):
        a=randint(0,1)
    else:
        a=argmax(q[s, :])
    return a
def teach():  
    y = 1
    alpha=.001
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=teachPolicy(s);
        r,sp=blackjack.sample(s,a)
        turn+=1
        q[s,a]=q[s,a]+alpha*(r+y*max(q[sp, :])-q[s,a])
        s=sp
        G=G+r
    return G

returnSum = 0.0

def Policy(s):
 return argmax(q[s,:])
def postteaching():  
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=Policy(s);
        r,sp=blackjack.sample(s,a)
        turn+=1
        s=sp
        G=G+r
    return G
for episodeNum in range(numEpisodes):
    teach()
for episodeNum in range(numEpisodes):
    G=postteaching()
    returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)
blackjack.printPolicy(Policy)

#Question3

numEpisodes = 500000
numStates = 182
numActions= 2
q = zeros((numStates, numActions))  
def teachPolicy1(i,s):
    epsilon=i/100
    b=randint(0,100)/100
    if (b<epsilon):
        a=randint(0,1)
        print("explore",epsilon)
    else:
        a=argmax(q[s, :])
    return a
def teach1(i,j):  
    alpha=j/100
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=teachPolicy1(i,s);
        r,sp=blackjack.sample(s,a)
        turn+=1
        q[s,a]=q[s,a]+alpha*(r+max(q[sp, :])-q[s,a])
        s=sp
        G=G+r
    return G

returnSum = 0.0

def Policy1(s):
 return argmax(q[s,:])
def postteaching1():  
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=Policy1(s);
        r,sp=blackjack.sample(s,a)
        turn+=1
        s=sp
        G=G+r
    return G
bestepsion=0
bestalpha=0
runningbest=-100
for i in range(0,100,5):
    for j in range(0,100,5):
        q = zeros((numStates, numActions))
        returnSum=0
        for episodeNum in range(numEpisodes):
            teach1(i,j)
        for episodeNum in range(numEpisodes):
            G=postteaching1()
            returnSum = returnSum + G
        print("Running,",i,j,returnSum/numEpisodes)
        if (returnSum/numEpisodes)>runningbest:
            runningbest=returnSum/numEpisodes
            bestepsion=i/100
            bestalpha=j/100
        print(i,j)
print(bestepsion,bestalpha,runningbest)
blackjack.printPolicy(Policy1)
