import re

pn_regex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
n = pn_regex.search('My phone number is :- 415-555-222')
area_cd, number = n.groups()
print(area_cd, number)

pn1_regex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{3})')
n1 = pn1_regex.search('My phone number is : (415) 555-222')
print(n1.groups())

pn2_regex = re.compile(r'C(S|None|None|None)')
n2 = pn2_regex.search('CS ABCD')
print(n2.group())     

pn3_regex = re.compile(r'C(K)?S')
n3 = pn3_regex.search('CS')
n4 = pn3_regex.search('CKS')
print(n3.group())     
print(n4.group())

pn5_regex = re.compile(r'C(K)*S') # similarly +
n5 = pn5_regex.search('CKKS')
print(n5.group())

pn6_regex = re.compile(r'(CS){3}')
n6 = pn6_regex.search('CSCSCSCSCS')
print(n6.group())


#greedy - longest
#non-greedy - curly brackets - shortest

greedyCS = re.compile(r'(CS){1,6}') #bydefault matches 6 
n7 = greedyCS.search('CSCSCSCSCSCSCS')
print(n7.group())

nongreedyCS = re.compile(r'(CS){1,6}?') #bydefault matches 1
n8 = nongreedyCS.search('CSCSCSCSCSCSCS')
print(n8.group())

pn_regex = re.compile(r'(\d{3}-\d{3}-\d{4})')
n9 = pn_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(n9)   

#\d -> digit \D ~ digit \w - word \W ~ word \s - space \S ~ space 
# carrot ^ -> begins with
# dollars $ -> ends with 
# \d$ -> ends with numeric
# \d+$ -> starts and ends with numeric
# Carrot cost Dollars
# wildcard -> (.*) -> matches anything --> gredymode
# (?.*) -> any all

'''
    The ? matches zero or one of the preceding group.

    The * matches zero or more of the preceding group.

    The + matches one or more of the preceding group.

    The {n} matches exactly n of the preceding group.

    The {n,} matches n or more of the preceding group.

    The {,m} matches 0 to m of the preceding group.

    The {n,m} matches at least n and at most m of the preceding group.

    {n,m}? or *? or +? performs a nongreedy match of the preceding group.

    ^spam means the string must begin with spam.

    spam$ means the string must end with spam.

    The . matches any character, except newline characters.

    \d, \w, and \s match a digit, word, or space character, respectively.

    \D, \W, and \S match anything except a digit, word, or space character, respectively.

    [abc] matches any character between the brackets (such as a, b, or c).

    [^abc] matches any character that isn’t between the brackets.
'''

