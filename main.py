import pygame

#inicializar pygame
pygame.init()

#crear pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
#jugador
img_jugador = pygame.image.load("rocket.png")
jugador_x = 368
jugador_y = 536
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# loop del juego
ejecutar = True
while ejecutar:
    pantalla.fill((205, 144, 228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                print("flecha izquierda presionada")
            if evento.key == pygame.K_RIGHT:
                print("flecha derecha presionada")
    jugador(jugador_x, jugador_y)
    pygame.display.update()