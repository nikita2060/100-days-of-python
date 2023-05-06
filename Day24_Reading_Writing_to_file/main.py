PLACEHOLDER = "[name]"

with open("names.txt") as namefile:
    name_list = namefile.readlines()

with open("letter.txt") as letterfile:
    letter_content = letterfile.read()
    for name in name_list:
        stripped_name = name.strip()
        final_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"letter_to_{stripped_name}.txt", "w") as file:
            file.write(final_letter)
