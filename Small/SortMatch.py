
import random
import time
def partition(a,low,high):
    key,i,j=a[low],low,high
    while i<j:
        while i<j and a[j]>=key:
            j-=1
        a[i]=a[j]
        while i<j and a[i]<=key:
            i+=1
        a[j]=a[i]
    a[i]=key
    return i
        
    
def quicksort(a,low=0,high=None):
    if high==None:
        high=len(a)-1
    if low<high:
        povitkey=partition(a,low,high)
        quicksort(a,low,povitkey-1)
        quicksort(a,povitkey+1,high)
         
        
a=list(range(2000))
random.shuffle(a)

time1=time.time()

for i in range(len(a)-1):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            
time2=time.time()



print("buddlesort time is ",time2-time1)


time1=time.time()

random.shuffle(a)
quicksort(a,0,len(a)-1)

time2=time.time()

print("quicksort time is ",time2-time1)
