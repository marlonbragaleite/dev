import curses

def main(win):
    #win.nodelay(True)
    curses.init_pair(1,  curses.COLOR_RED,  curses.COLOR_WHITE)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
            key = win.getkey()
            win.clear()
            win.addstr(" Detected key:", curses.color_pair(1))
            win.addstr(str(key))
            if key == "\n":
                break
        except Exception as e:
            pass
curses.wrapper(main)
