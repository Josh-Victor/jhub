age_check = int(input("Please enter the year in whcih you were born: "))
#we ask the user to input the year in which they were born in for use in our if statements
if age_check <= 2001:
    print("Congratulations you have met the minimum age requirement!!!")
#our if statement checks to see if the user was born before 2001 if they were they recieve the above message

if age_check >= 2001:
    print("Oh no!!! You have not met the minimum age requirement come back again in a few years.")
#our if statement checks to see if the user was born before 2001 if they weren't they recieve the above message
