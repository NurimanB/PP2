from itertools import permutations

def perms(string):
    perm_list = perms(string)
    
    for perm in perm_list:
        print(''.join(perm))

input_str = input("Enter a string: ")
perms(input_str)

