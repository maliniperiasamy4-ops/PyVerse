n=int(input())
evensum=0
while n>0:
  last=n%10
  if last%2==0:
    evensum+=last
  n=n//10
print(evensum)    
  
  
