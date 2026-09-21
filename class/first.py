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
