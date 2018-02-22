##def sum_digits(n):
##    conv = str(n)
##    a = [conv]
##    if len(conv) == 0:
##        print("Invalid")
##    elif len(conv) == 1:
##        return n
##    else:
##        return a[0] + sum_digits(n)
##
##print(sum_digits(233))


def sum_digits(n):
    add = 0
    while n:
        add += n % 10
        n //= 10
    return add
#main
a = int(input("Enter an integer: "))
print("The sum of digits is:", sum_digits(a))
