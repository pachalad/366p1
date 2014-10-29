import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 10000
numStates = 182
numActions= 2
q = zeros((numStates, numActions))    

def randomPolicy(s):
    a=randint(0,1)
    return a
def randomShowOneGame():  
    y = 1
    alpha=1
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=randomPolicy(s);
        r,sp=blackjack.sample(s,a)
        print("turn %d: s %d a %d -> r %d sp %d "%(turn,s,a,r,sp),end="")
        print("\t Player Sum: %d  Dealer Card: %d  Usable Ace: %d"%(blackjack.playerSum,blackjack.dealerCard, blackjack.usableAce))
        turn+=1
        q[s,a]=q[s,a]+alpha*(r+y*max(q[sp, :])-q[s,a])
        s=sp
        G=G+r
    return G

q = zeros((numStates, numActions))    

def Policy(s):
    a=randint(0,1)
    return a
def ShowOneGame():  
    y = 1
    alpha=1
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=Policy(s);
        r,sp=blackjack.sample(s,a)
        blackjack.printPolicy(Policy)
        print("turn %d: s %d a %d -> r %d sp %d "%(turn,s,a,r,sp),end="")
        print("\t Player Sum: %d  Dealer Card: %d  Usable Ace: %d"%(blackjack.playerSum,blackjack.dealerCard, blackjack.usableAce))
        turn+=1
        q[s,a]=q[s,a]+alpha*(r+y*max(q[sp, :])-q[s,a])
        s=sp
        G=G+r
    return G

returnSum = 0.0
    
for episodeNum in range(numEpisodes):
    G=ShowOneGame()
    print("Episode: ", episodeNum, "Return: ", G)
    returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)