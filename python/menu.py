import curses

menux=[]
menuy=[]
menutext=[]
activefg=curses.COLOR_WHITE
activebg=curses.COLOR_GREEN
inactivefg=curses.COLOR_BLUE
inactivebg=curses.COLOR_WHITE

def additem(x, y, text):
    menux.append(x)
    menuy.append(y)
    menutext.append(text)

def removeitem(n):
    del menux[n-1]
    del menuy[n-1]
    del menutext[n-1]

def setcolor(afg, abg, ifg, ibg):
    global activefg,  activebg,  inactivefg,  inactivebg
    activefg=afg
    activebg=abg
    inactivefg=ifg
    inactivebg=ibg


def reset():
    del menux[:]
    del menuy[:]
    del menutext[:]

def runmenu_inside(win,  active = 1, acceptesc=False):
    key="a"
    curses.init_pair(1, activefg, activebg)
    curses.init_pair(2, inactivefg, inactivebg)
    curses.curs_set(0)

    while key != 10:
        for i in range(len(menutext)):
            win.move(menuy[i], menux[i])
            if i+1 == active:
                cor = 1
            else:
                cor = 2
            win.addstr("", curses.color_pair(cor))
            win.addstr(menutext[i], curses.color_pair(cor))
            win.addstr("", curses.color_pair(cor))
        key = win.getch()
        if key ==  curses.KEY_UP or key == curses.KEY_LEFT:
            active = active - 1
        if key == curses.KEY_RIGHT or key == curses.KEY_DOWN:
            active = active + 1
        if active <= 0:
            active = len(menutext)
        if active > len(menutext):
            active = 1

        if key == 27 and acceptesc:
            active = 0
            break
    curses.curs_set(1)
    return active

def runmenu(active = 1, esc = False):
    return curses.wrapper(runmenu_inside,active, esc)
