def minimumSwaps(arr):
    swaps = 0
    for i, ele in enumerate(arr):
        if ele == i+1:
            continue
        temp_slot =  arr.index(i+1)
        arr[i] = i+1
        arr[temp_slot] = ele
        # arr.insert(i, i+1)
        # arr.insert(temp_slot, ele)
        swaps +=1
        print("swap", (i,temp_slot))
        print(arr)
    return swaps

test1 = [2 ,3, 4, 1 ,5]
test2 =[7, 1, 3, 2, 4, 5, 6]
test3 =[1 ,3 ,5 ,2 ,4 ,6 ,7]

print(minimumSwaps(test3))