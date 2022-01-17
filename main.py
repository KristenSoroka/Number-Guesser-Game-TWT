#Goal: generate a random number and track how many attempts it takes to guess the number assuming the range starts at 0.
import random


print("Goal: to guess the computer's randomly generated number. The range start at zero, but you will choose the top range value. ")

top_of_range = input("Type a number greater than zero: ")

# determining if the variable is a digit. Converting to the str to and int and telling the user what to do if they type in a number less than zero or something other than a number
if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  if top_of_range <= 0:
    print("Please type a number greater than zero next time")
    quit()
else:
  print("That is not a digit.  Please type a number next time")
  quit()

#create a variable that randomly selects a number in range selected by user.
random_number = random.randint(0, top_of_range)

#while loop to track how many times it takes to guess the correct number
guesses = 0
while True:
  guesses += 1
  user_guess = input("Make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("That is not a digit.  Please type a number next time")
    continue
  
  #print("after continue") 
  #this will only print after if a number is entered.  If you enter anything other than a number this pring statement will not print

  #this if statement will only run if a number was entered.
  if user_guess == random_number:
    print("You got the number!")
    break
  elif user_guess > random_number:
    print("Too high")
  else:
    print("Too low")

print(f"you got it in {guesses} guesses")