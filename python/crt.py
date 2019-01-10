ansi_esc = "\033["

def ansi_up(n):
    print (ansi_esc+str(n)+"A",end='',flush=True)
    
def ansi_down(n):
    print (ansi_esc+str(n)+"B",end='',flush=True)
    
def ansi_right(n):
    print (ansi_esc+str(n)+"C",end='',flush=True)
    
def ansi_left(n):
    print (ansi_esc+str(n)+"D",end='',flush=True)
    
def gotoxy(x, y):
    print(ansi_esc+str(x)+";"+str(y)+"H",end='',flush=True)
    
def clrscr():
    print(ansi_esc+"2J",end='',flush=True)
    
def ansi_scrollup(n):
    print(ansi_esc+str(n)+"S",end='',flush=True)
    
def ansi_scrolldown(n):
    print(ansi_esc+str(n)+"T",end='',flush=True)
        
def ansi_reset():
    print(ansi_esc+"0m",end='',flush=True)
    
def ansi_bold(n=True):
    """
    True = Bold, 2 = Faint, False = Regular
    """
    if n==True:
        print(ansi_esc+"1m",end='',flush=True)
    elif n==2:
        print(ansi_esc+"2m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"22m",end='',flush=True)

def ansi_italic(n=True):
    """
    True = Italic, 2 = Fraktur, False = No Italic
    """
    if n == True:
        print(ansi_esc+"3m",end='',flush=True)
    elif n==2:
        print(ansi_esc+"20m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"23m",end='',flush=True)

def ansi_underline(n=True):
    """
    True = Underline, 2 = Doubly Underline, False = No Underline
    """
    if n==True:
        print(ansi_esc+"4m",end='',flush=True)
    elif n==2:
        print(ansi_esc+"21m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"24m",end='',flush=True)

def ansi_blink(n=True):
    """
    True = Slow Blink, 2 = Fast Blink, False = No Blink
    """
    if n==True:
        print(ansi_esc+"5m",end='',flush=True)
    elif n==2:
        print(ansi_esc+"6m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"25m",end='',flush=True)
        
def ansi_reverse(n=True):
    if n==True:
        print(ansi_esc+"7m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"27m",end='',flush=True)
        
def ansi_conceal(n=True):
    if n==True:
        print(ansi_esc+"8m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"28m",end='',flush=True)

def ansi_crossed(n=True):
    if n==True:
        print(ansi_esc+"9m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"29m",end='',flush=True)
        
def ansi_framed(n=True):
    """
    True = Framed, 2 = Encircled, False = No Frame No Encircled
    """
    if n==True:
        print(ansi_esc+"51m",end='',flush=True)
    elif n==2:
        print(ansi_esc+"52m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"54m",end='',flush=True)

def ansi_overline(n=True):
    if n==True:
        print(ansi_esc+"53m",end='',flush=True)
    elif n==False:
        print(ansi_esc+"55m",end='',flush=True)
        
def ansi_font(n=0):
    if n>=0 and n<=9:
        print(ansi_esc+"1"+str(n)+"m",end='',flush=True)

# COLOUR CONSTANTS

BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7
BRIGHTBLACK = 8
BRIGHTRED = 9
BRIGHTGREEN = 10
BRIGHTYELLOW = 11
BRIGHTBLUE = 12
BRIGHTMAGENTA = 13
BRIGHTCYAN = 14
BRIGHTWHITE = 15


def textcolor(color,  bright=False):
    if bright == False and color < 8:
        b = 0
    elif bright == True and color <=7:
        b = 60
    elif color >=8 and color <=15:
        b = 60 - 8
    print(ansi_esc+str(30+color+b)+"m",end='',flush=True)

def textbackground(color,  bright=False):
    if bright == False and color < 8:
        b = 0
    elif bright == True and color <=7:
        b = 60
    elif color >=8 and color <=15:
        b = 60-8
    print(ansi_esc+str(10+30+color+b)+"m",end='',flush=True)

def ansi_color(fg, bg, fgbright=False, bgbright=False):
    if fgbright==False and fg < 8:
        fgb = 0
    elif fgbright ==True and fg<=7:
        fgb=60
    elif fg>=8 and fg <=15:
        fgb = 60-8
    if bgbright==False and bg < 8:
        bgb=0
    elif bgbright == True and bg<=7:
        bgb=60
    elif bg>=8 and bg<=15:
        bgb=60-8
    print(ansi_esc+str(30+fg+fgb)+";"+str(10+30+bg+bgb)+"m",end='',flush=True)

def ansi_color_8bit(fg, bg):
    print(ansi_esc+"38;5;"+str(fg)+"m",end='',flush=True)
    print(ansi_esc+"48;5;"+str(bg)+"m",end='',flush=True)
    
def ansi_color_24bit(r1, g1, b1, r2, g2, b2):
    print(ansi_esc+"38;2;"+str(r1)+";"+str(g1)+";"+str(b1)+"m",end='',flush=True)
    print(ansi_esc+"48;2;"+str(r2)+";"+str(g2)+";"+str(b2)+"m",end='',flush=True)
    
menux=[]
menuy=[]
menuitem=[]
def additem(x=1, y=1, text=""):
    menux.append(x)
    menuy.append(y)
    menuitem.append(text)

