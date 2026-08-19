i=0
j=0
k=0

for i in range(1,6):
    print(i)
print("///////////////////////////")
for i in range(1,6):
    for j in range(i):
        print(j,end="")
    print()
print("///////////////////////////")

for i in range(1,6):
    for j in range(i,6):
         print(j,end="")
    print()

print("///////////////////////////")


n = int(input('Enter the Number : '))

for i in range(1,n):
  for j in range(j,i):
     print(j,end="") 
print()
