class C1:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def add(self):
        print(self.a+self.b)
    def add(self):
        print(self.a+self.b+self.c)
    # def add(self,a=None,b=None,c=None):
    #     if(a!=None and b!=None and c!=None):
    #         print(a+b+c)
    #     elif(a!=None and b!=None):
    #         print(a+b)
ob=C1(1,2,3)
ob.add()
ob.add()

