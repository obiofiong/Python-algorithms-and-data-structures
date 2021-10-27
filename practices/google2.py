
def solution(S):
    totalPoints = 0
    rodColor = {}
    for entry in range(0,len(S),2):
        if S[entry+1] not in rodColor:
            rodColor[S[entry+1]] = S[entry]
        else:
          rodColor[S[entry+1]] += S[entry]
    print(rodColor)
#   return 0
    for values in rodColor.values():
        matchLength = 0
        for value in set(values):
            if value in "BGR":
                matchLength +=1
        if matchLength == 3:
            totalPoints +=1
    return totalPoints







test1 = "R8R0B5G1B8G8"
print(solution(test1))



# You have 10 rods numbered from 0 to 9. There are three types of rings—red, green and blue—being put on the rods. You get a point for each rod that has a ring of each color on it, i.e. to get a point you need a red ring, green ring and blue ring on one rod.

# A ring put on a rod is represented by two characters—the first describes the color of the ring and the second describes which number rod it is on from 0 to 9. For example "R8" means that a red ring is being put on the 8th rod. 


# Write a function:

# class Solution { public int solution(String S); }

# that, given a correct string of length 2N describing the N rings put onto rods, returns how many points you will get.

# Examples:
# For ""B2R5G2R2,"" the answer is 1
# Given S = "R8R0B5G1B8G8", your answer should be 1. You get one point for rings put on the 8th rod (there is one red, one blue and one green ring on it). There is also a red ring on the 0th rod, green on the 1st rod and blue on the 5th rod. You don't get points for them because they don't form a full trio on one rod. There are no rings on any of the other rods.