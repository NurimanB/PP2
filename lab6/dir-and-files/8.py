import os
p=(r"D:\VsCode\python\lab6\dir-and-files/delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")