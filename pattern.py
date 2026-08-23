i=0
j=0
k=0

for i in range(1,6):
    print(i)
print("///////////////////////////")
for i in range(1,6):
    for j in range(i):
        if j%2 == 0:
          print('1',end="")
        else:
          print('2' , end="")
    print()
print("///////////////////////////")

for i in range(1,6):
    for j in range(i,6):
         print(j,end="")
    print()
