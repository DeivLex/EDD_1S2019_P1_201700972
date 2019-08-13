import curses #import the curses library
import time
from ListaCircularDoble import ListaCircularDoble
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

menu = ListaCircularDoble()
menu.agregar_final('Davis')
menu.agregar_final('Marcos')
menu.agregar_final('Pedro')
menu.agregar_final('Mario')
menu.agregar_final('Antonio')

NombreUser='default'

node = menu.getPrimero()

def paint_menu(win,dato):
    paint_title(win,' USER SELECTION ')          #paint title
    win.addstr(18,10,'Elegir usuario con barra espaciadora')
    win.addstr(9,20,dato)             #paint option 1
    win.timeout(-1)                         #wait for an input thru the getch() function

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def getUser(self):
    return NombreUser

stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window,'<-- '+node.dato+' -->')      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==KEY_RIGHT): #1
        node = node.siguiente
        paint_menu(window,'<-- '+node.dato+' -->')
        keystroke=-1
    elif(keystroke==KEY_LEFT):
        node = node.anterior
        paint_menu(window,'<-- '+node.dato+' -->')
        keystroke=-1
    elif(keystroke==32):
        NombreUser=node.dato
    elif(keystroke==27):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state