# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def birthday(self):
#         self.age +=1

# names = ['john',"mich"]
# ages = [1,5]
# people = set(zip(names, ages))

# person_objects = []
# for i in people:
#     person_objects.append(Person(*i))
#     # print(i)
#     # print(*i)
#     # print(i.)
# for i in person_objects:
#     print(i.birthday()) #returns none

# print(people)
# print(person_objects)


#

# print(min(a,b))

def removeDuplicates( nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     duplicates = []
#     for i in nums:
#         if i not in duplicates:
#             duplicates.append(i)
#     return duplicates


# print(len(removeDuplicates([1,1,2])))


# a = '1'
# while len(a):
    
# test1 =  [[1,3],[15,18],[2,6],[8,10]]
# test2 = [2,72,5,7,4,2]
# test1.sort(key = lambda x : x[1])
# print(test1)

a = 'ab'
b = 'aba'

#print Zoropay 
# get character
get_char = lambda x: chr(x+ord('a'))

print(get_char(4))
