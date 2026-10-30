n=int(input())
product=1 
while n>0:
  last=n%10
  product*=last
  n=n//10
print(product)  
