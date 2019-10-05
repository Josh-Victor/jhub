user_weight = float(input("Please enter your weight (in kilograms): "))
user_height = float(input("Please enter your height (in metres): "))
body_mass_index = user_weight / (user_height * user_height)
body_type = 0

if body_mass_index >= 30:
    print("Oh no! You are obese, maybe you should go see a gym!")
    body_type = "obese"
elif body_mass_index >= 25:
          print("You are overweight! Maybe you shuld pay the dietitian a visit!")
          body_type = "overweight"
elif body_mass_index >= 18.5:
          print("Congratulations! Your Body Mass Index is normal.")
          body_type = "normal"
else:
    body_mass_index < 18.5
    print("Oh no! You are underweight, try eating something!")
    body_type = "underweight"

print("You are " + body_type + " and your Body Mass Index is " + str(body_mass_index))
