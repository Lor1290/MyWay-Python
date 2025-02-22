def butterfly(base: int):
    number = [str(x) for x in range(1, base+1)]
    space = base*2+1

    for x in range(base+1):
        print("".join(number[0: x]) + " " * space + "".join(number[0: x]))
        space -= 2

    space += 2
    print()

    for x in range(base, 0, -1):
        print("".join(number[:x]) + " " * space + "".join(number[:x]))
        space += 2
        
def hill(base: int):
    for x in range(1, base+1):
        print(" "*(base - x) + "* " * x)

def rock(base: int):
    number = [str(x) for x in range(1, base+1)]
    
    for x in range(1, base+1):
        print("".join(number[0:x]))
    for x in range(base+1):
        print(" " * (x) + "".join(number[0:(base-x)]))

def piramid(base: int, num: str):
    space = 0
    time = int(num)
    
    for x in range(time):
        print(" " * space + (num+" ")* (base - space))
        space += 2
        num = str(int(num)-1)
        
    space -= 2
    num = str(int(num)+1)
    
    for x in range(1, time+1):
        print(" " * space + (num+" ")*(base - space))
        space -= 2
        num = str(int(num)+1)

piramid(9, "5")

