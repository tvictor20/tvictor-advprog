class Student():
    counter = 0
    boyCounter = 0
    def __init__(self, name, lastName, gender):
        self.name = name
        self.lastName = lastName
        self.number = Student.counter
        if gender == "boy":
            Student.boyCounter += 1
        Student.counter += 1

    def numberIn(self):
        self.number += 1




tommy = Student("Tommy", "Victor", "boy")
ben = Student("Ben", "Rosin", "none")
javier = Student("Javier", "Carmona", "boy")
jesse = Student("Jesse", "McilHenny", "none")

javier.numberIn()
print tommy.boyCounter
print javier.boyCounter
print tommy.number
print ben.number
print javier.number
print jesse.number
