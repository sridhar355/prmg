str1=input()
visit = {} 
for i in str1: 
    if i in visit: 
        visit[i] += 1
    else: 
        visit[i] = 1
for i,j in visit.items():
    print(i,j,end="")