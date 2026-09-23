'''Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements
 as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.'''


l = [3,5,1]
1,3,5
1,3,5,

1 - 3 = -2 
3 - 5 = -2
def array(list):
    list.sort()
    number = False
    plus = [y - x for x , y in zip(list,list[1:])]
    print(plus)
    for i in plus:
        if i > 0:
          number = True
    print(number)
      

array(l)