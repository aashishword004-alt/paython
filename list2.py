# 10)
number = [1,2,3,4,5,6,7,8,9,10]

print(max(number))
print(min(number))

print('********************************************************')
# 11)
alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]

vow = ['A','I','O',',U','E']

count = 0
# vowel = [i for i in alp if i in vow]
 
for i in alp:
    if i in vow:
     count += 1
     print(count)

# 12) 

odd = [i for i in range(1,21) if i%2 != 0]
even = [i for i in range(1,21) if i%2 == 0]

# print(odd)
# print(even)

# list comprehension 

# 3)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

div = [i for i in numbers if i%2 == 0 and i%3 == 0 ]

# print(div)

# 4)

sub = [55,56,65,76,76]

mark = [i for i in sub if i > 60]

# print(mark)

# 5)

# n = int(input('Enter the number of Weather : '))

# prime = [i for i in range if i%n == 0]

# print(prime)

# 6) 
l1 = [10, 101, 2, 100, 405]

l3 = [i for i in l1 if len(str(i)) >= 3]

print(l3)
