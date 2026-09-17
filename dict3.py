prd = {
"P001": {"name": "Laptop", "price": 55000, "category":
"Electronics",
"tags": ["computer", "portable"],
"specs": ("Intel i5", "8GB RAM", "512GB SSD")},
"P002": {"name": "Office Chair", "price": 7500, "category":
"Furniture",
"tags": ["ergonomic", "adjustable"],
"specs": ("Mesh back", "Adjustable height", "360-degree swivel")},
"P003": {"name": "Smartphone", "price": 22000, "category":
"Electronics",
"tags": ["mobile", "5G"],
"specs": ("6.5-inch display", "128GB storage",
"5000mAh battery")},
"P004": {"name": "Study Table", "price": 4200, "category":
"Furniture",
"tags": ["wooden", "compact"],
"specs": ("120x60 cm", "Engineered wood", "2 drawers")},
"P005": {"name": "Headphones", "price": 3000, "category":
"Electronics",
"tags": ["wireless", "noise-cancelling"],
"specs": ("Bluetooth 5.0", "30-hour battery", "Overear")},
}




# 1 Print the specs (the tuple) of product "P003".
print(prd["P003"]['specs'])


# 2. List the names of all products in the "Electronics" category.
for k,v in prd.items():
    if 'Electronics' in (k,v['category']):
        print(k,v['category'])


# 3. Find and print the name of the cheapest product overall
chep = 5000
for k,v in prd.items():
      low = (v['price'])
      if low < chep:
       chep = low

print(k,v['name'],chep)

# 4. Print all the tags of product "P002".
for k,v in prd.items():
    if "P002" in (k):
        print(k,v['tags'])


# 5. Count how many products are priced above Rs. 5000.

count = 0
for k,v in prd.items():
   price = (v["price"])
   if price > 5000:
       count+=1
       keys=k

print(count)

# 6. Apply a 15% discount to product "P001" — update its price in place and print the new price.
prd["P001"]['price'] -= prd["P001"]['price']*.15

print(prd)