def main():
    password = input("Enter your password: ")
    is_valid = False
    for i in range(2):
        if(len(password)<8):
            print("Password too short!!. It  should be atleast 8 characters long.")
            password = input("Please try again: ")
        elif not(has_numeric_character(password)):
            print("Invalid Password!!. It  should atleast have one numeric character.")
            password = input("Please try again: ")
        elif not(has_uppercase_character(password)):
            print("Invalid Password!!. It  should atleast have one uppercase character.")
            password = input("Please try again: ")
        elif not(has_lowercase_character(password)):
            print("Invalid Password!!. It  should atleast have one lowercase character.")
            password = input("Please try again: ")
        elif not(has_special_character(password)):
            print("Invalid Password!!. It  should atleast have one special character.")
            password = input("Please try again: ")
        else:
            is_valid = True
            break
    
    if(is_valid):
        print("Valid Password, it matches all the requirements")
    else:
        print("You have exhausted all your attempts!!")


def has_numeric_character(str):
    for ch in str:
        if (ch>='0' and ch<='9'):
            return True
    return False

def has_uppercase_character(str):
    for ch in str:
        if (ch>='A' and ch<='Z'):
            return True
    return False

def has_lowercase_character(str):
    for ch in str:
        if (ch>='a' and ch<='z'):
            return True
    return False

def has_special_character(str):
    allowed_specials = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    for ch in str:
        if (ch in allowed_specials):
            return True
    return False

if __name__=="__main__":
    main()