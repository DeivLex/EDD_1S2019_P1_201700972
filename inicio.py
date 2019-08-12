import curses #import the curses library
from Random import Food
from ListaEnlazadaDoble import ListaDoble
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

comida = Food()
Score ='0'
velocidad = 100
nameplayer='Davis'

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
window.nodelay(True)    #return -1 when no key is pressed
window.addstr(0,30, 'SNAKE RELOADED')
window.addstr(0,55,'User : '+nameplayer)

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
            
           
curses.endwin() #return terminal to previous state