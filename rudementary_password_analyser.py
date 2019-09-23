pass_length_6 = False
up_case = False
low_case = False
has_num = False
access_granted = 0        #access granted is given the value of 0
suitable_pass = False     #suitable pass is here to let the program know if the password is suitable or not
import sys                #we import sys for later use

#*****************************
pass_length_6 = input("Does your password contain more than 6 characters?: ")     #we begin to ask the user questions
if pass_length_6 == "yes":     #if the user answers "yes"
    pass_length_6 = True       #the valuechanges to True
    access_granted +=1         #if the user answer "yes" the value of access_granted increases by 1

#*****************************
up_case = input("Does your password contain one or more uppercase characters?: ")
if up_case == "yes":       #if the user answers "yes"
    up_case = True         #the valuechanges to True
    access_granted +=1     #if the user answer "yes" the value of access_granted increases by 1
#*****************************

low_case = input("Does your password contain one or more lower case characters?: ")
if low_case == "yes":     #if the user answers "yes"
    low_case= True        #the valuechanges to True
    access_granted +=1    #if the user answer "yes" the value of access_granted increases by 1

if access_granted == 3:   #this line checks if access_granted has a value of 3
    suitable_pass = True  #if access_granted has the value of 3 suitable_pass is set to True

if suitable_pass == True:                     #this line checks if suitable_pass is True
    print("Your password IS strong enough!")  #if suitable_pass is True print thhe following statement

if suitable_pass == True: #this line checks if suitable_pass is true
    sys.exit()            #if suitable pass is True this stops the program from asking additional questions
    

#*****************************        
has_num  = input("Does your password contain one or more lower case characters?: ")
if has_num == "yes":     #if the user answers "yes"
    has_num = True       #the valuechanges to True
    access_granted +=1   #if the user answer "yes" the value of access_granted increases by 1

if access_granted == 3:  #this line checks if access_granted has a value of 3
    suitable_pass = True #if access_granted has the value of 3 suitable_pass is set to True

if suitable_pass == True:                      #this line checks if suitable_pass is true
    print("Your password IS strong enough!")   #if suitable_pass is True print thhe following statement

if suitable_pass == False:                         #this line checks if suitable_pass is False
    print("Your password is NOT strong enough!")   #if suitable_pass is False print thhe following statement











        
        


    



