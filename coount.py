
str1 =input()
opstr=""
dup=[]
strlst=(list(str1))
n=len(strlst)
visit=[]
for i in range(n):
    visit.append(0)
for j in range(n):
    count=0
    for k in range(j,n):
        if ((visit[k]==0)and(strlst[j]==strlst[k])):
            if strlst[j] not in dup:
                dup.append(strlst[j])
                opstr=opstr+strlst[j]
            visit[k]=1 
            count=count+1
    if(count>0):
        opstr=opstr+str(count)
#cmnt
print(opstr)
