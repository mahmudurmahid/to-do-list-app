date = input("Enter today's date: ")
mood = input("Rate your mood from 1 to 10: ")
thoughts = input("Write your thoughts:\n")

with open(f"..files/experiments_bonuses/journal/{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(thoughts)