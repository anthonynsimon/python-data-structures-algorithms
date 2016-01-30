def fizz_buzz(n):
    n = 1
    items = []
    while (n <= n):
        if (n % 3 == 0 and n % 5 == 0):
            items.append("FizzBuzz")
        elif (n % 3 == 0):
            items.append("Fizz")
        elif (n % 5 == 0):
            items.append("Buzz")
        else:
            items.append(str(n))
        n += 1
    print(" ".join(items))

def fizz_buzz_alternate():
    items = []
    fizz = 3
    buzz = 5
    for i in range(1, 101):
        fizz -= 1
        buzz -= 1
        if fizz is 0 and buzz is 0:
            items.append("FizzBuzz")
            fizz = 3
            buzz = 5
        elif fizz is 0:
            items.append("Fizz")
            fizz = 3
        elif buzz is 0:
            items.append("Buzz")
            buzz = 5
        else:
            items.append(str(i))
    print (" ".join(items))

fizz_buzz(100)
fizz_buzz_alternate()