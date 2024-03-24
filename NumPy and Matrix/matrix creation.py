# matrix

class array:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        st= str(self.lst).replace(',','')
        return st
    
    def __add__(self, other):
        lst_sum = []
        if len(self.lst) == len(other.lst):
            for i in range(len(self.lst)):
                lst_sum.append(self.lst[i] + other.lst[i])
            return array(lst_sum)
        else:
            return "Length is not same !"
        
    def reshape(self, m, n):
        M = []
        tmp = []
        for i in self.lst:
            tmp.append(i)
            if len(tmp) == n:
                M.append(tmp)
                tmp = []
        return array(M)

arr1 = array([2, 4, 6, 8, 4, 5])
arr2 = array([4, 7, 9, 3, 5, 2])
out = arr1 + arr2
print(arr1.reshape(2,3))
print(out, type(out))