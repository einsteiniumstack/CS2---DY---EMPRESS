# Electricity Bill Calculator
RATE = 12.90

# Validate customer name
while True:
    name = input("Enter customer name: ")

    if name.strip() != "":
        break
    else:
        print("Name cannot be empty. Please try again.")
    
# Validate previous reading
while True:
    previous = float(input("Enter previous meter reading: "))
    
    if 0 <= float(previous):
        previous = float(previous)
        break
    else:
        print("Invalid reading. Enter a number at least 0.")
        

# Validate current reading
while True:
    current = float(input("Enter current meter reading: "))

    if previous <= float(current):
        current = float(current)
        break
    else:
        print("Invalid reading. Enter a number at least previous reading.")
        
consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
