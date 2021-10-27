def solution(A):
    print(A)
    palindrome = []
    selfReverse = False
    used = set()
    uses = {}
    for i,pair in enumerate(A):
        if (pair,i) not in used:
            print("unused pair",pair)
            if pair[::-1] in A and A[i] != pair[::-1] :
                # print(pair[::-1])
                palindrome.append(pair)
                palindrome.append(pair[::-1])
                # A.pop(pair[::-1]) 
                # A.pop(pair)
                
                for j in range(i+1,len(A)):
                    if pair[::-1] == pair:
                        used.add((pair[::-1],j))
                        used.add((pair,i))
                        break
            elif pair == pair[::-1]:
                if selfReverse == False:
                    selfReverse = True
                    palindrome.append(pair)
                    used.add(pair)

            else:
                continue
    print(used)
    print(palindrome)
    return len(palindrome) * 2


# ab ba ab ba


test1 = ["ab", "hu", "ba", "ab","ab","ab","ba"]

test2 =     ["ca", "rd", "oo", "dr","ac"]
print(solution(test1))