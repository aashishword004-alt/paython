'''Q- 2 Write a Python program to input n positive integers from the user and store them in a list. Perform the following tasks:
1.	Create a dictionary having each number as the key and its sum of digits as the value. 
2.	Create a tuple containing all the palindrome numbers from the given list. 
3.	Create a set containing all the unique digits occurring in the given numbers. 
4.	Find the number having the highest sum of digits. If more than one number has the same highest digit sum, display all such numbers. 
5.	Display all numbers which are both palindrome and divisible by the sum of their digits.
'''

# 1.	Create a dictionary having each number as the key and its sum of digits as the value.
'''
num = int(input('Enter the Number : '))
d = {}
for i in range(num):
 n = int(input('Enter the Value : '))
 temp = n 
 total = 0
 while n > 0:
  ia = n % 10
  total +=ia
  n = n // 10
 d[temp] = {total}

print(d)

'''
# 2.	Create a tuple containing all the palindrome numbers from the given list. 

# l1 = [123,153,154,151,161,717]
# l2 = []
# for i in l1:
#   newstr = str(i)
#   if newstr == newstr[::-1]:
#      l2.append(newstr)

# num = list(map(int,l2))

# pali = tuple(num)
# print(pali)

# 4.	Find the number having the highest sum of digits. If more than one number has the same highest digit sum, display all such numbers.
l = [12,13,789,699,123]
high = []
result = []
mx = 0
n = {}
for i in l:
    total = 0
    n = i
    while n > 0:
     digit = n % 10
     total+=digit
     n = n // 10 
    high.append(total)
    for k in high:
     if k > mx:
        mx = k
    if high == mx:
      result.append(i)


print(result)




# d = {}
# for i in l:
#     temp = i
#     total = 0
#     while i > 0:
#        digit = i % 10
#        total+=digit
#        i  = i // 10
#     d[temp] = {total}

# x = []
# for k,v in d.items():
#    for y in v:
#       x.append(y)

# count = {}
# for v in x:
#     count[v] = count.get(v,0) + 1


# print(count)
# dup = [n for n , c in count.items() if c > 1]
