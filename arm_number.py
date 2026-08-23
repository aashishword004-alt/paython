n = int(input("Enter the Number : "))
num = n

length = len(str(n))
arm_number = 0

while num > 0:
   digit = num % 10
   arm_number += digit ** length
   num =  num // 10

print(arm_number)

if arm_number == n:
  print( n ,' is armstong number ')
else:
   print( n ,'is not armstrong number')