class Node:
  def __init__(self,dataval = None):
    self.dataval = dataval
    self.nextval = None

class SublistSearch:
  def findList(self,first,second):
    ptr1 = first
    ptr2 = second
    if first is None and Second is None:
      return true
    if first is None or Second is None:
      return false
    while second.dataval is not None:
      ptr2.dataval = second.dataval
      while ptr1.dataval is not None:
        if ptr2.dataval is None:
          return false
        elif ptr2.dataval == ptr1.dataval:
          ptr1 = ptr1.next
          ptr2 = ptr2.next
        else:
          break;
      if ptr is None:
        return true
      ptr1 = first
      second = second.next
    return false
    
a = Node(1)
a.nextval = Node(2)
a.nextval.nextval = Node(3)
a.nextval.nextval.nextval = Node(4)

b = Node(1)
b.nextval = Node(2)
b.nextval.nextval = Node(1)
b.nextval.nextval.nextval = Node(2)
b.nextval.nextval.nextval.nextval = Node(3)
b.nextval.nextval.nextval.nextval.nextval = Node(4)

c = SublistSearch()
d = c.findList(a,b)
if d == true:
  print("Found")
else:
  print("Not Found")



          
    
