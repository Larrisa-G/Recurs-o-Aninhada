from main import iniciarJogo
import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Trabalho Recursão Aninhada")

BG = pygame.image.load("./imagens/menu.jpg")

def get_font(size):
    return pygame.font.Font("button/font.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("The Magician", True, "purple")
        MENU_TEXT2 = get_font(100).render("Cat", True, "purple")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 80))
        MENU_RECT2 = MENU_TEXT2.get_rect(center=(640, 220))

        PLAY_BUTTON = Button(image=pygame.image.load("button/Play Rect.png"), pos=(640, 400), 
                            text_input="PLAY", font=get_font(75), base_color="white", hovering_color="#338036")
        QUIT_BUTTON = Button(image=pygame.image.load("button/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="white", hovering_color="#338036")

        SCREEN.blit(MENU_TEXT, MENU_RECT,)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    iniciarJogo()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()