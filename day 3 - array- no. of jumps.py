l=[int(i)for i in input().split()]
count=0
j=1
n=0
while(n<len(l)):
    n=n+l[n]
    if(n!=len(l)-2):
        count=count+1
print(count)
