product_1 = input("Please enter the name of a product: ")
product_1_price = float(input("Please enter the exact price of the product in your previous entry: "))
product_2 = input("Please enter the name of another product: ")
product_2_price = float(input("Please enter the exact price of the product in your previous entry: "))
product_3 = input("Please enter the name of another product: ")
product_3_price = float(input("Please enter the exact price of the product in your revious entry: "))
#we have reqeusted the customer to enter the name and price of three produccts

total_price = product_1_price + product_2_price + product_3_price
#we simply calculate the total price of the products entered by the customer.
average_price = (product_1_price + product_2_price + product_3_price) / 3
#we calculate the total price of the products entered by the customer and divide by the total number of products bought to find the average price of the products.

print("The Total of " + product_1 + ", " + product_2 + ", " + "and " + product_3 + " is " + "R" + str(total_price) + " and the average price of the products is " + str(average_price))
#we print out the message to the customer but in order for this to worker we need to cast the float values back into strings in order to
#to preserve the values as floats in case we need to do further calculations with the values entered by the user.

