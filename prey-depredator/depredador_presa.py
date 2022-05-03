# autor: Ruben Rodriguez
from numpy import unique, linspace
import pygame
from random import randint, random
import matplotlib.pyplot as plt
# Define some colors222
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GREEN = (0, 255, 0, 255)
RED = (255, 0, 0, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 7
HEIGHT = 7

# This sets the margin between each cell
MARGIN = 1

# FOX PROPERTIES
MAX_AGE_ZORRO = 150
PROB_APAREARCE_ZORRO = 0.92
MAX_CRIAS_ZORRO = 2
EDAD_APAREARCE_ZORRO = 50
EDAD_ZORRO = 0
COMIDA = 10
CRIAS = 0

# RABBIT PROPERTIES
MAX_AGE_CONEJO = 150
PROB_APAREARCE_CONEJO = 0.92
MAX_CRIAS_CONEJO = 2
EDAD_APAREARCE_CONEJO = 50
EDAD_CONEJO = 0
CRIAS = 0

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(100):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(100):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
# grid[1][5] = 1
posiciones_conejos = []
posiciones_zorros = []

"""

objetos_conejo ={
    
    key = {
        properties
    }
    
    "2x2y" : {
        hambre:...,
        
    }
}


"""


def zorro(coordenadas, cria):

    if cria:
        edad = 0
        comida = COMIDA
    else:
        edad = randint(1, MAX_AGE_ZORRO)
        comida = randint(5, COMIDA)

    zorro = {
        "edadAparearce": EDAD_APAREARCE_ZORRO,
        "edadMaxima": MAX_AGE_ZORRO,
        "probAparearce": PROB_APAREARCE_ZORRO,
        "maxCrias": MAX_CRIAS_ZORRO,
        "comida": comida,
        "edad": edad,
        "coordenadas": coordenadas,
        "crias": 0
    }

    return zorro


def conejo(coordenadas, cria):

    if cria:
        edad = 0
    else:
        edad = randint(1, MAX_AGE_CONEJO)

    conejo = {
        "edadAparearce": EDAD_APAREARCE_CONEJO,
        "edadMaxima": MAX_AGE_CONEJO,
        "probAparearce": PROB_APAREARCE_CONEJO,
        "maxCrias": MAX_CRIAS_CONEJO,
        "edad": edad,
        "coordenadas": coordenadas,
        "crias": 0
    }

    return conejo


def generate():

    # generate random rabbits == 1
    for i in range(300):
        x = randint(0, 99)
        y = randint(0, 99)
        grid[x][y] = 1
        posiciones_conejos.append([x, y])

    # grid[0][10] = 1
    # posiciones_conejos.append([0, 10])

    # grid[0][11] = 2
    # posiciones_conejos.append([0, 11])

    # generate random foxies == 2
    for i in range(50):
        # x = randint(0, 99)
        # y = randint(0, 99)

        while True:
            x = randint(0, 99)
            y = randint(0, 99)
            if(grid[x][y] == 1):
                pass
            else:
                grid[x][y] = 2
                posiciones_zorros.append([x, y])
                break
            # else:
            #     grid[x][y] = 2
            #     posiciones_zorros.append([x, y])


# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [810, 810]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def positions(posicion):
    arround = []
    # primer fila
    if posicion[0] == 0 and posicion[1] != 0 and posicion[1] != len(grid[0])-1:
        # izquierda - derecha
        arround.append([posicion[0], posicion[1]-1])  # x-1, y
        arround.append([posicion[0], posicion[1]+1])  # x+1, y

        # abajo
        arround.append([posicion[0]+1, posicion[1]-1])  # x+1,y+1
        arround.append([posicion[0]+1, posicion[1]])  # x, y+1
        arround.append([posicion[0]+1, posicion[1]+1])  # x+1,y+1
    # ultima fila
    elif posicion[0] == len(grid)-1 and posicion[1] != 0 and posicion[1] != len(grid[0])-1:
        # arriba
        arround.append([posicion[0]-1, posicion[1]-1])  # x-1,y-1
        arround.append([posicion[0]-1, posicion[1]])  # x, y-1
        arround.append([posicion[0]-1, posicion[1]+1])  # x+1,y+1

        # izquierda - derecha
        arround.append([posicion[0], posicion[1]-1])  # x-1, y
        arround.append([posicion[0], posicion[1]+1])  # x+1, y
    # primer columna
    elif posicion[1] == 0 and posicion[0] != 0 and posicion[0] != len(grid[0])-1:
        # arriba
        arround.append([posicion[0]-1, posicion[1]])  # x, y-1
        arround.append([posicion[0]-1, posicion[1]+1])  # x+1,y+1
        # derecha
        arround.append([posicion[0], posicion[1]+1])  # x+1, y
        # abajo
        arround.append([posicion[0]+1, posicion[1]])  # x, y+1
        arround.append([posicion[0]+1, posicion[1]+1])  # x+1,y+1
    # ultima columna
    elif posicion[1] == len(grid[0])-1 and posicion[0] != 0 and posicion[0] != len(grid[0])-1:
        # arriba
        arround.append([posicion[0]-1, posicion[1]])  # x, y-1
        arround.append([posicion[0]-1, posicion[1]-1])  # x-1,y-1
        # izquierda
        arround.append([posicion[0], posicion[1]-1])  # x-1, y
        # abajo
        arround.append([posicion[0]+1, posicion[1]])  # x, y+1
        arround.append([posicion[0]+1, posicion[1]-1])  # x-1 , y+1
    # esquina superior izquierda
    elif posicion[0] == 0 and posicion[1] == 0:
        # derecha
        arround.append([posicion[0], posicion[1]+1])  # x+1, y
        # abajo
        arround.append([posicion[0]+1, posicion[1]])  # x, y+1
        arround.append([posicion[0]+1, posicion[1]+1])  # x+1,y+1
    # esquina inferior izquierda
    elif posicion[0] == len(grid)-1 and posicion[1] == 0:
        # derecha
        arround.append([posicion[0], posicion[1]+1])  # x-1, y
        # arriba
        arround.append([posicion[0]-1, posicion[1]])  # x, y-1
        arround.append([posicion[0]-1, posicion[1]+1])  # x+1,y+1
    # esquina superior derecha
    elif posicion[0] == 0 and posicion[1] == len(grid[0])-1:
        # izquierda
        arround.append([posicion[0], posicion[1]-1])  # x+1, y
        # abajo
        arround.append([posicion[0]+1, posicion[1]])  # x, y+1
        arround.append([posicion[0]+1, posicion[1]-1])  # x+1,y+1
    # esquina inferior derecha
    elif posicion[0] == len(grid)-1 and posicion[1] == len(grid[0])-1:
        # izquierda
        arround.append([posicion[0], posicion[1]-1])  # x-1, y
        # arriba
        arround.append([posicion[0]-1, posicion[1]])  # x, y-1
        arround.append([posicion[0]-1, posicion[1]-1])  # x+1,y+1
    else:
        # arriba
        arround.append([posicion[0]-1, posicion[1]-1])  # x-1,y-1
        arround.append([posicion[0]-1, posicion[1]])  # x, y-1
        arround.append([posicion[0]-1, posicion[1]+1])  # x+1,y+1

        # izquierda - derecha
        arround.append([posicion[0], posicion[1]-1])  # x-1, y
        arround.append([posicion[0], posicion[1]+1])  # x+1, y

        # abajo
        arround.append([posicion[0]+1, posicion[1]-1])  # x+1,y+1
        arround.append([posicion[0]+1, posicion[1]])  # x, y+1
        arround.append([posicion[0]+1, posicion[1]+1])  # x+1,y+1

    return arround


def movements(posicion):
    disponibles = []
    arround = positions(posicion)

    # print("--------------------------------------------------")
    # print(posicion, "   ", arround)
    for disp in arround:
        # print(pygame.Surface.get_at(
        #     screen, ((MARGIN + WIDTH) * disp[1] + MARGIN, (MARGIN + HEIGHT) * disp[0] + MARGIN)), pygame.Surface.get_at(
        #     screen, ((MARGIN + WIDTH) * disp[1] + MARGIN, (MARGIN + HEIGHT) * disp[0] + MARGIN)) == (255, 255, 255, 255))
        if(pygame.Surface.get_at(
                screen, ((MARGIN + WIDTH) * disp[1] + MARGIN, (MARGIN + HEIGHT) * disp[0] + MARGIN)) == (255, 255, 255, 255)):
            disponibles.append(disp)
    if len(disponibles) > 0:
        sel = randint(0, len(disponibles)-1)
        # print(sel, " ", disponibles)
        return disponibles[sel]


def eat(posicionZorro):

    conejosDisponibles = []
    arround = positions(posicionZorro)

    for disp in arround:
        if(pygame.Surface.get_at(screen, ((MARGIN + WIDTH) * disp[1] + MARGIN, (MARGIN + HEIGHT) * disp[0] + MARGIN)) == (0, 255, 0, 255)):
            conejosDisponibles.append(disp)

    if len(conejosDisponibles) != 0:
        sel = randint(0, len(conejosDisponibles)-1)
        # print(sel, " ", conejosDisponibles)
        return conejosDisponibles[sel]


def reproduce(posicion, color, natalidad):
    arround = positions(posicion)
    disponibles = []
    parejas = []

    # print("--------------------------------------------------")
    # print(posicion, "   ", arround)
    for position in arround:
        # print(pygame.Surface.get_at(
        #     screen, ((MARGIN + WIDTH) * disp[1] + MARGIN, (MARGIN + HEIGHT) * disp[0] + MARGIN)), pygame.Surface.get_at(
        #     screen, ((MARGIN + WIDTH) * disp[1] + MARGIN, (MARGIN + HEIGHT) * disp[0] + MARGIN)) == (255, 255, 255, 255))

        # white
        if(pygame.Surface.get_at(
                screen, ((MARGIN + WIDTH) * position[1] + MARGIN, (MARGIN + HEIGHT) * position[0] + MARGIN)) == (255, 255, 255, 255)):
            disponibles.append(position)

        # green or red
        if(pygame.Surface.get_at(
                screen, ((MARGIN + WIDTH) * position[1] + MARGIN, (MARGIN + HEIGHT) * position[0] + MARGIN)) == color):
            parejas.append(position)

    probRepro = random()
    if probRepro > natalidad and len(parejas) == 1 and len(disponibles) > 0:
        sel = randint(0, len(disponibles)-1)
        # print(sel, " ", disponibles)
        return disponibles[sel]
    else:
        return None


# -------- Main Program Loop -----------
# while not done:
i = 0
tiempos = []
estadosZorros = []
estadosConejos = []
generate()
again = False
while not done:

    # Set the screen background
    screen.fill(BLACK)
    if not again:
        # Draw the grid
        for row in range(100):
            for column in range(100):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                if grid[row][column] == 2:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                done = True

        for posicion in posiciones_zorros:
            eatRabbit = eat(posicion)
            # print(eatRabbit)

            if len(posiciones_zorros) > len(posiciones_conejos):
                probRepro = 1.1
                probMuerte = 0.1
            else:
                probRepro = 0.99
                probMuerte = 0.8

            if i % 80 == 0:
                muerte = random()
                if muerte > probMuerte:
                    grid[posicion[0]][posicion[1]] = 0
                    posiciones_zorros.remove(posicion)
                    continue

            if eatRabbit is None:
                reprod = reproduce(posicion, (255, 0, 0, 255), probRepro)
                if reprod is None:
                    new_position = movements(posicion)
                    if new_position is None:
                        grid[posicion[0]][posicion[1]] = 0
                        posiciones_zorros.remove(posicion)
                    else:
                        grid[posicion[0]][posicion[1]] = 0
                        grid[new_position[0]][new_position[1]] = 2
                        posiciones_zorros.remove(posicion)
                        posiciones_zorros.append(new_position)
                else:
                    grid[reprod[0]][reprod[1]] = 2
                    posiciones_zorros.append(reprod)

            else:
                if eatRabbit in posiciones_conejos and len(posiciones_conejos) > 100:
                    grid[posicion[0]][posicion[1]] = 0
                    grid[eatRabbit[0]][eatRabbit[1]] = 2
                    posiciones_zorros.remove(posicion)
                    posiciones_zorros.append(eatRabbit)
                    # remove rabbit
                    posiciones_conejos.remove(eatRabbit)

        for posicion in posiciones_conejos:

            probRepro = 0.

            if len(posiciones_conejos) < len(posiciones_zorros):
                probRepro = 0.2
                probMuerte = 0.95
            else:
                probRepro = 0.94
                probMuerte = 0.4

            if i % 40 == 0:
                muerte = random()
                if muerte > probMuerte:
                    grid[posicion[0]][posicion[1]] = 0
                    posiciones_conejos.remove(posicion)
                    continue

            reprod = reproduce(posicion, (0, 255, 0, 255), probRepro)
            if reprod is None:
                new_position = movements(posicion)
                if new_position is None:
                    grid[posicion[0]][posicion[1]] = 0
                    posiciones_conejos.remove(posicion)
                else:
                    grid[posicion[0]][posicion[1]] = 0
                    grid[new_position[0]][new_position[1]] = 1
                    posiciones_conejos.remove(posicion)
                    posiciones_conejos.append(new_position)
            else:
                # if type(reprod) != "NoneType":
                grid[reprod[0]][reprod[1]] = 1
                posiciones_conejos.append(reprod)

        print(
            f"conejos: {len(posiciones_conejos)} zorros:{len(posiciones_zorros)}")
    else:
        pass
    i += 1
    tiempos.append(i)
    estadosConejos.append(len(posiciones_conejos))
    estadosZorros.append(len(posiciones_zorros))
    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# for i in posiciones_conejos:
#     print(i, " ", posiciones_conejos.count(i))

# print(len(set(posiciones_conejos)))
# graphConejos = np.concatenate(tiempos, len(posiciones_conejos))
plt.plot(tiempos, estadosZorros, label="Zorros", color="red")
plt.plot(tiempos, estadosConejos, label="Conejos", color="green")
#plt.title("Zorros aumentan - Conejos se extinguen")
plt.show()
# plt.savefig("zorrosGanan.jpg")
