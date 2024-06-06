#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to splitwise!\n")
total_bill = float(input("Enter total bill amount (Rs.): Rs."))
no_of_people = int(input("Enter number of people : "))
tip = int(input("How much tip you want to give 'Rs.50', 'Rs.100', 'Rs.200' : Rs. " ))
bill_for_each = round(((total_bill +tip) / no_of_people),2)
print(f"Each person has to contribute Rs. {bill_for_each}")
