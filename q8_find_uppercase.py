def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    elif ord('A') <= ord(str[0]) <= ord('Z'):
        return 1 + find_num_uppercase(str[1:])
    else:
        return 0 + find_num_uppercase(str[1:])

#main
Words = str(input("Enter a phrase with upper and lower cases: "))
print(find_num_uppercase(Words))
