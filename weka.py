n=4
l=[]
count = 0
for i in range(n):
    l.append([])
    for j in range(n):
            l[i].append(count)
            count+=1
print(l)
# print(sum([l[len(l)-i-1][len(l)-i-1] for i in range(len(l))]))
l=[l[i][::-1] if i%2!=0 else l[i] for i in range(n)]
print(l)
for i in l:
    print(''.join(str(j) + ' ' for j in i))