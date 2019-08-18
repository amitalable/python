'''
Created on 19-Aug-2019

@author: Amit Ranjan

Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases.

Here are some examples of how your function should work.

  >>> expanding([1,3,7,2,9])
  True
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 9-2 = 7.

  >>> expanding([1,3,7,2,-3]) 
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 2-(-3) = 5, so not strictly increasing.

  >>> expanding([1,3,7,10])
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 10-7 = 3, so not (strictly) increasing.


'''
def expanding(_list):                   
    for i in range(len(_list)-2):
        if abs(_list[i] - _list[i+1]) >= abs(_list[i+1] - _list[i+2]):
            return False
    else:
        return True
print(expanding([1,3,7,2,9]))
