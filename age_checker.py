age = int(input("How old are you?: " )) #we ask the user to input their age and assign their 
if age >= 18:                           #the computer checks if the users age is equal to or greater than 18
    print("You are old enough!")        #if the users age is 18 or greater the following mesaged is displayed
elif age >=16:                          #if the user is not 18 or over the computer checks if the users age is equal to or greater than 16
    print("Almost there!")              #if the user is equal to 16 or greater the following message is displayed
else:
    age >16                             #this line checks if the user is younger thab 16
    print("You're just too young!")     #if the user is younger than 16 the following message is displayed

