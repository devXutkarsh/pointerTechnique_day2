import numpy as np


arr= np.array([1,2,3,4,5,6,7,8,10,11,12,13,14,15])
w=4

maxx=0

for i in range(len(arr)-w):
  current=0
  for j in range(i+w-1):
    current +=arr[j]
    maxx= max(maxx,current)
 
print(maxx)