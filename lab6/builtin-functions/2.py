text = str(input())
low, up = 0, 0
for char in text:
    if(char.islower()):
        low += 1
    else:
        up +=1

print(low, up)