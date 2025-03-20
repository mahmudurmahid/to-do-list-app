feet_inches = input("Enter the number of feet and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = (feet + inches / 12) * 0.3048
    return meters


result = (convert(feet_inches))

if result < 1:
    print("The child is too small to use the ride.")
else:
    print("The child is tall enough to use the ride.")
