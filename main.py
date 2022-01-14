#Goal: generate a random number and track how many attempts it takes to guess the number assuming the range starts at 0.
import random


print("Goal: to guess the computer's randomly generated number. The range start at zero, but you will choose the top range value. ")

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  if top_of_range <= 0:
    print("Please type a number greater than zero next time")
    quit()
else:
  print("That is not a digit.  Please type a number next time")
  quit()

random_number = random.randint(0, top_of_range)
print(random_number)