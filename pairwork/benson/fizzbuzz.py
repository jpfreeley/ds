for _ in range(1,101):
    if _%3  == 0 and _%5 == 0:
        print("FizzBuzz")
    elif _%3  == 0 and _%5 != 0:
        print("Fizz")
    elif _%3  != 0 and _%5 == 0:
        print("Buzz")
    else:
        print(_)


fizzbuzz = ["FizzBuzz" if (i%3 == 0 and i%5 == 0) else "Fizz"
    if (i%3 == 0 and i%5 != 0) else "Buzz"if (i%3 != 0 and i%5 == 0)
    else i for i in range(1,101)]

for _ in fizzbuzz:
    print(_)
