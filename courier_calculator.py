air_courier = float(0.36) 
freight_courier = float(0.25) 
full_insurance = 50
limited_insurance = 25
gift = 15
not_gift = 0
priority_delivery = 100
standard_delivery = 20


########################################################################################################################################
package_price = int(input("What is the price of the package that you want to send?: "))
########################################################################################################################################
courier_choice = input("Would you like to deliver your package through air or freight? (please answer 'air' or 'freight': ")
if courier_choice == "air":
    delivery_distance = int(input("whats is the total distance (in Kilometres) that the parcel needs to travel?: "))
    courier_choice = float(delivery_distance) * float(air_courier)
else: 
        courier_choice == "freight"
        delivery_distance = int(input("whats is the total distance (in Kilometres) that the parcel needs to travel?: "))
        courier_choice = float(delivery_distance) * float(freight_courier)
########################################################################################################################################
insurance_type = input("We have two choices of insurance, please answer 'full' or 'limited': ")
if insurance_type == "full":
    insurance_type = full_insurance
else:    
        insurance_type == "limited"
        insurance_type = limited_insurance
########################################################################################################################################        
gift_type = input("Would you like to send this parcel as a gift? Please answer 'yes' or 'no': ")
if gift_type == "yes":
    gift_type = gift
else: 
        gift_type == "no"
        gift_type = not_gift
########################################################################################################################################
delivery_type = input("Whould you like to use our priority or standard delivery? Please answer 'priority' or 'standard': ")
if delivery_type == "priority":
    delivery_type = priority_delivery

else:
    delivery_type == "standard"
    delivery_type = standard_delivery


total_cost = package_price + float(courier_choice) + insurance_type + gift_type + delivery_type
print("The total price to deliver your parcel comes to the Total Of: " + "R" + str(total_cost))
