import re

text = "Hello My name, is. Nuriman, but you can call me Nurik"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)