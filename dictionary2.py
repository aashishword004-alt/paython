stds = {
"S1": {"name": "Amit", "age": 16,
"marks": {"Math": 85, "Science": 90, "English": 78},
"guardian": ("Mr. Sharma", "9998887777")},

"S2": {"name": "Bela", "age": 15,
"marks": {"Math": 92, "Science": 88, "English": 95},
"guardian": ("Mrs. Verma", "9998888888")},

"S3": {"name": "Chirag", "age": 16,
"marks": {"Math": 65, "Science": 70, "English": 60},
"guardian": ("Mr. Patel", "9998889999")},

"S4": {"name": "Divya", "age": 14,
"marks": {"Math": 88, "Science": 91, "English": 84},
"guardian": ("Mrs. Rao", "9998880000")},
}


#1. Print student "S2"’s marks in Science only.

print(stds['S2']['marks']['Science'])

#2. Print the guardian’s name and phone number (the tuple) for student "S3".
print(stds['S3']['guardian'])

#3. Calculate and print each student’s total marks (sum of all 3 subjects).
#4. Find and print the name of the student with the highest total marks.

count = {}
high = 0
for k,v in stds.items():
    total = sum(v['marks'].values())
    if total > high:
          high = total
          keys = k
print(k,v['name'],high)

#5. List the names of all students who scored above 80 in Math.


for k,v in stds.items():
     math = (v['marks']['Math'])
     if math > 80:
      print(k,v['name'],math)
 




#6. Add a new subject, "Computer": 95, to student "S1"’s marks dictionary.
stds["S1"]['marks']['computer'] = 95

print(stds)