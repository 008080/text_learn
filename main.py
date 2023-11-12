#ask for a text input and return it to confirm input
print("Let's get started. When you are done press 'Enter' and then 'STRG + D'. Please paste your text below:")
input_text = []
while True:
    try:
        line = input()
    except EOFError:
        break
    input_text.append(line)


print("----------------------------")
print("This is the text you gave me")
print("----------------------------")
print("\n".join(input_text))
print("----------------------------")

#replace the following letters in the text if they are not the first letter in a sentance with an "_". Maintain line brakes as in the input text.
letter_list_01 = ["a", "e", "i", "o", "u", "ä", "ö", "ü"]
def replace_form_list(input, list):
    new_list = []
    for i in input:
        sub_list = []
        for ii in i:   
            #print(f"This is the i {i}")
            if ii in list:
                sub_list.append("_")
                #print(f"This is the new_list{new_list}")
            else:
                sub_list.append(ii)
                #print(f"This is the new_list{new_list}")
        new_list.append(sub_list)
    return new_list

def join_list_to_string(list):
    new_string = ""
    for i in list:
        new_string = f"{new_string} {''.join(i)}\n"
    return new_string
        

level_01_list = replace_form_list(input_text, letter_list_01)
level_01_string = join_list_to_string(level_01_list)
print("----------------------------")
print("We removed some letters.\nTry to complete the missing letters from memory")
print("----------------------------")
print(level_01_string)
print("----------------------------")