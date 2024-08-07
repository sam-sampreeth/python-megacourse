date = input("Enter today's date: ")
mood = int(input("Enter today's mood from 1 to 10: "))
thoughts = input("Let your thoughts flow:\n")

with open(f"./subfiles/journal/{date}.txt", "w") as file:
    file.write(f"Today's mood: {mood}")
    file.write(2 * "\n")
    file.write("Today's thoughts: \n" + thoughts + "\n")
