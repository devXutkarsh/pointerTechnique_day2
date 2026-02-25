
import numpy as np

arr= np.array([1,2,3,4,5,6,7,8,10,11,12,13,14,15])
target_val=3
Sum=0
count=0


for i in range(len(arr)):
  count +=1
  for j in range(i+1, len(arr)):
   
   Sum=arr[i]+ arr[j]
   if(Sum==target_val):
     print("the no is this", arr[i], arr[j])
print(count)
     


