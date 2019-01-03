from math import log10
from random import randint
N = int(input("Enter no of observations : ")) #Number of Observations
l = [ randint(1,1000) for var in range(N) ] #Discrete Data or Ungroup data
print(l) # L = min(l) U = max(l)
l.sort()
print(l) #orderd data
k1 = 1
while 2 ** k1 < N :
   
    k1 += 1

k2 = 1 + (3.322*log10(N))
k2 = round(k2)


print("Method 1 class interval = ",k1)
print("Method 2 class intervar Sturge's rule = ",k2)

L = l[0]
U = l[-1]
R = U - L
NCI = k2

size = round(R / NCI)
print("Size of class Interval = ",size)
