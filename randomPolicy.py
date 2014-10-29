import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 10000


def showOneGame():
    s=blackjack.init()
    moves=[0,1,0] 
    turn=0
    while s!=-1: #-1 is terminal
        a=moves[turn]
        r,sp=blackjack.sample(s,a)
        print("turn %d: s %d a %d -> r %d sp %d "%(turn,s,a,r,sp),end="")
        print("\t Player Sum: %d  Dealer Card: %d  Usable Ace: %d"%(blackjack.playerSum,blackjack.dealerCard, blackjack.usableAce))
        s=sp
        turn+=1
    return None


returnSum = 0.0
    
for episodeNum in range(numEpisodes):
    G = 0
    r = 0
    s=blackjack.init()
    R,sp=blackjack.sample(s,0)
    while s!=-1:
        a=randint(0,1)
        s=sp
        r=r+R
        R,sp=blackjack.sample(s,a)
       
    G=r
    print("Episode: ", episodeNum, "Return: ", G)
    returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)

