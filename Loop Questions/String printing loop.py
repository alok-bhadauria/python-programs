import time

x = input().lower()
ls = []
for i in x:
    ls.append(ord(i))

st = ""

for i in ls:
    for j in range(97, 123):
        print(st+chr(j))
        time.sleep(0.008)
        if i == j:
            st += chr(j)
            break
        elif i == 32:
            st += " "
            break
