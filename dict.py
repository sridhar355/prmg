
#dictionary comprehension

# ex 1
#square of number
res={i:i*i for i in range(1,11)}
print(res)

#ex2
#using if condition
num={'a':33,'b':12,'c':25,'d':6,'e':40}
res={key:val for (key,val) in num.items() if val>20}
print(res)

#using if-else
#ex3
res={key:'can vote' if val>18 else "can't" for (key,val) in num.items()}
print(res)

#ex4
#two lists to dictionary
even=[2,4,6,8,10]
odd=[1,3,5,7,9]
res={even[i]:odd[i] for i in range(len(even))}
print(res)










