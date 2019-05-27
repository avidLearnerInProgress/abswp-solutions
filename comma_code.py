def comma_code(l = ['a', 'b', 'c', 'd']):
    x = ''
    if len(l) == 0:
        x += l[0]
        print(x)
        return
    else:
        for y in range(0, len(l) - 1):
            x += l[y]
            if y + 1 == len(l) - 1:
                pass
            else:
                x += ", "
        x += " and "
        x += l[-1]

        print(x) 


if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats']
    comma_code(spam)
