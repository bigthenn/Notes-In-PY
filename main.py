# Open the Notes.txt file in append mode
with open("Notes.txt", "a") as file:
    # Prompt the user for input
    note = input("Enter your note: ")

    # Write the input to the file
    file.write(note + "\n")
