def flatten(x):
    y = []
    for z in x:
        if type(z) is list:
            y.extend(flatten(z))
        else:
            y.append(z)
    return y

def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5
    while n >= 0:
        a,b,c,d,e =  b, c, d, e, a-c+e
        n -= 1
    return a

def mystery2(n):
    if n<10:
        return n
    total = (n % 10) + mystery2(n//10)
    return total

def collatz_sequence(i):
    print(i,end = " ")
    if i==1:
        print()
        return
    if i % 2 == 0:
        collatz_sequence(i//2)
    else:
        collatz_sequence(3*i+1)



