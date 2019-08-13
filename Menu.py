import curses #import the curses library
import time
from Cola import Cola
from ListaCircularDoble import ListaCircularDoble
from Random import Food
from ListaEnlazadaDoble import ListaDoble
from Pila import Pila
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

NombreUser='default'

def inicio(NombreUser):
    comida = Food()
    Score ='0'
    velocidad = 100
    
    serpiente = ListaDoble()
    stdscr = curses.initscr() #initialize console
    height = 25
    width = 80
    pos_y = 0
    pos_x = 0
    window = curses.newwin(height,width,pos_y,pos_x) #create a new curses window
    window.keypad(True)     #enable Keypad mode
    curses.noecho()         #prevent input from displaying in the screen
    curses.curs_set(0)      #cursor invisible (0)
    window.border(0)        #default border for our window
    window.nodelay(True)    #return -1 when no key is pressed """"
    window.addstr(0,30, 'SNAKE RELOADED')
    window.addstr(0,55,'User : '+NombreUser)

    key = KEY_RIGHT         #key defaulted to KEY_RIGHT
    pos_x = 5               #initial x position
    pos_y = 5               #initial y position
    serpiente.AddInicio(pos_x,pos_y)
    pos_x=pos_x+1
    serpiente.AddInicio(pos_x,pos_y)
    pos_x=pos_x+1
    serpiente.AddInicio(pos_x,pos_y)

    window.addch(comida.getY(),comida.getX(),comida.getFood())

    while key != 27:                #run program while [ESC] key is not pressed
        window.timeout(velocidad)         #delay of 100 milliseconds

        keystroke = window.getch()  #get current key being pressed
        if keystroke is not  -1:    #key is pressed
            key = keystroke         #key direction changes

        window.addstr(0,1,'SCORE : '+Score)
        nodo = serpiente.final()            #obtiene el ultimo nodo
        window.addch(nodo.posy,nodo.posx,' ')
        
        if key == KEY_RIGHT:                #right direction
            pos_x = pos_x + 1               #pos_x increase
        elif key == KEY_LEFT:               #left direction
            pos_x = pos_x - 1               #pos_x decrease
        elif key == KEY_UP:                 #up direction
            pos_y = pos_y - 1               #pos_y decrease
        elif key == KEY_DOWN:               #down direction
            pos_y = pos_y + 1               #pos_y increase
        
        if pos_x>78:      # para que no tope
            pos_x=1
        if pos_y>23:
            pos_y=1	
        if pos_x<1:
            pos_x=78
        if pos_y<1:
            pos_y=23    

        nodo = serpiente.head()
        serpiente.cambiar(pos_x,pos_y)

        if nodo.posx == comida.getX() and nodo.posy== comida.getY():
            GuardarScore.apilar(comida.getX(),comida.getY())
            sumarscore=int(Score)+1
            Score=str(sumarscore)
            if Score=='15':
                velocidad=75
            food = Food()
            window.addch(food.getY(),food.getX(),food.getFood())
            comida=food
            if food.getFood() == '*':
                serpiente.AddInicio(pos_x,pos_y)
            else:
                serpiente.AddInicio(pos_x,pos_y)
        while nodo !=None:
            x=nodo.posx
            y=nodo.posy
            nodo = nodo.pSig 
            window.addch(y,x,'#')
                
    Puntos.encolar(Score,NombreUser)
    curses.endwin() #return terminal to previous state

def OpcionUser():
    menu = ListaCircularDoble()
    menu.agregar_final('Davis')
    menu.agregar_final('Marcos')
    menu.agregar_final('Pedro')
    menu.agregar_final('Mario')
    menu.agregar_final('Antonio')

    node = menu.getPrimero()

    def paint_menu(win,dato):
        paint_title(win,' USER SELECTION ')          #paint title
        win.addstr(23,20,'Elegir usuario con barra espaciadora')
        win.addstr(11,30,dato)             #paint option 1
        win.timeout(-1)                         #wait for an input thru the getch() function

    def paint_title(win,var):
        win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
        win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
        x_start = round((60-len(var))/2)    #center the new title to be painted
        win.addstr(0,x_start,var)           #paint the title on the screen

    stdscr = curses.initscr() #initialize console
    window = curses.newwin(25,80,0,0) #create a new curses window
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
            return NombreUser
        elif(keystroke==27):
            pass
        else:
            keystroke=-1

    curses.endwin() #return terminal to previous state

def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,25, '1. Play')             #paint option 1
    win.addstr(8,25, '2. Scoreboard')       #paint option 2
    win.addstr(9,25, '3. User Selection')   #paint option 3
    win.addstr(10,25, '4. Reports')         #paint option 4
    win.addstr(11,25, '5. Bulk Loading')    #paint option 5
    win.addstr(12,25, '6. Exit')            #paint option 6
    win.timeout(-1)                         #wait for an input thru the getch() function

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def wait_esc(win):
    key = window.getch()
    while key!=27 and key!=32 :
        key = window.getch()

Puntos = Cola()
GuardarScore = Pila()

stdscr = curses.initscr() #initialize console
window = curses.newwin(25,80,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        
        inicio(NombreUser)

        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SCOREBOARD ')

        window.addstr(2,18, 'NAME')             
        window.addstr(2,31, 'SCORE')

        k=len(Puntos.items)-1
        h=k-20
        hori=3
        while k > h :
            window.addstr(hori,18, Puntos.items[k] )
            window.addstr(hori,31, Puntos.items[k-1] )
            k-=2
            hori+=1
        window.timeout(-1)

        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        
        NombreUser =OpcionUser()
        
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' REPORTS ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' BULK LOADING ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state