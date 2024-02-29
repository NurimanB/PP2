import re

def ab(str):
    pattern = r'ab*'
    if re.match(pattern, str):
        return True
    else:
        return False
    
str = str(input())
print(ab(str))