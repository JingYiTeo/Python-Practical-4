#recursive function

def m(i):
    if i == 1:
        return 1/((2*1)+1)
    else:
        return (i/((2*i)+1)) + m(i-1)
#main
a = int(input("Enter the number of terms: "))
print("The sum series is {:.3f}".format(m(a)))
