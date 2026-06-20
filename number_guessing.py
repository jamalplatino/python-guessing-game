import random

# chosenNumber = random.randint(1, 100)
chosenNumber = random.choice([1,2,3,4,5,6,7,8,9,10])
# start guessing
choice = input("Pick a number between 1-10 for your lucky number: ")

while True:
    # higher than
    if int(choice) > chosenNumber:
        choice = input(f"Too high, try again but choose a lower number than {choice} ")
    # lower than
    elif int(choice) < chosenNumber:
        choice = input(f"Too low, try again but choose a higher number than {choice} ")
    # terminate
    elif choice == "x":
        print("Thank you for playing with you")
        break
    # if its the right number
    elif int(choice) == chosenNumber:
        print(f"Congratulations on the getting your lucky number {chosenNumber} ")
        break