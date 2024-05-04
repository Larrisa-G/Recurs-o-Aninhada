import pygame
import sys
import random

pygame.init()
x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Recurssao aninhada game')

bg = pygame.image.load('./imagens/fundo_laranja.png').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

inimigo = pygame.image.load('./imagens/cat_idle.png').convert_alpha()
inimigo = pygame.transform.scale(inimigo, (50,50))

personagem = pygame.image.load('./imagens/cat_idle_small.png').convert_alpha()
personagem = pygame.transform.scale(personagem, (300,300))
personagem = pygame.transform.rotate(personagem, 0)

pos_inimigo_x = 500
pos_inimigo_y = 360

pos_personagem_x = 200
pos_personagem_y = 300

triggered = False
rodando = True


class Projetil(pygame.sprite.Sprite) :
    def __init__(self, posx, posy) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./imagens/luzt.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.velocidadade = -5

    def update(self) :
        self.rect.x = self.rect.x - self.velocidadade
    
all_sprites = pygame.sprite.Group()

def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x,y]

while rodando:
    for event in pygame.event.get(): #fecha ao clicar em X
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0)) 

    #cria background
    rel_x = x % bg.get_rect().width
    screen.blit(bg,(rel_x - bg.get_rect().width,0)) 
    if rel_x < 1280:
        screen.blit(bg, (rel_x,0))
    
    #movimento personagem
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_personagem_y > 1 :
        pos_personagem_y -= velocidade_personagem
    if tecla[pygame.K_DOWN] and pos_personagem_y < 505 :
        pos_personagem_y +=velocidade_personagem 
    if tecla[pygame.K_RIGHT] and pos_personagem_x < 1000 :
        pos_personagem_x +=velocidade_personagem
    if tecla[pygame.K_LEFT] and pos_personagem_x  > 1 :
        pos_personagem_x -= (velocidade_personagem + 0.5)

    # inimigo
    if pos_inimigo_x == 50:
        pos_inimigo_x = respawn()[0]
        pos_inimigo_y = respawn()[1]

    #luz
    if tecla[pygame.K_SPACE] :
        triggered = True
        proj_luz = Projetil(pos_personagem_x, pos_personagem_y)
        all_sprites.add(proj_luz)

    #velocidade dos movimentos
    x-=1 
    velocidade_personagem = 2
    pos_inimigo_x -=5

    #Atualização e desenho do projétil de luz
    if triggered:
        all_sprites.update()
        all_sprites.draw(screen)

    #mostra na teal
    screen.blit(inimigo,(pos_inimigo_x, pos_inimigo_y))
    screen.blit(personagem, (pos_personagem_x, pos_personagem_y))
        
    pygame.display.update()