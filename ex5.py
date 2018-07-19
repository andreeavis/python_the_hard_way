name = "Zara Zaraza"
age = 35 #not a lie
height = 74 # inches
weight = 180 #pounds
eyes = 'Brown'
teeth = 'White'
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get{total}.")

# Try to write some variables that convert the inches and pounds to centimeters and kilograms.
# Do not just type in the measurements. Work out the math in Python.
inches_to_cm = height * 2.54
pounds_to_kg = weight * 0.453596

print(f"His weight  is {pounds_to_kg} kg.")
print(f"His height is {inches_to_cm} cm.")
