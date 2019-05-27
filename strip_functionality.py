import re
def strip_func(srt):
    if str is not None:
        return re.sub(r"\s+", "", srt)

if __name__ == "__main__":
    print(strip_func("            ASDZXC123               "))