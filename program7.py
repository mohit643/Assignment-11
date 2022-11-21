# Write a python script to count digits in a given number


a=int(input("enter a no "))
count=0
while a>0:
  count+=1
  a=a//10
print(count)  

