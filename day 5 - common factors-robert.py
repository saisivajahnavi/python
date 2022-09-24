s=int(input())
a=int(input())
b=max(s,a)
c=0
for i in range(1,b):
    if(a%i==0 and s%i==0):
        c+=1
print(c)
