import re

def isValidCurrency(s):
    # pattern = re.compile(r'[-+]?([$]|([U][S][D]))(\d{1,3}[,]?)*([.]\d{1,2})?[MKB]?')
    pattern = re.compile(r'[-+]?([$]|([U][S][D]))\d{1,3}(?:,?\d)*(?:\.\d{1,2})?[MKB]?')
    matches = pattern.finditer(str(s))
    for x in matches :
        print("Found Valid Currency : ",x)