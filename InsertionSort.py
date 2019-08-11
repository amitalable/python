class InsertionSort:
    def __init__(self,_array):
        self._array = _array
       
    def Sort(self):
        pos =1
        while pos<len(self._array):
            nextpos = pos
            #print(self._array)
            while(nextpos>0 and self._array[nextpos]<self._array[nextpos-1]):
                self.Swap(nextpos, nextpos-1)
                nextpos -=1
                #print("        ",self._array)
            pos+=1
        return self._array
            
    def Swap(self,_index1,_index2):
        _temp = self._array[_index1]
        self._array[_index1] = self._array[_index2]
        self._array[_index2] = _temp
        

print(InsertionSort([22,34,11,43,2,23]).Sort())
