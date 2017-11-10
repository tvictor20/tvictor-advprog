class Student():
    counter = 0

    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
        self.number = Student.counter
        Student.counter += 1

    def numberIn(self):
        self.number += 1




tommy = Student("Tommy", "Victor")
ben = Student("Ben", "Rosin")
javier = Student("Javier", "Carmona")

javier.numberIn()
print tommy.number
print ben.number
print javier.number
