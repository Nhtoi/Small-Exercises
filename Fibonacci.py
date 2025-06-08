def fib(number):
    i = 0
    a=0
    b=1
    tmp = 0
    while i < number:
        tmp = a
        a += b
        b = tmp
        print(b)
        i += 1
fib(11)