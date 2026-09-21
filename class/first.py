'''Q-1 Write a Python program to input a string and a number from the user. Perform the following tasks:
2.	Display all the words from the string that are palindromes. 
3.	Check whether the given number is an Armstrong number or not.
4.	Reverse the given number and display the sum of its digits.
'''
#1.	Count and display the number of vowels, consonants and digits present in the string. 
user = input("Enter the input : ")

cout = 0
vowel = ['a','i','o','u','e']
num = []
consonats = []
is_vowel = []
for char in user:
    if char in vowel:
        is_vowel.append(char)
        cout+=1
    elif char.isdigit():
        num.append(char)
    elif char not in vowel:
        consonats.append(char)

print(is_vowel,cout)
print(num)
print(consonats) 
# 2.	Display all the words from the string that are palindromes. 
string = str(input('Enter the input  :'))
palind = False
if string == string[::-1]:
        palind = True

if palind == False:
    print(string , 'is not palindromes')
else:
    print(string,'is palindromes') 
    
# 3.	Check whether the given number is an Armstrong number or not.
n = int(input('Enter The input : '))
temp = n 
length = len(str(n))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** length
    temp = temp // 10

if n == total:
    print(n ,' is armstrong number ') 
else:
     print(n ,' is not armstrong number ') 

# 4.	Reverse the given number and display the sum of its digits.
n  = input('Enter the number : ')
rev = n[::-1]
digit = int(n)
total = 0
while digit > 0:
    i = digit % 10
    total += i
    digit = digit // 10
print(rev)
print(total)
