# Create names.txt file manually before running, with each name on a new line.

with open("names.txt", mode="r") as names_file:
    # .splitlines() automatically removes the newline \n characters at the end of each line
    names_list = names_file.read().splitlines()

for name in names_list:
    # Generate a personalized txt file for each name
    with open(f"{name}_invitation.txt", mode="w+") as letter:
        letter.write(f"Hi {name}!\nCome to my birthday party!")
        
print(f"Successfully generated {len(names_list)} invitations.")
