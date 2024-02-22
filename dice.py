import random

print("Welcome to Dice Roller")
print("----------------------")

#ask user to choose how many sides on dice
print("How many sides on the dice would you like?")
#validate input
while True:
 try:
    diceSides = int(input("Type of number between 1 and 20: "))
    if (diceSides > 0 and diceSides < 21):
      break
    else:
      print("please enter a integer between 1 and 20: ")
 except:
    print("Invalid input. Please enter a integer between 1 and 20")

print("How many dice would you like to role?")
#validate input
while True:
 try:
    numberPicked = int(input("Type a number between 1 and 10: "))
    if(numberPicked > 0 and numberPicked < 11):
      break
    else:
      print("Invalid input. Please enter a integer between 1 and 10.")
 except:
   print("Invalid input. Please enter a integer between 1 and 10.")
   
results = []

#roll the dice 
for _ in range(numberPicked): 
  roll = random.randint(1, diceSides)  
  results.append(roll)
  print(f"You rolled a {roll}")
