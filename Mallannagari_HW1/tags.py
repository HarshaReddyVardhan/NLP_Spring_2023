import re

def isTagPresent(line):
    pattern = re.compile(r'<(\w+)\s*.*?[^\/]>')
    matches = pattern.finditer(line)
    for x in matches :
        print("Found a Line with tags : ",x)
        # print("Found a Line with tags : ",x.string)
        return True
    return False