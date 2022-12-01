# list1 = {'Z':1, 'B':2, 'C':3, 'A':4,'A':0,'B':1}
# e=sorted(list1.items(),key=lambda x:x[1])
# print(str(e))
# n=2
# d=dict(input().split() for x in range(n))
# print(d)

# n=2
# d={}
# for i in range(n):
#     key,a,b,c=(input().split())
#     d[key]=[a]
#     d[key].append(b)
#     d[key].append(c)
# print(d)

p = ('e', 'a', 'u', 'o', 'i')
print(sorted(p))
print(sorted(p,reverse=True))
print(list(reversed(p)))
