#prime or not

n=int(input())
count=0
for i in range(2,n):
    if(n%i==0):
        count+=1
    
    if(count==1):
        print(n," is a Prime number")
    else:
        print(n," is not a Prime number")        