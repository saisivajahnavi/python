d={1:" ",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"," ":" "}
get=int(input())
get2=int(input())
for i in range(1):
    if((get2 in d)):
        s=d[get2]
for i in range(1):
    if((get in d)):
        v=d[get]
l=[]
for i in range(0,len(v),1):
    for j in range(0,len(s),1):
        l.append(v[i]+s[j])
print(l)
