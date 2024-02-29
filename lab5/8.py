import re

text = "MyNameIsNurik"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)