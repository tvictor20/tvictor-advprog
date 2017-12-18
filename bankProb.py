class BankAccount():

    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
        self.balance = 100

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount


accountList = []
accountList.append(BankAccount("Tommy", "Victor"))

def main():
    running = 1
    while running == 1:
        print "Press 1 to see everyone in the directory"
        print "Press 2 to add someone to the directory"
        print "Press 3 to deposit money"
        print "Press 4 to withdraw money"
        print "Press 5 to close"
        try:
            x = input()
        except NameError:
            print "Invalid input"
            print ""
            x = 6
        print ""
        if x == 1:
            for i in accountList:
                print i.name + " " + i.lastName
            print ""

        if x == 2:
            fname = raw_input("What is their first name? ")
            lname = raw_input("What is their last name? ")
            accountList.append(BankAccount(fname, lname))

        if x == 3:
            g = 0
            while g == 0:
                print "Which account do you want to withdraw from?"
                x = raw_input()
                for i in accountList:
                    if x == i.name:
                        print "success"
            while g == 0:
                try:
                    print "How much would you like to deposit?"
                    x = input()
                    g = 1
                except NameError:
                    print "Invalid input"
                    print ""



        if x == 5:
            running = 0

        else:
            print "Invalid input"
            print ""


main()
