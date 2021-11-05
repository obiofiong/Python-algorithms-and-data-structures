
# O(N^2) solution

# 1 6 8 9 0 
def rotate_180(arr):
    valid = []
    invalid = [2,3,4,5,7]
    for num in range(arr):
        check = 0
        for i in num:
            # if check == 0 or check == 
            if i in invalid:
                break
            else:
                check +=1
            
        if check == len(num):
            valid.append(num)
    return len(valid)
print(rotate_180(12))


