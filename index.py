'''Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"'''

arr = [3,5,1]
def chevk(arr):
    output = False
    for i in arr:
       if i > 0:
          output = True
    print(output)


chevk(arr)