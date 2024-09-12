import pygame
import random
import math

#inicializar pygame
pygame.init()

#crear pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

#Fondo
fondo = pygame.image.load("Fondo.jpg")
#jugador
img_jugador = pygame.image.load("rocket.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append( random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.09)
    enemigo_y_cambio.append(50)



#variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.30
bala_visible = False
#puntaje
puntaje = 0
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16,y + 10))

#funcion detectar colisiones
def colisiones(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1,2))
    if distancia < 27:
        return True
    else:
        return False
# loop del juego
ejecutar = True
while ejecutar:
    #imagen de fondo
    pantalla.blit(fondo, (0,0))

    #evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
        #evento presionar fechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.15
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.15
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(jugador_x, bala_y)
        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    #modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    #mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

    # mantener dentro de bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.09
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.09
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        colision = colisiones(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
        enemigo(enemigo_x[e], enemigo_y[e], e)
    #movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)
    #actualizar
    pygame.display.update()