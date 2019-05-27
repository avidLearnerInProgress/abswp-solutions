import os, re

lib = open('madlibs.txt', 'w+')
string = lib.read()
replaced = 0
madlib_regex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = madlib_regex.findall(string)
for found in matches:
    sub = input('Enter a ' + found + ': ')
    string = string.replace(found, sub, 1)
    print(string)