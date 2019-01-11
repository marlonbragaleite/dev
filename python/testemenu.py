#!/usr/bin/python3.5
import menu
import curses

menu.additem(10,10,"alfa")
menu.additem(15,15,"bravo")
menu.additem(22,22,"charlie")

menu.setcolor(curses.COLOR_RED,  curses.COLOR_YELLOW,  curses.COLOR_CYAN,  curses.COLOR_BLUE)

print(menu.runmenu(2,True))
