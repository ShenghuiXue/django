import re

patterns = ["term1", "term2"]

text = "this is the string term 1 and not other!"

for pattern in patterns:
    if re.search(pattern, text):
        print (pattern)
    else :
        print (pattern)
