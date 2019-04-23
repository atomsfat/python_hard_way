import curses
import random


def fill_screen(stdscr):
    h, w = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)

    caracol = 128012  # caracol
    panda = 128060  # panda

    for x in range(w-2):
        for y in range(h):
            animal = chr(random.randint(caracol, panda))
            stdscr.addstr(y, x, animal)
    stdscr.getch()


def emoji_screen():
    curses.wrapper(fill_screen)
