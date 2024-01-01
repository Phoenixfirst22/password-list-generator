import random

#https://github.com/Phoenixfirst22
print("made by Phoenixfirst22\nhttps://github.com/Phoenixfirst22\nleave blank if you don't know\n")


#input
requirements = {"first name": "w1", "last name": "w2", "birthday year": "w3", "birthday month": "w4", "birthday day": "w5", "phone number": "w6", "pet name": "w7", "favorite sport": "w8", "favorite sports club": "w9", "first name of boyfriend/girlfriend": "w10"}

requirements_copy = requirements.copy()

for key, value in requirements.items():
    inp = input(key + ": ")
    if inp is None or inp == "":
        requirements_copy.pop(key)
    else:
        requirements_copy[key] = inp





add = "..."
x = 11



while add != "":
    add = input("add more or leave blank to continue: ")
    requirements_copy.update({f"addByUser{x}": add})
    x = x + 1
requirements_copy.popitem()
list1 = list(requirements_copy.values())

print("generating...")


#make passwords
def changeFirstLetter(word):
    abc = "qwertzuiopasdfghjklyxcvbnm"
    ABC = abc.upper()
    abc = list(abc)
    ABC = list(ABC)
    word = list(word)
    if word[0] in abc or word[0] in ABC:
        if word[0].islower():
            word[0] = word[0].upper()
            word = "".join(word)
        else:
            word[0] = word[0].lower()
            word = "".join(word)
    return word


def check_if_list(objekt):
    return isinstance(objekt, list)



passwords = []
def makePassword(list):

    count = int(0)
    while count != 100000:
        k = random.choice(list) + random.choice(list)
        if k in passwords:
            count = count + 1
        else:
            passwords.append(k)
    return passwords



makePassword(list1)
list2 = [changeFirstLetter(item) for item in passwords if changeFirstLetter(item) != item]


safetxt = "passwords.txt"
def addToTxt(list_):
    for item in list_:
        with open(safetxt, "a") as f:
            f.write("".join(item) + "\n")



list3 = []
def addNumbers(list_):
    numbers = ["123", "12345", "54321", "321"]
    global list3
    for element in list_:
        if check_if_list(element):
            element = "".join(element)
        for item in numbers:
            list3.append(item + str(element))
            list3.append(str(element) + item)
        list3.append(f"12{str(element)}34")
        list3.append(f"123{str(element)}456")
        list3.append(f"43{str(element)}21")
        list3.append(f"654{str(element)}321")
    return list3



ipasswords = []
def addSpecialCharacter(passwords):
    global ipasswords
    for password in passwords:
        if check_if_list(password):
            password = "".join(password)

        ipasswords.append(f"{password}!")
        ipasswords.append(f"!{password}")
        ipasswords.append(f"{password}?")
        ipasswords.append(f"?{password}")
        ipasswords.append(f"{password}!?")
        ipasswords.append(f"{password}?!")
    return ipasswords



passwords.extend(list2)




addSpecialCharacter(passwords)


passwords.extend(ipasswords)

addNumbers(passwords)

addSpecialCharacter(list3)

list3.extend(ipasswords)

passwords.extend(list3)



def cleanDoublePasswords(passwords):
    unique_passwords = set()
    duplicate_passwords = set()
    cleaned_passwords = []

    for password_list in passwords:
        password_tuple = tuple(password_list)

        if password_tuple in unique_passwords:
            duplicate_passwords.add(password_tuple)
        else:
            unique_passwords.add(password_tuple)
            cleaned_passwords.append(password_list)

    return cleaned_passwords

passwords = cleanDoublePasswords(passwords)



#delete short passwords
passwords = [item for item in passwords if len(item) >= 4]

addToTxt(passwords)

print(f"\n{len(passwords)} passwords saved in {safetxt}")


