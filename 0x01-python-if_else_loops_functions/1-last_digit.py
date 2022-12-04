#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = number % 10 if number >= 0 else ((-number % 10) * -1)
print(f"Last digit of {number} is {lastNumber}")
if lastNumber > 5:
    print("and is greater than 5")
elif lastNumber == 0:
    print("and is 0")
elif lastNumber < 6 and lastNumber != 0:
    print("and is less than 6 and not 0")
