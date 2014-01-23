from random import randrange
# this line of code ...
random_number = randrange(1, 10)
# randrange is a function that generates a random number within a specified range.
count = 0
# Start your game!
first = raw_input("What is your first guess?")
if first == random_number:
    print "You win!"
else:
    second = raw_input("What is your second guess?")