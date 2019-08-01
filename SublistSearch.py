class Node:
  def __init__(self,dataval = None):
    self.dataval = dataval
    self.nextval = None
class SublistSearch:
  def findList(self,first,second):
    ptr1 = first
    ptr2 = second
    #Printing first list
    while ptr1 is not None:
        print(ptr1.dataval,end=" ")
        ptr1 = ptr1.nextval
    print()
    #Printing second list
    while ptr2 is not None:
        print(ptr2.dataval,end =" ")
        ptr2 = ptr2.nextval
    print()
    
    if first is None and second is None:
        return True
    if first is None or second is None:
        return False
      
    while second is not None:
        ptr2 = second
        while ptr1 is not None:
            if ptr2 is None:
                return False
            elif ptr1.dataval == ptr2.dataval:
                ptr1 = ptr1.nextval
                ptr2 = ptr2.nextval
            else:
                break;
        if ptr1 is None:
            return True
        ptr1 = first
        second = second.nextval
    return False
    
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
if d == True:
  print("Found")
else:
  print("Not Found")
