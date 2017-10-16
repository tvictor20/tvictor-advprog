def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic4 = {}
    for (key1, value1), (key2, value2), (key3, value3) in zip(dic1.items(), dic2.items(), dic3.items()):
        dic4[key1] = value1
        dic4[key2] = value2
        dic4[key3] = value3

    print dic4

    for key, value in dic4.items():
        print key

    x = bool

    keyCheck = raw_input("What key are you checking for?")
    for key, value, in dic4.items():
        if keyCheck == str(key):
            x = True

    if x == True:
        print "That key is in the dictionary"
    else:
        print "That key is not in the dictionary"
main()
