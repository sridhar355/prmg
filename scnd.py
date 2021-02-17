from firstp import *


obj=ListDict()
str1=input()
lst1 = str1.split(",")
for i in range(len(lst1)):
	obj.addElementToList(lst1[i])
tup1=tuple(input().split(','))
tup2=tuple(input().split(','))
for i in range(len(tup1)):
	obj.addElementToDict(tup1[i],tup2[i])
obj.printObject()