with open("Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
name_list_striped = []
for i in name_list:
    name_list_striped.append(i.strip('\n'))

for i in name_list_striped:
    with open(f"Output/ReadyToSend/letter_for_{i}.txt","w") as ready_letter:
        ready_letter.write(letter_text.replace("[name]", i))