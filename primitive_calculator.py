num_1 = int(input("Please input a number: "))
num_2 = int(input("Please input a number: "))
num_3 = int(input("Please input a number: "))
#num_1-3 are variables that are declared by the user for later mathematical purposes.
#we also cast the input to int() so that the computer can do mathemematical equations


sum_of_nums = num_1 + num_2 + num_3
#we apply addition to the values declared by the user.
subtract = num_1 - num_2
#we subtract num_1 from num_2 which are values provoided by the user. 
multiply = num_1 * num_3
#we multiply num_1 by num_2 which are values provided by the user.
sum_divided_num_3 = (num_1 + num_2 + num_3) / num_3
#we apply addition to the values the user provided, then after we divide the total sum by the variable num_3

print("The sum of all the numbers.")
print(sum_of_nums)
print("The first number minus the second number.")
print(subtract)
print("The third number multiplied by the first number.")
print(multiply)
print("The sum of all three numbers divided by the third number.")
print(sum_divided_num_3)
