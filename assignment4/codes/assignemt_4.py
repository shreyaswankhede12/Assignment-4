import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,53,1)#all cards in deck is given linear nos
a=np.random.randint(1,53,size=1)#generated a random card
b=np.random.randint(1,53,size=1)#generated another random card
arr=np.arange(1,53,13)#array of positions with aces marked
l=len(x)
k=len(arr)
if(a in arr and b in arr ):
    print("The practical probability is :",(k/l)*(k/l))
if((a in arr and b not in arr) or (a not in arr and b in arr)):
    print("The practical probability is :",(k/l)*((l-k)/l))
if(a not in arr and b not in arr):
    print("The practical probability is :",((l-k)/l)*((l-k)/l))

#theorotical probability
print("therotical probabilty for 2 aces is: ",(4/52)*(4/52))
print("therotical probabilty for 1 ace and 1 non ace is: ",(4/52)*(48/52))
print("therotical probabilty for 2 non aces is: ",(48/52)*(48/52))

x = [0,1,2]
y_1 = [0.9,0.99,1]
plt.stem(x,y_1,label = 'CDF',linefmt='blue',markerfmt='D')
y_2 = [0.9,0.09,0.01]
plt.stem(x,y_2,label = 'PMF',linefmt='red',markerfmt='D')
plt.ylabel('Probability')
plt.xlabel('Random Variable(X)')
plt.legend()
plt.show()
