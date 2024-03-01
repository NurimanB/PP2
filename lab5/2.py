import re

def search_pattern(string):
    p = r'ab{2,3}'
    if re.match(p, string):
        return True
    else:
        return False

string = str(input())
print(search_pattern(string))