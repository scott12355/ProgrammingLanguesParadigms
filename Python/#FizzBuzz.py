#FizzBuzz

#Scotts implementation
#procedural - parameterized
def fizz_buzz(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
#fizz_buzz(100)

#can be further broken down into two functions
def divisibleBy(number, divisor):
    return number % divisor == 0

def fizz_buzz2(n):
    for i in range(n+1):
        if divisibleBy(i, 5):
            print('FizzBuzz')
        elif divisibleBy(i, 3):
            print('Fizz')
        elif divisibleBy(i, 5):
            print('Buzz')
        else:
            print(i)

fizz_buzz2(100)


########################################################################
#imperative solution
#version 1 - if-else ladder
for x in range(1,101):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
print()


