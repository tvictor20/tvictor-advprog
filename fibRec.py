def fib(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    else:
        return fib(num - 1) + fib(num - 2)




def main():
    num = fib(3)
    print num

main()
