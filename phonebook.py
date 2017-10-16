def main():
    phonebook = {}
    while True:
        print "Press 1 to add an entry to the phonebook"
        print "Press 2 to search for a name by a number"
        print "Press 3 to search for a number by a name"
        print "Press 4 to remove an entry from the phonebook by name"
        print "Press 5 to see the phonebook"
        print "Press 6 to exit"
        x = input()
        if x == 1:
            print "\n"
            nameEntry = raw_input("Enter the name")
            numEntry = input("Enter the number")
            phonebook[nameEntry] = numEntry
            print "\n"
        if x == 2:
            print "\n"
            nameFinder = raw_input("Type in the number you're looking for the name associated with: ")
            isNum = False
            for key, value in phonebook.items():
                if int(value) == int(nameFinder):
                    print "The person who holds that number is " + key + "\n"
                    isNum = True
            if isNum == False:
                print "That number is not in the book \n"

        if x == 3:
            print "\n"
            numFinder = raw_input("Type in the name you're looking for the number associated with: ")
            isName = False
            for key, value in phonebook.items():
                if str(key) == str(numFinder):
                    print "The number of that person is " + str(value) + "\n"
                    isName = True
            if isName == False:
                print "That name is not in the book \n"

        if x == 4:
            print "\n"
            numToDel = raw_input("Enter the name to remove")


        if x == 5:
            print "\n"
            for key, value in phonebook.items():
                print str(key) + " : " + str(value)
        print "\n"

        if x == 6:
            exit()
main()
