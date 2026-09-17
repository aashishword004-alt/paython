patients = {
"PID001": {"name": "Rita", "age": 45, "doctor": "Dr. Mehta",
"medications": ["Metformin", "Insulin"],
"admission": ("2026-01-05", "Ward 3")},
"PID002": {"name": "Sanjay", "age": 60, "doctor": "Dr. Rao",
"medications": ["Atorvastatin"],
"admission": ("2026-01-07", "Ward 1")},
"PID003": {"name": "Kavita", "age": 32, "doctor": "Dr. Mehta",
"medications": ["Paracetamol", "Vitamin D"],
"admission": ("2026-01-08", "Ward 3")},
"PID004": {"name": "Farhan", "age": 50, "doctor": "Dr. Iyer",
"medications": ["Amlodipine"],
"admission": ("2026-01-06", "Ward 2")},
}

# 1. Print the full record of patient "PID002".
# print(patients["PID002"])

# 2. List the names of all patients under "Dr. Mehta".
for k,v in patients.items():
    if 'Dr. Mehta' in (k,v['doctor']):
        print(k,v)

# 3. Find and print the name of the oldest patient.
old = ''
for k,v in patients.items(): 
    old =  min(v['admission'])
    keys = k
    break

print(k,v['name'],old)

# 4. Print the admission date and ward (the tuple) for patient "PID004".
Pi = set(patients["PID004"]['admission'])
print(Pi)

# 5. Count how many patients are currently in "Ward 3".
count = 0
for k,v in patients.items():
    if 'Ward 3' in (v["admission"][1]):
        count+=1

print(count)

# 6. Add "Cough Syrup" to patient "PID003"’s medications list.
patients["PID003"]['medications'].append('Coup sryup')

print(patients)