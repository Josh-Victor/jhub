start_year = int(input("Please enter the year you would like to start with: "))
number_of_years = int(input("Please enter the number of years you want to check: "))


for i in range (start_year, start_year + number_of_years):
    if i % 4 ==0:
        print (i , " IS a leap year")
    else:
        print(i , " is NOT a leap year" )
        
