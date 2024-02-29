import re

def search_pattern(string):
    p = r'ab{2,3}' #ищем паттерн где после 'a' идет 2 или 3 'b'
    if re.match(p, string):
        return True
    else:
        return False

string = str(input())
print(search_pattern(string))