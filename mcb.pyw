import shelve, pyperclip, sys
clipboard_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    clipboard_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2: 
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(clipboard_shelf.keys())))
    elif sys.argv[1] in clipboard_shelf:
        pyperclip.copy(clipboard_shelf[sys.argv[1]])
clipboard_shelf.close()