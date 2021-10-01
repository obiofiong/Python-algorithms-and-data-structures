class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def birthday(self):
        self.age +=1

names = ['john',"mich"]
ages = [1,5]
people = set(zip(names, ages))

person_objects = []
for i in people:
    person_objects.append(Person(*i))
    # print(i)
    # print(*i)
    # print(i.)
for i in person_objects:
    print(i.birthday()) #returns none

print(people)
print(person_objects)