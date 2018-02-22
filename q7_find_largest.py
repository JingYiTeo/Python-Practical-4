alist = []

def largest(alist):
    if len(alist) == 0:
        return None
    elif len(alist) == 1:
        return Num
    else:
        alist.sort()
        return alist[-1]

#main
items = int(input("Enter number of terms: "))
for i in range(items):
    Num = int(input("Enter an Integer: "))
    alist.append(Num)

print("The largest value is {}".format(largest(alist)))
