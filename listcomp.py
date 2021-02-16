#list comprehension
#example1
#print square of numbers
b=[i*i for i in range(1,11)]
print(b)

#ex2
#print words greater than given length
word=['apple','orange','mango','papaya','grapes']
res=[a for a in word if len(a)>5]
print(res)

#ex3
#using if-else condition
res=[a if a!='papaya' else 'berry' for a in word]
print(res)

#ex4
#using nested list
nlst=[[1,2],[3,4],[5,6]]
res=[a for i in nlst for a in i]
print(res)




