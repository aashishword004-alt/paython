amit = {'python' , 'java' , 'git' , 'linux'}

rahul = {'sql' ,'c++','python','java'}

priya = {'sql' , 'python' , 'machinlearning','java'}

unique = amit |  rahul
print(unique)

unique2 = unique ^ priya
print(unique2)



# output = {machinlearning ,c++,git,linux}