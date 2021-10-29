# Check the maximum amount of BALLONS in a given string
def search(word):
    phrase = {
        'B': 1,
        'A' :1,
        'L': 2,
        'O': 2,
        'N':1
    }
    check = 0
    for item in phrase:
        if item == 'L' or item == 'O':
            if item in word:
                word = word.replace(item,"",1)
                check+=1
                if item in word:
                    word = word.replace(item,"",1)
                    check+=1
        else:
            if item in word:
                word = word.replace(item,"",1)
                check+=1
    if check == 7:
        return [True , word]
    else:
        return [False, word]
def solution(S):
    length = 0
    # s = "BALLOON"
    # phrase = ['B','A','L','O','N']
    found = search(S)
    while found[0]:
        length += 1
        found = search(found[1])

    return length

print(solution('BAONXXOLL'))