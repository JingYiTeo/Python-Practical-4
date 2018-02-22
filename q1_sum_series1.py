#recurrsion
def m(i):
    if i == 1:
        return 1
    else:
        return (1/i) + (m(i-1))

#main

a = int(input("Enter the number of terms: "))
print("The sum series is {:.2f}".format(m(a)))
