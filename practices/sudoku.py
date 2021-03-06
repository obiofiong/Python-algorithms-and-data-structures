print('Starting')

def check_sudoku(square): 
    # Create a list with the integers 1, 2, ..., n.
    # We will check that each number in the row is in the list
    # and remove the numbers from the list once they are verified
    # to ensure that each number only occurs once in the row.
    for row in square:
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:  
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True
square = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]
print(check_sudoku(square))