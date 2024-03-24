n = int(input())
x = input()

for i in range(0, n+1):
    print((n-i)*' ',i*x, sep="", end="\n")

for i in range(0, n+1):
    print(n*' ', end="")
    print((n-i)*x ,end="\n")

print('-'*(2*n))

for i in range(0, n+1):
    print(n*' ', end="")
    print((n-i)*' ',i*x, sep="", end="\n")

for i in range(0, n+1):
    print((n-i)*x ,end="\n")
    