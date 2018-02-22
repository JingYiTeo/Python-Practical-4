#recursive function

def reverse(n):
    Num = 0
    while n > 0:
        Num *= 10
        Num += n % 10
        n //= 10
    return Num
#main
Number = int(input("Enter an integer: "))
print("The reverse of {} is {}.".format(Number, reverse(Number)))
