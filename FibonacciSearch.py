'''
Created on 07-Aug-2019

@author: Amit Ranjan
'''
def FibonacciGenerator(n):
    if n == 0:
        return 0;
    elif n ==1:
        return 1;
    else:
        return FibonacciGenerator(n-1) + FibonacciGenerator(n-2);

def FibonacciSearch(arr,n):
    m =0;
    
    while(FibonacciGenerator(m)<len(arr)):
        m+=1;
    
    offset =-1;
    
    while(FibonacciGenerator(m)>1):
        i = min(offset+FibonacciGenerator(m-2),len(arr)-1)
        
        if(n>arr[i]):
            m-=1;
            offset= i;
        elif(n<arr[i]):
            m-=2;
        else:
            return i
        
    if(FibonacciGenerator(m-1) and arr[offset+i]==n):
        return offset+1
    return -1;

arr =[10,22,30,44,56,58,60,70,100,110,130]
x = 60
print(FibonacciSearch(arr,x))
