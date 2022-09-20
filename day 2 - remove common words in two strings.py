a=input().split()
b=input().split()
l=a+b
for i in l:
    if((i not in a) or (i not in b)):
        print(i," ",end=' ')
