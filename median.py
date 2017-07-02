def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

#function to calculate median of three numbers
def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger (b,c)
    if big == b:
        return bigger (a,c)
    else:
        return bigger(a,b)

print median(1,2,3)
