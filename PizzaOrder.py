print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size of pizza would you like? S, M, or L?\n")
add_pepperoni = input("Would you like to add pepperoni? Y or N\n")
extra_cheese = input("Would you like extra cheese? Y or N\n")

bill: 0

if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
if size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
if size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")