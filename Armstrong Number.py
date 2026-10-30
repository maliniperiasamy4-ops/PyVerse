n=int(input())
temp=n
digit=0
while n>0:
  n=n//10
  digit+=1
n=temp
sum=0 
while n>0:
  last=n%10
  sum=sum+last**digit
  n=n//10
if sum==temp:
  print("Armstrong")
else:
  print("Not Armstrong")
