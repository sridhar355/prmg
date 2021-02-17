class ListDict:
	
	def __init__(self):
		self.lst=list()
		self.dict=dict()
		pass
	
	def addElementToList(self,a):
		
		self.lst.append(a)
	def addElementToDict(self,b,c):
		
		self.dict[b]=c
	def printObject(self):
		print("list",self.lst)
		print("dictionary",self.dict)