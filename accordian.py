'''
Created on 19-Aug-2019

@author: Amit Ranjan
Write a function accordian(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements alternates between increasing strictly and decreasing strictly.

Here are some examples of how your function should work.

 
  >>> accordian([1,5,1])
  False
Explanation: Differences between adjacent elements are 5-1 = 4, 5-1 = 4, which are equal.

 
  >>> accordian([1,5,2,8,3])
  True
Explanation: Differences between adjacent elements are 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences decrease, increase and then decrease.

 
  >>> accordian([-2,1,5,2,8,3]) 
  True
Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences increase, decrease, increase and then decrease.

 
  >>> accordian([1,5,2,8,1])
  False
Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-1 = 7, so the differences increase, decrease, increase and then increase again.
'''
def accordian(_list):                  
    temp=[]
    for i in range(len(_list)-2):
        if abs(_list[i] - _list[i+1]) > abs(_list[i+1] - _list[i+2]):
                temp.append(1);
        elif abs(_list[i] - _list[i+1]) < abs(_list[i+1] - _list[i+2]):
            temp.append(0);
        else:
            temp.append(-1); 
    if -1 in temp:
        return False
    else:
        return all(m!=n for m,n in zip(temp,temp[1:]))
print(accordian([1,5,2,8,3]))

print(accordian([1,5,2,1,3]))
