import re
'''
^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$
This regex will enforce these rules:
    At least one upper case English letter, (?=.*?[A-Z])
    At least one lower case English letter, (?=.*?[a-z])
    At least one digit, (?=.*?[0-9])
    At least one special character, (?=.*?[#?!@$%^&*-])
    Minimum eight in length .{8,} (with the anchors)
'''

def strong_password(pwd):
    strength_pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
    return True if re.match(strength_pattern, pwd) else False

if __name__ == "__main__":
    pwd = str(input("Enter password: "))
    if strong_password(pwd):
        print("Strong password")
    else:
        print("Not so strong password")