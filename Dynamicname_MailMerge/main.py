PLACEHOLDER="[name]"



with open("./Input/Names/invited_names.txt") as name:
    names_list=name.readlines()
    print(names_list)
with open("./Input/Letters/starting_letter.txt") as letter:
    content=letter.read()
    for name in names_list:
        stripped_name=name.strip()
        new_letter=content.replace( PLACEHOLDER,stripped_name)
        with open(f"./output/ReadyToSend/letter for{stripped_name}.docx","w") as completed_letter:
            completed_letter.write(new_letter)