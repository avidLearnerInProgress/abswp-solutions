import shutil, os, re

def datePattern():
    date_pattern = re.compile(r"""
        ^(.*?) #all before date
        ((0|1)?\d)- #one or two digits for month
        ((0|1|2|3)?\d)- #one or two digits for day
        (19|20\d\d) #four digits for year
        (.*?)$ #all after date
        """, re.VERBOSE)

    for file in os.listdir('.'):
        pattern = date_pattern.search(file)
        if pattern is None:
            continue
        before_pat = pattern.group(1)
        month_pat = pattern.group(2)
        day_pat = pattern.group(3)
        year_pat = pattern.group(4)
        after_pat = pattern.group(5)

        euro_name = before_pat + day_pat + '-' + month_pat + '-' + year_pat + after_pat
        abs_dir = os.path.abspath('.')
        file = os.path.join(abs_dir, file)
        euro_name = os.path.join(abs_dir, euro_name)

        print("Renaming %s to %s..:" %(file, euro_name))
        shutil.move(file, euro_name)

if __name__ == "__main__":
    datePattern()