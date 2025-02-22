def LetteraX(n):
    spazi = 1
    for x in range(1, n):
        print(" " * x, "*")
    for x in range(n, spazi, -1):
        print(" "* x, "*")

LetteraX(11)