def factorial(dig):
    if dig > 1:
        return dig * factorial(dig-1)
    else:
        return 1


def main():
    print factorial(998)

main()
