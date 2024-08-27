#generate a random 6 digit number with no repeating numbers

import random

def main():
    #create a list of numbers 0-9
    numbers = list(range(10))
    #create an empty list
    pin = []
    #loop 6 times
    for i in range(6):
        #pick a random number from the list
        num = random.choice(numbers)
        #add the number to the pin list
        pin.append(num)
        #remove the number from the list
        numbers.remove(num)
    #print the pin
    print(pin)

main()
