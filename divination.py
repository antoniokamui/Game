print("****************************")
print("Welcome to Divination Number")
print("****************************")

secret_number = 10
number_try = 3
goal = bool(0)

print("You have ", number_try, " attempts.")

while (number_try > 0 ):
    inserted_number = int(input("insert a number between 1 and 20.  \n"))
    if inserted_number >= 1 and inserted_number <= 20:
        if secret_number == inserted_number:
            print("you're right , the secret number is ", secret_number, " your number is ", inserted_number, ".\n")
            print("YOU WON ")
            number_try = 0
            goal = bool(1)
        else:
            if secret_number < inserted_number:
               print("You entered a number greater than the secret number, try again. \n")
            elif secret_number > inserted_number:
               print("You entered a number less than the secret number, try again. \n")

            number_try = number_try - 1
            print("You have ", number_try, " attempts.")
    else:
        print("you entered an invalid number.\n")

if number_try == 0 and goal == (10 < 1):
      print("You Missed , the secret number is ", secret_number, " your number is ", inserted_number, ". \n")

print("Game Over")