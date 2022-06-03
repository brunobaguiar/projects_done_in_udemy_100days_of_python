#TODO: Create a letter using starting_letter.txt 

with open("./Input/Names/invited_names.txt") as invited:
    invited_list = invited.readlines()
for n in range(len(invited_list)):
    invited_list[n] = invited_list[n].strip()
    with open("./Input/Letters/starting_letter.txt") as file:
        contents = file.read()
        new_name = contents.replace("[name]", invited_list[n])
    with open(f"./Output/ReadyToSend/letter_for_{invited_list[n]}.txt", mode="w") as letter:
        new_letter = letter.write(new_name)