i=int(input("enter the year:"))
if(i%4==0 and i%100!=0):
    print("leap year")
else:
    print("not a leap year")
    for n in range(i,i-4,-1):
        if(n%4==0 and n%100!=0):
            print("previous year",n)
      
