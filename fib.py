def main():
    x, y, z = 0, 1, 1
    print x
    print y
    for i in range(100):
        z = x + y
        x = y
        y = z
        print z

main()
