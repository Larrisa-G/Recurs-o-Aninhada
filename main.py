import pygame

pygame.init()
x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Recurssao aninhada game')

bg = pygame.image.load('./imagens/fundo_laranja.png').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

inimigo = pygame.image.load('./imagens/inimigo1t.png').convert_alpha()
inimigo = pygame.transform.scale(inimigo, (50,50))

personagem = pygame.image.load('./imagens/gato_verde.png').convert_alpha()
personagem = pygame.transform.scale(bg, (80,80))
personagem = pygame.transform.rotate(personagem, -90)

pos_inimigo_x = 500
pos_inimigo_y = 360

pos_personagem_x = 200
pos_personagem_y = 300


rodando = True

while rodando:
    for event in pygame.event.get(): #fecha ao clicar em X
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0)) #bg de background

    rel_x = x % bg.get_rect().width
    screen.blit(bg,(rel_x - bg.get_rect().width,0)) #cria background
    if rel_x < 1280:
        screen.blit(bg, (rel_x,0))
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_personagem_y > 1 :
        pos_personagem_y -=1
    if tecla[pygame.K_DOWN] and pos_personagem_y < 665 :
        pos_personagem_y +=1
    if tecla[pygame.K_RIGHT] and pos_personagem_x > 1 :
        pos_personagem_x +=1
    if tecla[pygame.K_LEFT] and pos_personagem_x < 1275 :
        pos_personagem_x -=1

    x-=1 #movimento do fundo
    pos_inimigo_x -=1


    screen.blit(inimigo,(pos_inimigo_x, pos_inimigo_y))
    screen.blit(personagem, (pos_personagem_x, pos_personagem_y))


    pygame.display.update()