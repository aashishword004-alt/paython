floor = [1,2,3,4,5,6,7,8,9,10]

floor_number = int(input('Enter the floor number : '))

if floor_number not in floor:
      print('floor number are not available only have 10 floor')
else:
      print('floor is hear',floor_number)
      floor_number2 = int(input('Enter the floor number '))
      if floor_number2 == floor_number:
            print('door are open ') 
      else:
            print('floor are hear   : ' , floor_number2)
      