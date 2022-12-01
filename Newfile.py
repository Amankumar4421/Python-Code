f=open("one.txt","r")
st1=f.read()
l1=st1.split()
d1={}
for i in l1:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
for i in d1:
    print(i,'occured',d1[i],'times')
