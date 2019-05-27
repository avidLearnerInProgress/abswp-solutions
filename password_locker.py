import hashlib, sys, pyperclip

email_pwd = 'abc123xyz'
blog_pwd = 'chirag123'
desk_pwd = 'qwerty9696'

passwords = {'email' : str(hashlib.md5(email_pwd.encode())), 
             'blog' : str(hashlib.md5(blog_pwd.encode())),
             'desk' : str(hashlib.md5(desk_pwd.encode()))
            }

def copypwd():
    if len(sys.argv) < 2:
        print('Usage: python password_locker.py [account] - copy account password')
        sys.exit()
    account = sys.argv[1]
    if account in passwords:
        pyperclip.copy(passwords[account])
        print("Password for account: " + account + " copied to clipboard")
    else:
        print("No such account found.!!")
    pastepwd()

def pastepwd():
    print("The password copied for your specific account is :- " + pyperclip.paste())

if __name__ == "__main__":
    copypwd()