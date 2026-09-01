l1  = ['rahul','aman','manish','vivek','aakash','asshish','aman']


name = str(input('Enter the name of student : '))
l1.remove(name)

print(l1)

l1.pop(-1)
print(l1)
sorted(l1)
print(sorted(l1))

n = str(input("Eneter the name of student : "))
coutnt = 0
if n in l1:
    coutnt += 1
    print( n,coutnt,'present')
    print(len(l1))
else:
    print(n,'not present')


    


