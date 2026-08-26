weather = int(input("Enter the weather number : "))

number = True

prime = [ i for i in  range(1,weather) if i%weather == 0]

print(prime)