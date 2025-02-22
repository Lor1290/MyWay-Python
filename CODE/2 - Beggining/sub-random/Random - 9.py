import curses
import time
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 20, "pazzpanino")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
time.sleep(1000)
