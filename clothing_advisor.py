temp_above_20 = False
is_weekend = False
is_sunny = False

###################################################################
temp_above_20 = input("Is the temperature above 20 degrees?: ")     #we ask the user if the temperature is above or below 20 degrees
if temp_above_20 == "yes":                                          #this line checks if the answer from the user was 'yes'
    temp_above_20 = True                                            #if the user answered yes temp_above_20 changes to True
    if temp_above_20 == True:                                       #this line checks if temp_above_20 is True
        temp_above_20 = "A short sleeved shirt"                     #if temp_above_20 is True, the value temp_above_20 changes to the text within the " "


if temp_above_20 == "no":                                           #this line checks if the answer from the user was 'no'
    temp_above_20 = False                                           #if the user answered yes temp_above_20 changes to False
    if temp_above_20 == False:                                      #this line checks if temp_above_20 is False
        temp_above_20 = "A short sleeved shirt"                     #if temp_above_20 is False, the value temp_above_20 changes to the text within the " "
####################################################################
is_weekend = input("Is it the weekend yet?: ")                      #we ask the user if it is the weekend
if is_weekend == "yes":                                             #this line checks if the answer from the user was 'yes'
    is_weekend = True                                               #if the user answered yes is_weekend changes to True
    if is_weekend == True:                                          #this line checks if is_weekend is True
        is_weekend = "shorts"                                       #if is_weekend is True, the value is_weekend changes to the text within the " "
        
if is_weekend == "no":                                              #this line checks if the answer from the user was 'no'
    is_weekend = False                                              #if the user answered no is_weekend changes to False
    if is_weekend == False:                                         #this line checks if is_weekend is False
        is_weekend = "jeans"                                        #if is_weekend is False, the value is_weekend changes to the text within the " "
####################################################################
is_sunny = input("Is it sunny today?: ")                            #we ask the user if it is sunny or not
if is_sunny == "yes":                                               #this line checks if the answer from the user was 'yes'
    is_sunny = True                                                 #if the user answered yes is_Sunny changes to True
    if is_sunny == True:                                            #this line checks if is_sunny is True
        is_sunny = "a cap"                                          #if is_sunny is True, the value is_weekend changes to the text within the " "

if is_sunny == "no":                                                #this line checks if the answer from the user was 'no'
    is_sunny = False                                                #if the user answered yes is_sunny changes to False
    if is_sunny == False:                                           #this line checks if is_sunny is False
        is_sunny = "a raincoat"                                     #if is_sunny is False, the value is_weekend changes to the text within the " "
#####################################################################

print("Your outfit for today is as follows: " + str(temp_above_20) + ", " + str(is_weekend) + " and " + str(is_sunny) + ".")
#The above line of codes prints out a message that layed out in relation to the answers the user gave

                 

