"""ESERCIZE LEETCODE"""
class WaterRain:
    def __init__(self, height: list, water = 0): #Inizializing the metod
        self.H = height
        self.W = water

    def HowMuch(self) -> int:
        for rn in range(max(self.H)): #Control for all the water in the container

            """DETERMINATING THE START AND THE END"""
            for x in range(0, len(self.H)):
                print(self.H[x])
                if self.H[x] != 0:
                    start = x
                    break
            for y in reversed(range(len(self.H), 0)):
                print(self.H[y])
                if self.H[y] != 0:
                    end = y
                    break

            """HOW MUCH WATER?"""
            print(start, end)
            try:
                for z in range(start, end -1):
                    print(start, end)
                    if self.H[z + 1] == 0:
                        self.W += 1
            except IndexError:
                break

            self.H = [el - 1 for el in self.H if el != 0]

        return self.W

cicle = True

print("Welcome to my application, here you can recive how much water your container saved")
print("Please, enter the capacity of the container (like: [1 2 0 4 0 1])")

while cicle:

    decision = True
    continuing = True

    while decision:

        try:
            Array = list(map(int, input("> ").split()))
        except ValueError:
            print("Invalid data, Retry: ")
            continue

        for el in Array:
            if el < 0 or el > 10*+5:
                print("Invalid data, Retry: ")
            else:
                decision = False

    Water = WaterRain(Array)
    print("The Array You Insert Was:", *Array)
    print("And the max amount of water that can be store is: ", Water.HowMuch())
    print("You want to continue ? (s/n) ", end = "")

    while continuing:
        val = input()

        if val == "s":
            continuing = False
        elif val == "n":
            continuing = False
            cicle = False
        else:
            print("Invalid data, Retry: ", end = "")
