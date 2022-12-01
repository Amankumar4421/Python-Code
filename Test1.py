n=int(input())
student={}
for i in range(n):
    name=input()
    marks={}
    keys=['ds','daa','python']
    for j in keys:
        m=float(input())
        marks[j]=m
    student[name]=marks
res=sorted(student.items(),key=lambda x:x[1]['ds'])
print(res)