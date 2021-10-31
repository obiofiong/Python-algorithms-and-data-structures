def jump_to_flag(flagHeight , bigJump) :
    # flagHeight 
    check = 0
    i = 0
    while check < flagHeight:
        check = bigJump * i
        print(check)

        i +=1
        print('i',i)
    if check < flagHeight:
        i = i - 2
        check = check - bigJump
        jumps = flagHeight - (check)
        return i  + jumps
    elif check > flagHeight:
        check = check - bigJump
        
        return 
    else:
        return i - 1


print(jump_to_flag(flagHeight = 19, bigJump = 2))