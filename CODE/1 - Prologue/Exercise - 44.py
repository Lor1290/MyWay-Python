import time
import re

class Func:
    def slow_print(word: str, tmp: int):
        for letter in word:
            print(letter, end = "")
            time.sleep(tmp)
        print()
    def slow_prints(msg: str, tmp: int):
        for word in msg:
            for letter in word:
                print(letter, end = "")
                time.sleep(tmp)
            print()


class Main:
    def diamond(base: str):
        Dict: dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, 
                     "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                     "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
                     "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                     "u": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    
        time: int = Dict[base]
        for x in range(time):
            