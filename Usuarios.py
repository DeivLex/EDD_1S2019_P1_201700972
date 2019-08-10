import curses
import time

menu = ["Opcion1  --->", "<--- Opcion2 --->", "<--- Opcion3 --->", "<--- Opcion4 ---->", "<--- Opcion5"]

def main(stdscr): #INICIA LAS PROPIEDADES BASICAS
    curses.curs_set(0) # SETEA EL CURSOR EN LA POSICION 0
    index = 0
    pintar_menu(stdscr, 0) # VA A INICAR EN EL INDICE 0
    while True:
        tecla = stdscr.getch() # OBTENEMOS EL CARACTER DEL TECLADO
        if(tecla == curses.KEY_RIGHT): # VERIFICAMOS SI EL FLECHA A LA DERECHA
            index = index + 1
        elif (tecla == curses.KEY_LEFT ): # VERIFICAMOS SI ES FLECHA A LA IZQUIERDA
            index = index - 1
        elif (tecla == 27): # SI ES LA TECLA DE SCAPE....
            break
        if( index < 0): # EN CASO DE QUE EL INDICE SE VUELVA NEGAVITO LO DEJAMOS EN 0
            index = 0
        if( index >= len(menu)): # EN CASO QUE EL INDICE SE VUELVA MAYOR AL SIZE DEL ARREGLO...
            index = len(menu)-1 # ... LO LIMITAMOS AL ULTIMO INDICE VALIDO
        pintar_menu(stdscr, index) # MANDAMOS A REPINTAR LA PANTALLA

def pinter_ventana(stdscr):
    # -----------------------------------------------------------
    # PINTAMOS EL MARCO DEL MENU
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK) # COLOR DEL MARCO
    stdscr.attron(curses.color_pair(1)) # PERMITE HABILITAR UN ATRIBUTO ESPECIFICO
    stdscr.box("#", "$") ## PINTA EL MARCO
    stdscr.attroff(curses.color_pair(1)) # DESHABILITA EL ATRIBUTO ESPECIICO
    stdscr.refresh()
    # -----------------------------------------------------------

def pintar_menu(stdsrc, index):
    # -----------------------------------------------------------
    stdsrc.clear() # LIMPIA LA CONSOLA
    pinter_ventana(stdsrc) # MANDA A PINTAR EL MARCO
    altura, ancho = stdsrc.getmaxyx() # OBTIENE LA ALTURA Y ANCHO DE LA PANTALLA
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # COLOR DE LAS OPCIONES, INIICIALIZA UNA PAREJA DE COLORES EL COLOR DE LETRA Y COLOR DE FONDO RESPECTIVAMENTE
    y = int(altura/2) 
    x = int((ancho/2)-(len(menu[index])/2))
    stdsrc.addstr(y,x, menu[index], curses.color_pair(2)) # HAGREGA UNA CADENA  LA PANTALLA EN COORDENADAS Y, X Y UN ATRIBUTO EN ESTE CASO ES LA PAREJA DE COLORES
    stdsrc.refresh()
    # -----------------------------------------------------------


curses.wrapper(main)