while 1 :
    x = int(input("enter a number: "))
    i = x
    z = 0 
    while i > 0:
        r = i % 10
        i //= 10
        z = z*10 + r
    if z == x:
        print("Ok")
    else:
        print("NOT Ok")
