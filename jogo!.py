import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


velocidade = 10
auto_x = velocidade
auto_y = 0

pause = False

comprimento_snake = 10
quadrado = [20, 20]
altura = 640
largura = 480
x = largura / 2
y = altura / 2

list_snake = list()

fruit_x = randint(0, largura)
fruit_y = randint(0, altura)

pontos = 0

coin = pygame.mixer.Sound('smw_coin.wav')

pygame.mixer.music.set_volume(0.8)
musica_fundo = pygame.mixer.music.load('BoxCat Games - Mission.mp3')
pygame.mixer.music.play(-1)

tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Achei Fácil')
font = pygame.font.SysFont('arial', 30, True, True)
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    text_form = font.render(mensagem, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            exit()
    
    if x > altura - velocidade:
        x = 0
    if x < 0:
        x = altura - velocidade
    if y > largura - velocidade:
        y = 0
    if y < 0:
        y = largura - velocidade

    if pygame.key.get_pressed()[K_a]:
        if auto_x != velocidade:
            auto_x = - velocidade
            auto_y = 0
    elif pygame.key.get_pressed()[K_d]:
        if auto_x != - velocidade:
            auto_x = velocidade
            auto_y = 0
    elif pygame.key.get_pressed()[K_w]:
        if auto_y != velocidade:
            auto_y = - velocidade
            auto_x = 0
    elif pygame.key.get_pressed()[K_s]:
        if auto_y != - velocidade:
            auto_y = velocidade
            auto_x = 0
    
    x += auto_x
    y += auto_y

    fruit = pygame.draw.rect(tela, (255, 0, 0), (fruit_x, fruit_y, *quadrado))
    snake = pygame.draw.rect(tela, (0, 255, 0), (x, y, *quadrado))

    if snake.colliderect(fruit):
        fruit_x = randint(50, 600)
        fruit_y = randint(50, 400)
        pontos += 1
        coin.play()
        comprimento_snake += 1
        
    
    list_head = []
    list_head.append(x)
    list_head.append(y)
    list_snake.append(list_head)

    aumenta_cobra(list_snake)

    if len(list_snake) > comprimento_snake:
        del list_snake[0]

    tela.blit(text_form, (460, 30))

    if [x, y] in list_snake[0:-1]:
        font2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar de novo.'
        format_text = font2.render(mensagem, True, (0, 0, 0))
        ret_text = format_text.get_rect()
        pause = True
        while pause:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                            pontos = 0
                            comprimento_snake = 5
                            auto_x = velocidade
                            auto_y = 0
                            x = int(largura / 2)
                            y = int(altura / 2)
                            list_head = []
                            list_snake = []
                            pause = False
                            fruit_x = randint(50, 600)
                            fruit_y = randint(50, 400)
            ret_text.center = (largura // 1.5, altura // 3)
            tela.blit(format_text, ret_text)
            pygame.display.update()


    pygame.display.update()
