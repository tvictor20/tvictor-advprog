class Student():
    counter = 0
    maleCounter = 0
    def __init__(self, name, lastName, gender):
        self.name = name
        self.lastName = lastName
        self.number = Student.counter
        if gender == "male":
            Student.maleCounter += 1
        Student.counter += 1

studentList = []
tommy = Student("Tommy", "Victor", "male")
studentList.append(tommy)
ben = Student("Ben", "Rosin", "male")
studentList.append(ben)

def main():
    while True:
        print "There are " + str(tommy.counter) + " students in the directory"
        print "Press 1 to see everyone in the directory"
        print "Press 2 to add someone to the directory"
        x = input()
        print ""
        if x == 1:
            for i in studentList:
                print i.name + " " + i.lastName

        if x == 2:
            fname = raw_input("What is their first name? ")
            lname = raw_input("What is their last name? ")
            gender = raw_input("What is their gender?")
            fname = Student(fname, lname, gender)



main()
