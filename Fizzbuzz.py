### Fizzbuzz ###

import time

choice = (int(input("What number would you like to choose?")))

def function(choice):
    for num in range(1, choice):
        if num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        else:
            print(num)

print("about to run the program")
time.sleep(5)
function(choice)
    
