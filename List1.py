print("Enter the List: ")
l1=list(map(int,input().split()))
c=0
print(l1)
for i in l1:
    c+=1
print("The length of the list is : ",c)
print("Enter 3 element to append : ",end="")
n1,n2,n3=map(int,input().split())
l1[c:]=[n1,n2,n3]
c+=3
min=l1[0]
max=l1[0]
sum=0
for i in range(c):
    if min > l1[i]:
        min=l1[i]
    if max < l1[i]:
        max=l1[i]
    sum+=l1[i]
print("The length of the list is : ",c)
print("The max element in the list is : ",max)
print("The min element in the list is : ",min)
print("The total sum of the element is : ",sum)
print(l1)
print("Enter the index to be removed : ",end="")
index=int(input())
l1=[l1[i] for i in range(c) if i!=index]
c-=1
print("After removing by index : ",l1)
print("Enter the element to be removed : ",end="")
ele=int(input())
for i in range(c):
    if l1[i]==ele:
        index=i
l1=[l1[i] for i in range(c) if i!=index]
c-=1
print("After removing the element list is :",l1)
print("Enter the element and index to be inserted : ")
n1,index=map(int,input().split())
l2=[]
l2=[l1[i] for i in range(index,c)]
l1[index:]=[n1]
l1[index+1:]=l2
c+=1
print(l1)
n1=int(input("Enter Element to check the occurence : "))
d=0
for i in range(c):
    if l1[i]==n1:
        d+=1
print("The Element",n1,"occured",d,"times")