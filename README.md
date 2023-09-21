# Divination Game
#### Video Demo:  https://youtu.be/XeottSGy884
#### Description:
Hello everyone, my name is Antonio Fujii, I'm from São Paulo Brazil.  
I have a bachelor's degree in computer science and an MBA in Internet of Things in my country.  
 
This is the numerical guessing game made in Python for Harvard CS50.  
It is a simple program and was created just for fun and to pass the time.    
Basically the game consists of you entering a number from 1 to 20, trying to guess the secret number that is in hardcode.  
You have 3 attempts, if you make a mistake it will inform you whether the number entered is below or above the secret number.  
If you get it right, the game will inform you that you got it right and it will end.    
If you miss all 3 attempts, the game will inform you that you lost and it will end.  

I used Python 3 because it is a current and easy-to-use language.  
I used basic commands such as data entry, while, conditionals.

> [!IMPORTANT]
> Let's go to the code!!!  
I created a file called divinacao.py , Below is the complete file code:  
>
```python
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
```
> [!IMPORTANT]
let's explain the code:

> I started by a welcome sentence
 ```python
print("****************************")
print("Welcome to Divination Number")
print("****************************")
```

> I declared 3 variables informing their values:  
 - secret_number = is the number to be guessed  
 - number_try = is the number of attempts, its fixed in 3  
 - goal = bool(0) variable for flow control with initial value of false
```python
secret_number = 10 
number_try = 3 
goal = bool(0) 
```
> Displaying a message containing the number of attempts  
```python
print("You have ", number_try, " attempts.")
```

>#### looping that contains most of the program execution , it will run until the number of attempts reaches zero.
```python
while (number_try > 0 ):
```
> I am creating the variable inserted_number that records the user input, already converting the string type to integer.
```python
inserted_number = int(input("insert a number between 1 and 20.  \n"))
```
> Here we check if the numerical value is between 1 and 20(which is required to play), and a sentence with a line break at the end.
I will name this if  the  "inputIF_1_20"
```python
	if inserted_number >= 1 and inserted_number <= 20:
```
> Here we compare the user input inserted_number value with the secret_number value.  
If they are the same, a message will be displayed containing the numbers and that the user has won the game.  
The number of attempts will receive the value 0, causing the loop to stop executing and the correct answer will receive the true value.
```python
		if secret_number == inserted_number:
            		print("you're right , the secret number is ", secret_number, " your number is ", inserted_number, ".\n")
					print("YOU WON ")
            		number_try = 0
            		goal = bool(1)
			print("Game Over ")
```
> else the number is not the same, it will enter these conditions:  
If the inserted_number is greater than secret_number the system reports it to user, and a line break at the end.
```python
	    	else:
 	            if secret_number < inserted_number:
               		print("You entered a number greater than the secret number, try again. \n")
```
> else if the inserted_number is less than secret_number , the system reports it to user, and a line break at the end.
```python
			elif secret_number > inserted_number:
		               print("You entered a number less than the secret number, try again. \n")
```
> The number of attempts will be decremented by one
 A message containing the remaining number of attempts will be displayed
```python
				number_try = number_try - 1
				print("You have ", number_try, " attempts.")
```
> This ELSE is the counterpart of inputIF_1_20, the numerical value is not between 1 and 20, a message will be displayed , and a line break at the end.
```python
	else:
        print("you entered an invalid number.\n")
```
> After the loop completes, it will to check whether the number of attempts is over and the goal variable is false, the message will be displayed with the last inserted_number entered and the secret_number.
```python
if number_try == 0 and goal == (10 < 1):
      print("You Missed , the secret number is ", secret_number, " your number is ", inserted_number, ". \n")
```
> When the game ends, the message system will  be displayed game over 
```python
print("Game Over ")
```



