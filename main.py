#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.readlines()

with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    for name in names:
        name = name.strip()
        letter[0] = f"Dear {name},\n"
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_letter:
            output_letter.writelines(letter)


