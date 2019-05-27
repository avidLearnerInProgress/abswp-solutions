import pyperclip
copied_txt = ""

def copy_from_clipboard():
    global copied_txt 
    copied_txt = pyperclip.paste() 

def edit_copied_txt():
    l_copied_txt = ["* " + x for x in copied_txt.split('\r\n')]
    to_paste = '\r\n'. join(l_copied_txt)
    print(to_paste)
    pyperclip.copy(to_paste)
    print("Pasted on clipboard!!")

if __name__ == "__main__":
    copy_from_clipboard()
    edit_copied_txt()