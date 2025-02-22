import curses
import time
from curses import wrapper

def main(stdscr):
    def matrice_ad_aspirale(num):
        lista_num = []
        num_alla_seconda = num**2
               
        for i in range(num**2):
            lista_num.append(num_alla_seconda)
            num_alla_seconda -= 1
        
        lista_num.sort()
        
        
        Y = 2
        X = 2
        Z = 0
        P = 0

        while (num - Z) != 0:   
            for A in range(num - Z):
                try:
                    stdscr.addstr(Y, X, str(lista_num[P]))
                    stdscr.refresh()
                    time.sleep(0.5)
                    Y += 1
                    P += 1
                except curses.error:
                    pass
                
            Z += 1
            
            for B in range(num - Z):
                try:
                    stdscr.addstr(Y, X, str(lista_num[P]))
                    stdscr.refresh()
                    time.sleep(0.5)
                    X += 1
                    P += 1
                except curses.error:
                    pass

            for C in range(num - Z):
                try:
                    stdscr.addstr(Y, X, str(lista_num[P]))
                    stdscr.refresh()
                    time.sleep(0.5)
                    Y -= 1
                    P += 1
                except curses.error:
                    pass
            Z += 1

            for D in range(num - Z):
                try:
                    stdscr.addstr(Y, X, str(lista_num[P]))
                    stdscr.refresh()
                    time.sleep(0.5)
                    X -= 1
                    P += 1
                except curses.error:
                    pass
            
    while True:
        stdscr.addstr("decidi un numero di cui avere la matrice ad aspirale: ")
        curses.echo()
        _num_ = stdscr.getstr()
        matrice_ad_aspirale(int(_num_))
        
wrapper(main)
