# define the function with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print the line including first argument
	print(f"You have {cheese_count} cheeses!")
	# print next line including second argument
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	# print other stuff 
	print("Man, that's enough for a party!")
	print("Get a blanket. \n")

# prints a new line
print("We can just give the function numbers directly: ")
# prints the 4 lines in the functions with arguments 20 and 30
cheese_and_crackers(20, 30)

# prints a new line
print("OR, we can use variables from our script")
# dfine a  variable
amount_of_cheese = 10
# dfine another  variable
amount_of_crackers = 50

# call the function and print the 4 lines in the function 
# with the new variables defined
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a new line
print("We can even do math inside too:")
# call the function and print the result of addition in each of the
# two arguments given here
cheese_and_crackers(10 + 20, 5 + 6)

# print a new line
print("And we can combine the two, variables and math:")
# calls the function, prints the 4 lines defined in the function with
# the addition of variable + in given as arguments here
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 1000)



