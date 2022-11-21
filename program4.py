# Write a python script to calculate sum of first N odd natural numbers

sum=0
for a in range(2*int(input("enter a no "))+1):
  if a%2!=0:
    sum+=a
print(sum)    