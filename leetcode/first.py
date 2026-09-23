'''Example 1:
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s


Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged'''

#Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
word1 = 'abc'
word2 = 'pqr'
def marge(word,word2):
    new_str = "".join(a + b for a,b in zip(word1,word2))
    print(new_str)



# merged: a p b q   r   s
w1 = 'ab'
w2 = 'pqrs'

def marge2(w1,w2):
    new_str = "".join(a + b for a , b in zip(w1,w2))
    print(new_str)


marge(word1,word2)
marge2(w1,w2)


'''Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

 '''