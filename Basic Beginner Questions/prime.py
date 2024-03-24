def Prime(num):
    return (("Prime" if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1 else "Not Prime"))

# main code
n = int(input())
re = Prime(n)
print(re)