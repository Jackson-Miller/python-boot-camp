#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Open the template
with open("./Input/Letters/starting_letter.txt") as data:
    mail_template = data.read()

# Open name list
with open("./Input/Names/invited_names.txt") as data:
    name_list = [line.strip() for line in data]

# For each name in the list create an invitation
for name in name_list:
    file_name = "./Output/ReadyToSend/letter_for_" + name.replace(" ", "_") + ".txt"
    with open(file_name, mode='w') as outfile:
        outfile.write(mail_template.replace("[name]", name))

