candidate  = int(input("Enter the  total candidate : "))
weekend = int(input('Enter the day : '))
price = int(input("Enter the price of movie : "))


adult = int(input("How many  adult ? :"))
child = int(input("How many  child  ? :"))
senior  = int(input("How many  senior  ? :"))

adult_total = adult * price
child_total = child*price
senior_total = senior*price

match weekend :
    case 1 :
        day = 'Monday'
    case 2 :
        day = 'tuesday'
    case 3 :
         day = 'wensday'
    case 4 : 
         day = 'thuday'
    case 5:
        day = 'friday'
    case 6 :
         day = 'saturday'
    case 7 : 
        day = 'weekend'
    case _: 
        day = 'not valid day' 

if weekend == 7: 
      child_total -= child_total * 15 / 100
      senior_total -= senior_total * 10 / 100
      final_price = adult_total + child_total + senior_total
      print(final_price,'Weekend day')
else:
           child_total -= child_total * 25 / 100
           senior_total -= senior_total * 15 / 100
           final_price = adult_total + child_total + senior_total
           print(final_price,'noraml day')
       


