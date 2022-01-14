Resource: https://youtu.be/DLn3jOsNRVE

Tech with Tim 5 Mini Projects for Beginners
This is the second project, the number guesser

generate a random number and track how many attempts it takes to guess the number


NOTES:

#random is a module you can import
import random

# .randrange(start, stop)
# the will generate a number btwn the start and stop but does not include the stop #
# so, if you wanted it to guess a number btwn -1 and 10 you would write it as (-1, 11)
# if you want the range to start at 0 you can put just the stop in ().  Again it will not include that number in the range
#print(random.randrange(-5,11)) -- will randomly print numbers between -5 and 10

r = random.randrange(-5,11)
print(r)

# .randint(start, stop)
# unlike the .randrange(start, stop), this will print the stop value

r_int = random.randint(-5, 11)
print(r_int)


# .isdigit()
# a method that will return true or false depeding if the input is a digit or not  