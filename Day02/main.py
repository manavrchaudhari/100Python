initial_bill = float(input("What was the total bill?\n₹"))
tip = int(input("How much would you like to tip?\n"))
people = int(input("How many people are there?\n"))

tip_percent = tip / 100
tip_amount = initial_bill * tip_percent
total_bill = initial_bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ₹{final_amount}")