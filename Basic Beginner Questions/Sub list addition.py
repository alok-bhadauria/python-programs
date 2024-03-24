ls = eval(input())

sub_ls = []

for i in ls:
    a = [i]
    sub_ls.append(a)

for i in range(1,len(ls)):
    a = [ls[i-1],ls[i]]
    sub_ls.append(a)
    
sub_ls.append(ls)

sum = 0

for i in sub_ls:
    for j in i:
        sum += j
print(sum)