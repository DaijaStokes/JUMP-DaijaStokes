def fizz_buzz():
    num = int(input("Enter a number: "))
    fizzbuzz = [0]
    for i in range(1, num + 1):
        if(i % 15 == 0): fizzbuzz.append("Fizzbuzz")
        elif (i%3 == 0): fizzbuzz.append("Fizz")
        elif (i%5 == 0): fizzbuzz.append("Buzz")
        else: fizzbuzz.append(i)
    print(fizzbuzz)
    sum = 0
    for elm in fizzbuzz:
        if (isinstance(elm, int)):
            sum += elm
    print(f"Sum = {sum}")
    print(f"Fizz Count: {fizzbuzz.count('Fizz')}")
    print(f"Buzz Count: {fizzbuzz.count('Buzz')}")
    print(f"Fizzbuzz Count: {fizzbuzz.count('Fizzbuzz')}")

fizz_buzz()