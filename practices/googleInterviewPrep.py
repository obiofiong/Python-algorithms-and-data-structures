# 
def minimumServerDifference(A):
    # empty ipnput test case
    # A = sorted(A)
    A.sort()
    serverA = 0
    serverB = 0
    for i in range(len(A)-1,-1,-1):
        if serverA - serverB <= 0:
             serverA += A[i]
        else :
            serverB += A[i]
    return abs(serverA - serverB)


print(minimumServerDifference(test1))









# 1
#   2
#   3
#   4
#   5
#   7
  
#       7   5    
# 4     11  9
# 3     10  8
      
#       10  9
# 2     12  11
# 1     11  10
      
#       11  11   --- 0


# 1 3 4 7 9 13 17 20 21 
  
#       20  21
# 17    37  38
# 13    33  34

#       33  34
  
  
  
#   1 2 3 4 5 7 25
  
#       25  7     18
# 6               10
# 5     30  12    5
# 4     29  11    1
# 3               -2
# 2      27        0
# 1         28     1