class A:
	def show(self):
		print("it is super class")
class B(A):
	def show(self):
		print("it overrides the super class method")
ob=B()
ob.show()
