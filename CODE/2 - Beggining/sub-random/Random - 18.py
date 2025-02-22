def Stella(length: int):
    count: int = 1
    for x in range(1, length+1):
        print(" "*(length + (length-x)) + "*"*count)
        count += 2

    count = (length*4)-1
    for x in range(length):
        print(" "*x + "*"*count)
        count -= 2

    count = 0
    for x in range(length+1):
        print(" "*(length-x) + "*"*(length-x) + " "*count + "*"*(length-x))
        count += 4
        
Stella(7)     
