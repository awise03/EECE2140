total_gallons = total_miles = 0
while True:
    gallons_used = float(input("Enter the number of gallon used (any negative number to end): "))
    if gallons_used < 0: break
    miles_driven = float(input("Enter the number of miles driven: "))
    print(f"The miles/gallon for this tank was {miles_driven/gallons_used}.")
    total_gallons += gallons_used
    total_miles += miles_driven

if total_gallons < 0: print("Not enough information to compute the total")
else: print(f"The overall average miles/gallon for the above tankfulls was {total_miles/total_gallons}.")
