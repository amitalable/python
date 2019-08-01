class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None
class SublistSearch:
    def findList(self,first,second):
        ptr1 = first
        ptr2 = second
        if first is None and second is None:
            return True
        if first is None or (first is not None and second is None):
            return False
        while second is not None:
            ptr2 = second
            while ptr1 is not None:
                if ptr2 is None:
                    return False
                elif (ptr1.dataval == ptr2.dataval):
                    ptr1 = ptr1.nextval
                    ptr2 = ptr2.nextval
                else:
                    break
            if ptr1 is None:
                return True
            ptr1 = first
            second = second.nextval
        return False
        
    
        
a = Node(1)
a.nextval = Node(2)
a.nextval.nextval = Node(3)
a.nextval.nextval.nextval = Node(5)

b = Node(1)
b.nextval = Node(2)
b.nextval.nextval = Node(1)
b.nextval.nextval.nextval = Node(2)
b.nextval.nextval.nextval.nextval = Node(3)
b.nextval.nextval.nextval.nextval.nextval = Node(4)


if SublistSearch().findList(a,b) == True:
  print("Found")
else:
  print("Not Found")
