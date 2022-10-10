import os
import random
from time import sleep

os.system('cls')

# Introduccion de datos
width = int(input("Introduzca el ancho del laberinto: "))
height = int(input("Introduzca el alto del laberinto: "))
obs = int(input("Introduzca la cantidad de obstaculos: "))

while obs > (width * height * 0.8):
    nval = int(input("Error, la cantidad de paredes no debe ocupar más que el 80% del laberinto: "))
    obs = nval
maze = []

# Se crea el terreno
for i in range(height):
    row = []
    for j in range(width):
        row.append("#")
    maze.append(row)

# Se recorre el laberinto aleatoriamente vaciando espacios
space = (width * height) - obs
n = 1
x = random.randint(0, width - 1)
y = random.randint(0, height - 1)
maze[y][x] = " "
# Esto se hace hasta que se cumpla la cantidad de espacios correspondiente
while n < space:
    mov = random.randint(0, 3)
    if mov == 0:
        cant = random.randint(0, height - 1 - y)
        for i in range(cant):
            if (n >= space):
                break
            y += 1
            if (maze[y][x] != " "):
                maze[y][x] = " "
                n += 1

    if mov == 1:
        cant = random.randint(0, y)
        for i in range(cant):
            if (n >= space):
                break
            y -= 1
            if (maze[y][x] != " "):
                maze[y][x] = " "
                n += 1

    if mov == 2:
        cant = random.randint(0, width - 1 - x)
        for i in range(cant):
            if (n >= space):
                break
            x += 1
            if (maze[y][x] != " "):
                maze[y][x] = " "
                n += 1

    if mov == 3:
        cant = random.randint(0, x)
        for i in range(cant):
            if (n >= space):
                break
            x -= 1
            if (maze[y][x] != " "):
                maze[y][x] = " "
                n += 1

# Se agrega el objeto
while True:
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    if maze[y][x] != "#":
        maze[y][x] = "*"
        break
# Se muestra el laberinto
for i in range(height):
    for j in range(width):
        print(maze[i][j],end=" ")
    print("")