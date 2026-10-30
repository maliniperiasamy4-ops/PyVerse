#Length of a string
n=input()
print(len(n))

#Join the strings
a=input()
b=input()
print(a+" "+b)

#Compare the Strings
a=input()
b=input()
if a==b:
  print("true")
else:
  print("false")

#First character of a string
n=input()
print(n[0])

#Last character of a string
a=input()
print(a[-1])

#Join first & last characters of a string
n=input()
print(n[0]+n[-1])

#Alphanumeric strings
s=input()
alphacount=numcount=0
for i in s:
  if i.isalpha():
    alphacount=True
  elif i.isdigit():
    numcount=True
if alphacount and numcount:
  print("true")
else:
  print("false")

#Uppercase check
n=input()
if n.isupper():
  print("true")
else:
  print("false")

#Lowercase check
n=input()
if n.islower():
  print("true")
else:
  print("false")

#String lengths equal or not
a=input()
b=input()
if len(a)==len(b):
  print("true")
else:
  print("false")

#Reverse a string
n=input()
print(n[::-1])

#Split strings by comma
n=input()
for i in n.split(","):
  print(i)

#Remove vowels
n=input()
vol="aeiouAEIOU"
for i in n:
  if i in vol:
    n=n.replace(i,"")
print(n)   

#Reverse the character case
n=input()
print(n.swapcase())

#Print ascii value
n=input()
print(ord(n))

#Remove occurrences of a char
n=input()
s=input()
for i in n:
  if i in s:
    n=n.replace(i,"")
print(n)    
    
#Search for a word
n=input()
b=input()
if b in n:
  print("true")
else:
  print("false")

#Count vowels and consonants
n=input()
vow="aeiouAEIOU"
vowcount=con=0
for i in n:
  if i in vow:
    vowcount+=1 
  else:
    con+=1 
print(vowcount)
print(con)
    
#Anagram check
a=input().lower().replace(" ","")
b=input().lower().replace(" ","")
if len(a)!=len(b):
  print()
if sorted(a)==sorted(b):
  print("true")
else:
  print("false")

#Palindrome check
n=input()
if n==n[::-1]:
  print("true")
else:
  print("false")


    

