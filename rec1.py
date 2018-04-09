def digit(dig):
    if dig > 10:
        return 1 + digit(dig/10)
    else:
        return 1


def main():
    print digit(45345342.62)

main()
