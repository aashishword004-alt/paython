a =   [3, 4, 24, 24, 6]
count = {}
for n in a:
    count[n] = count.get(n, 0) + 1
    print(count)

duplicates = [n for n, c in count.items() if c > 1]
print(duplicates)