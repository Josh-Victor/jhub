from random import randint                                                                                        #we import random integer from the library 'random'
player_number = input("Please enter a random number between 10 and 99.: ")                                        #we ask the user to input a number
for winning_number in range(1):                                                                                   #this line of code tells the computer to generate only 1 integer
    	winning_number = randint(10, 99)                                                                          #this line tells you the computer to generate a number between 10 and 99
	print("Your number was: " + str(player_number) + " and the winning number was: " + str(winning_number))   #this line prints out a message and the users number as well as the winning number

if player_number == winning_number:                                                                               #this line checks if the users number
                      print("CONGRATULATIONS YOU JUST WON R20,000.00!!!")                                         #this line displays the congratulations message
else:           
                      player_number != winning_number                                                             #this checks if the player number does not match the winning number
                      print("Oh no! You guessed wrong, better luck next time!")                                   #this line displays the better luck next time message 
