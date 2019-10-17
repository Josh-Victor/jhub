P = int(input("Please input they amount of money you want to store: "))                #this line asks the user to input the amount of money they wish to store which is saved as the variable 'P'
i = float(input("Please input the interest rate you will recieve: "))                  #this line asks the user to input the interest rate they are recieving which is then stored as the variable 'i'
t = int(input("Please enter the number of years you wish to store your money: "))      #this line asks the user to input the number of years they wish to store the money which is then saved as the variable 't'
r = i / 100                                                                             #this line defines r so we can use it as a percentage

interest_type = ("Please enter your interest type '1' (simple) or '2' compund: ")      #this line asks the user which type of interest they are using
if interest_type == "1":                                                                #this line checks if the user selected interest type 1
        interest_type = P *(1 + r *t)                                                   #this line applies the math for simple interest on the users inputs
else:
        interest_type == "2"                                                            #this line checks if the user entered interest type 2
        interest_type = P * pow((1 + r),t)                                              #this line applies the math for compound interest on the users inputs
print("You will be storing " + "R" + str(P) + " with an interest rate of " + str(i) + "%" + " per year for " + str(t) + " year/s, netting you a total of " + "R" + str(interest_type)
#The line above prints out all of the users inputted values and their net       
