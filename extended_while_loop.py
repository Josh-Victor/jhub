import sys
user_num_sum = 0
user_num_entries = 0
user_num_avg = 0
user_abort = False
user_name_entries = 0

user_num = int(input("Please enter a number!: "))

while user_num > 0:
    user_num = int(input("Please enter a number!: "))
    user_num_sum += user_num
    user_num_entries += 1

if user_num < 0:
    user_num_avg = user_num_sum / user_num_entries
    
user_name = input("Please try to guess my name: ")

while user_name != "Josh":
    user_name = input("Please try to guess my name: ")
    user_name_entries += 1

if user_name == "Josh":
    print("You tried to guees the name " + str(user_name_entries) + " times before getting it right! ")

user_abort = input("Would you like to abort?: ")
if user_abort == "yes":
    sys.exit()  

print("The average of the numbers entered is: " + str(user_num_avg))



    
    
    
    

