def FizzBuzz():
    numbers = []
    for i in range(0, 101, 1):
        numbers.append(i)
    for number in numbers:
        if number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz")
        else:
            print("Number: ", number)
FizzBuzz()