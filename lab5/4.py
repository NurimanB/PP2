import re

pattern = re.compile(r"[A-Z]{1}[a-z]+")
print(pattern.findall("Nuriman Baltabayev is back On Track"))
