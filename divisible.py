x = False
i = 2520
while x == False:
    if i % 18 == 0 and i % 14 == 0 and i % 11 == 0 and i % 13 == 0 and i % 17 == 0 and i % 19 == 0 and i % 12 == 0 and i % 16 == 0:
        x = True
        print i


    else:
        i = i + 20

print "done"
