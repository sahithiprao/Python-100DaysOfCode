#Write your code below this row 👇
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    elif num % 5 == 0:
        num = "Buzz"
    elif num % 3 == 0:
        num = "Fizz"
    print(num)
