#3 digitx3 digit = palindrome

def palindrome(x):
    y = str(x)
    if len(y) % 2 == 0:
        z = y[len(y)/2:len(y)]
        if y[0:len(y)/2] == str(z[::-1]):
            return True
        else:
            return False

    else:
        k = len(y) - 1
        z = y[(k/2) + 1:len(y)]
        if y[0:k/2] == str(z[::-1]):
            return True
        else:
            return False

def main():
    cPal = 0
    for a in range (9999, 99, -1):
        for b in range (9999, 99, -1):
            c = a*b
            pal = palindrome(c)
            if pal == True and c > cPal:
                cPal = c

    print cPal

main()
