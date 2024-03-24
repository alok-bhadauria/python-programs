n = int(input("Enter no. of rows : "))

# Left forward triangle
for i in range(1, n+1):
    print(i*'*',end="\n")
    
# Left backward triangle
for i in range(n):
    print((n-i)*'*',end="\n")

# Right forward triangle
for i in range(n):
    print((n-i)*' ',i*'*',end="\n")

# Right backward triangle
for i in range(n+1):
    print(i*' ',(n-i)*'*',end="\n")


