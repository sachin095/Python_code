import random
def generator_password(len):
    list_of_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$%^&*()" 
    selected_character = random.sample(list_of_char, len)
    print("the random number is",selected_character)
    pass_str="".join(selected_character)
    return pass_str
if __name__ == "__main__":
    while True:
        userSelection = input("do you wish to generate password? \n press Y/y to continue of press N/n to exit ")
        if userSelection == "N" or userSelection == "n":
            print("see you!")
            break
        elif userSelection == "Y" or userSelection == "y":
           len= int(input("enter the length of the password"))
           pass_str = generator_password(len)
           print("password is",pass_str)
           print("")
else:
    print("error")
    print("")
        
    