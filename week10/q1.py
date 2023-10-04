# Given a list L write a program to make a new list to fix the indexes of numbers to in list L to its same value in the new list. Put 0 at remaining indexes. Also print the elements of the new list in the single line. (See explanation for more clarity.)

# Input:
# [1,5,6]

# Output:
# 0 1 0 0 0 5 6

# Explanation: 

# List L contains 1,5,9 so at 1,5,9, index of new list the respective values are put and rest are initialized as zero.

L = list(map(int, input().split()))

s = set(L)
l = list(s)
l1 = sorted(l)
for i in range(0,max(l)+1):
  if(i in l):
    print(i,end = " ")
  else:
    print (0,end = " ")
  
