import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 10000


def showOneGame():
    G = 0
    s=blackjack.init()
    turn=0
    while s!=-1: #-1 is terminal
        a=randint(0,1)
        r,sp=blackjack.sample(s,a)
        print("turn %d: s %d a %d -> r %d sp %d "%(turn,s,a,r,sp),end="")
        print("\t Player Sum: %d  Dealer Card: %d  Usable Ace: %d"%(blackjack.playerSum,blackjack.dealerCard, blackjack.usableAce))
        turn+=1
        s=sp
        G=G+r
    return G


returnSum = 0.0
    
for episodeNum in range(numEpisodes):
    G=showOneGame()
    print("Episode: ", episodeNum, "Return: ", G)
    returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)

