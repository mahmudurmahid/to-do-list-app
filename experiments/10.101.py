try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That is a square. Please enter a rectangle.")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a valid number.")
