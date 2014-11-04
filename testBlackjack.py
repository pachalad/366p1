
import blackjack

counts=[0 for i in range(11)]
for i in range(1000000):
    counts[blackjack.card()]+=1
for i in range(11):
    print(i,counts[i]/1000000.)
