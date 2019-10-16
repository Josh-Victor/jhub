provincial_colours = False
provincial_half_colours = False
provincial_scroll = False
provincial_certificate = False
no_award =  False

swimming_time = int(input("How many minutes did you take to complete the swimming segment of the triathlon?: "))
cycling_time = int(input("How many minutes did you take to complete the cyling segment of the triathlon?: "))
running_time = int(input("How many minutes did you take to complete the running segment of the triathlon?: "))
participant_position = input("What position did you place in the triathlon?: ")

                   

total_triathlon_time = swimming_time + cycling_time + running_time

if total_triathlon_time <= 100:
    participant_position == "1"
    provincial_colours = True
elif total_triathlon_time <= 110:
    participant_position == "1" or "2"
    provincial_half_colours = True
elif total_triathlon_time <= 115:
    provincial_scroll = True
elif total_triathlon_time >= 120:
    provincial_certificate = True
else:
    total_triathlon_time > 120
    no_award = True


if provincial_colours == True:
    print("Congratulations you have been awarded with Provincial Colours!")
elif provincial_half_colours == True:
    print("Congratulations you have been awarded Provincial Half Colours!")
elif provincial_scroll == True:
    print("Congratulations you have been awarded with a Provincial Scroll!")
elif provincial_certificate == True:
    print("Congratulations you have been awarded with a Provincial Certficate!")
if no_award == True:
    print("Sorry, you have not qualified for an award!")



  
                   
