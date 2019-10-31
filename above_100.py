user_num = int(input("Please enter a number below 100: "))
user_num_valid = 0
user_num_invalid = 0

while user_num > 100:
    user_num = int(input("Please enter a number below 100: "))
if user_num % 2 == 0:
    user_num_valid = user_num * 2
    print(user_num_valid)
else:
    user_num % 2 == 1
    user_num_invalid = user_num * 3
    print(user_num_invalid)
    
    
    
    
