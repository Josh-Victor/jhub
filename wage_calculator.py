sales_person = False
manager = False
gross_sales = 0
hours_worked = 0

job_role = input("Are you a 1(Salesperson) or 2(Manager)?: " )

if job_role == "1":
    sales_person = True
    sales_person == True
    gross_sales = float(input("What has been the gross value of products sold this month?: "))
    job_role = gross_sales * 8 / 100 + 2000
    
if job_role == "2":
    manager = True
    manager == True
    hours_worked = int(input("How many hours have you worked this month?: "))
    job_role = hours_worked * 40 

      


print("Your total wage for the month was " + "R" + str(job_role))
                 
                 
