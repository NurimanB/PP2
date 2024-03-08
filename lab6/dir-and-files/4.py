import os

f = open(r"D:\VsCode\python\lab6\dir-and-files\4.txt")
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")