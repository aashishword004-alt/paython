"""Q-3 Write a Python program to accept details of n medicines and create a dictionary in the following format:
{
    101: ["Paracetamol", "Tablet", 25.50, 40],
    102: ["Azithromycin", "Tablet", 120.00, 15],
    103: ["Cough Syrup", "Syrup", 85.00, 8],
    ...
}
Where:
Key → Medicine ID
Value → [Medicine Name, Medicine Type, Price, Quantity]
Perform the following tasks:
1.	Create a new dictionary where Medicine ID is the key and value is a tuple containing:
(Medicine Name, Stock Value)
where Stock Value = Price × Quantity.
2.	Display the medicine(s) having the highest stock value. 
3.	Create a set containing all the different medicine types available in the pharmacy. 
4.	Create a dictionary where:
o	Key → Medicine Type 
o	Value → Number of medicines belonging to that type 
Example:
Tablet : 4
Syrup  : 2
Capsule: 3
5.	Display all medicines whose quantity is less than 10 and whose price is greater than the average price of all medicines. 
6.	For each medicine type, find and display the most expensive medicine belonging to that type.
"""

md = {
    101: ["Paracetamol", "Tablet", 25.50, 40],
    102: ["Azithromycin", "Tablet", 120.00, 15],
    103: ["Cough Syrup", "Syrup", 85.00, 8]
}
# 1.	Create a new dictionary where Medicine ID is the key and value is a tuple containing:
#(Medicine Name, Stock Value)
#where Stock Value = Price × Quantity.
d = {}
mx = 0
for k,v in md.items():
    stock = v[2] * v[3]
    if stock > mx:
        mx = stock
    d[v[0]] = {stock}

# 2.	Display the medicine(s) having the highest stock value.
for k,v in d.items():
    if mx in v:
        print(k,v)

#  3.Create a set containing all the different medicine types available in the pharmacy.
 