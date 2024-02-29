import re

def S2C(text):
    words = text.split('_')
    CamelStr= words[0]
    for char in words[1:]:
        CamelStr += char.capitalize()
    return CamelStr

text = "my_snake_case_string"
print(S2C(text))


    
