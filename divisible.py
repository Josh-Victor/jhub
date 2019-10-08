import sys
user_num = int(input("Please enter a number!: "))

outcome_1 = False                                             #divisible by 2 and 5
outcome_2 = False                                             #divisible by 2 or 5
outcome_3 = False                                             #not divisible by 2 or 5

if user_num % 2 == 0 and user_num % 5 == 0:
    print("Your number is divisible by 2 and 5!")
    sys.exit()

if user_num % 2 == 0:
    print("Your number is divisble by 2!")
    sys.exit()
    

elif user_num % 5 == 0:
    print("Your number is divisble by 5!")
    sys.exit()
    

else:
    user_num % 2 == 1 or user_num % 5 == 1
    print("Your number is not divisble by 2 or 5")
    sys.exit()
    
