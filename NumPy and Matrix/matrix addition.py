class array:
    def __init__(self, lst):
        self.lst = lst
    
    def reshape(self, m, n):
        M = []
        tmp = []
        for i in self.lst:
            tmp.append(i)
            if len(tmp) == n:
                M.append(tmp)
                tmp = []
        self.lst = M
    
    def __add__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0] * c] * r))
        for i in range(r):
            for j in range(c):
                M[i][j] = self.lst[i][j] + other.lst[i][j]
        
    def __subtract__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0] * c] * r))
        for i in range(r):
            for j in range(c):
                M[i][j] = self.lst[i][j] - other.lst[i][j]
        return array(M)

    def __subtract__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0] * c] * r))
        for i in range(r):
            for j in range(c):
                M[i][j] = self.lst[i][j] - other.lst[i][j]
        return array(M)

    def dot(self, other):
        r1 = len(self.lst)
        c1 = len(self.lst[0])
        r2 = len(other.lst)
        c2 = len(other.lst[0])

        M = eval(str([[0] * c2] * r1))
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    M[i][j] += self.lst[i][k] * other.lst[k][j]
        return array(M)

    def disp_matrix(self):
        for i in self.lst:
            print(*i)

# raw array
lst1 = list(map(int, input().split()))
r1, c1 = map(int, input().split())
arr1 = array(lst1)
arr1.reshape(r1, c1)

lst2 = list(map(int, input().split()))
r2, c2 = map(int, input().split())
arr2 = array(lst2)
arr2.reshape(r2,c2)

addition = arr1 + arr2