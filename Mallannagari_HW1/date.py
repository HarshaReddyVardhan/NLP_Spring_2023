import re

def isValidDate(date):
    # flag = False
    p1 = r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[ -,](?:0[1-9]|[12][0-9]|3[01])[.,]\s(\d{2,4})'
    pattern1 = re.compile(p1)
    matches = pattern1.finditer(str(date))
    for x in matches:
        print('Date Matched with pattern 1 : ',x)
    #     flag = True
    # if flag :
    #     return

    p2 = r'(?:0[1-9]|[12][0-9]|3[01])[- ,](Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[. ,]?\s?(\d{2,4})'
    pattern2 = re.compile(p2)
    matches = pattern2.finditer(str(date))
    for x in matches:
        print('Date Matched with pattern 2 : ',x)
    #     flag = True
    # if flag :
    #     return

    p3 = r'\d{2,4}[-/](?:0[1-9]|[12][0-9]|3[01])[-/](?:0[1-9]|1[012])'
    pattern3 = re.compile(p3)
    matches = pattern3.finditer(str(date))
    for x in matches:
        print('Date Matched with pattern 3 : ',x)
    #     flag = True
    # if flag :
    #     return

    p4 = r'(?:0?[1-9]|[12][0-9]|3[01])[-/ ](?:0?[1-9]|1[012])[-/ ]\d{2,4}'
    pattern4 = re.compile(p4)
    matches = pattern4.finditer(str(date))
    for x in matches:
        print('Date Matched with pattern 4 : ',x)
        