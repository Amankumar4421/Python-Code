l=[1,2,3,4]
j=0
n=4
c=0
print(l)
l2=[l[i] for i in range(j,n)]
l[j:]=[8]
l[j+1:]=l2
n+=1
print(l)
l=[l[i] for i in range(0,n) if i!=2]
c=0
print(l)
for i in l[::-1]:
    l[c:]=[i]
    c+=1

l=[l[i] for i in range(0,c) if l[i]!=1]
print(l)
l=l[::-1]
print(l)
c=len(l)
for i in range(int(c/2)):
    temp=l[c-i-1]
    l[c-i-1]=l[i]
    l[i]=temp
print(l)