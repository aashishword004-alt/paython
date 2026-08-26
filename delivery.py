amount = int(input('Enter the amount : '))

distance = int(input("Enter the distance : "))

check_weather = str(input('Enter the weather condition   : '))

rain_charge = 30

weather = 'rainny'

if check_weather == weather:
     dis_fee = distance * 20
     amount += dis_fee + rain_charge
     print(['Total fee : ' , amount , 'Rainny charge' , rain_charge,'delivery fee ' , dis_fee, 'Thanks for order Enjoy the Food' ])
else:
     dis_fee = distance * 20
     amount += dis_fee + amount
     print(['Total fee' , amount,'delivery fee ' , dis_fee,'Thanks for order Enjoy the Food'])
       