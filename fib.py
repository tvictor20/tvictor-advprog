import sys

def fib(n):
    x, y, z = 0, 1, 1
    print x
    print y
    for i in range(0,n-2):
        z = x + y
        x, y = y, z
        print z

if __name__ == "__main__":
    fib(int(sys.argv[1]))
