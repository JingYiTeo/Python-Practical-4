
def count_letter(str, ch):
    if (len(str)) == 0:
        return 0
    elif str[0] == ch:
        return 1 + count_letter(str[1:], ch)
    else:
        return count_letter(str[1:], ch)
#main
str = input("Enter a phrase: ")
ch  = input("Enter a letter you want to track: ")
print(count_letter(str, ch))
