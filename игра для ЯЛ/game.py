# coding=utf-8
import pygame
from pygame import *


pygame.init()
window = pygame.display.set_mode((1920, 1080))  # создаем окно
pygame.display.set_caption('Game for YL')  # добавляем имя игры


class Player(object):  # создаем класс игрока с параметрами
    def __init__(self, x, y, width, height):  # координаты по x и y ширина и высота
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5  # скорость игрока
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, window):  # рисуем героя в зависимости от положения
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:  # если игрок смотрит влево то и кадры обновляются из массива с картинками, которые смотрят влево
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:  # если игрок смотрит вправо то и кадры берутся из массива с картинками, которые смотрят вправо
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:  # если игрок стоит то загружается картинка стоячего персонажа
            window .blit(playerStand, (self.x, self.y))


PLATFORM_WIDTH = 64  # высота блока
PLATFORM_HEIGHT = 64  # ширина блока
ROAD = pygame.image.load('platformPack_tile016.png')  # дорга
KUST = pygame.image.load('foliagePack_019.png')  # куст
TREE = pygame.image.load('foliagePack_009.png') # дерево
TOWER = pygame.image.load('tower.png')  # башня

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),
             pygame.image.load('R3.png'), pygame.image.load('R4.png'),
             pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]
# моделька игрока в движении
playerStand = pygame.image.load('standing.png')  # игрок стоит
clock = pygame.time.Clock()
# left = False
# right = False

# карта уровня
level = [
    "  !!                          ",
    "  !!                  ^       ",
    "  !!!!!!!!!!!!!!  ^      @    ",
    "  !!!!!!!!!!!!!!         ^    ",
    "   @    ^    !!!  @    ^      ",
    "   ^   @     !!!    ^   ^     ",
    "        ^    !!! ^       @    ",
    "    @   @    !!!        ^     ",
    "  ^   @ ^    !!!    @    @    ",
    "   @     &   !!! &            ",
    "       ^     !!!      ^  ^    ",
    "     ^       !!!    ^         ",
    "             !!!         @    ",
    "  ^    @     !!!         ^    ",
    "      ^      !!!    ^   ^     ",
    "             !!!              "]


def draw_game_window():  # рисуем карту
    window.fill((62, 117, 59))

    x_block = y_block = 0  # координаты
    for row in level:  # вся строка в level
        for col in row:  # каждый символ в level
            if col == '&':  # рисуем башню
                window.blit(TOWER, (x_block, y_block))
            if col == '!':  # рисуем дорогу
                window.blit(ROAD, (x_block, y_block))
            if col == '^':  # рисуем кусты
                window.blit(KUST, (x_block, y_block))
            if col == '@':  # рисуем деревья
                window.blit(TREE, (x_block, y_block))

            x_block += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y_block += PLATFORM_HEIGHT  # то же самое и с высотой
        x_block = 0
        hero.draw(window)


hero = Player(72, 70, 64, 64)  # создаем игрока, используя консьруктор класса Player
run = True
while run: #  основной цикл игры
    clock.tick(27)  # 27 кадров в секунду
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если нажать крестик игра завершается без ошибки
            run = False

    keys = pygame.key.get_pressed()  # все клавиши

    if keys[pygame.K_a] and hero.x > hero.vel + 5:  # двжение влево
        hero.x -= hero.vel
        hero.left = True  # направление игрока
        hero.right = False  # направление игрока
        hero.standing = False

    elif keys[pygame.K_d] and hero.x < 1920 - hero.width - 10:  # двжение вправо
        hero.x += hero.vel
        hero.left = False  # направление игрока
        hero.right = True  # направление игрока
        hero.standing = False

    elif keys[pygame.K_w] and hero.y > hero.vel + 5:  # двжение вверх
        hero.y -= hero.vel
        hero.left = False  # направление игрока
        hero.right = True  # направление игрока
        hero.standing = False

    elif keys[pygame.K_s] and hero.y < 1080 - hero.height - 10:  # движение вниз
        hero.y += hero.vel
        hero.left = True  # направление игрока
        hero.right = False  # направление игрока
        hero.standing = False

    elif event.type == MOUSEBUTTONDOWN:
        bullets.append([event.pos[0] - 32, 500])
    else:
        hero.left = False  # направление игрока
        hero.right = False  # направление игрока
        hero.walkCount = 0

    draw_game_window()  # рисуем элементы
    pygame.display.update()  # обновляем окно

pygame.quit()  #  обязательная строчка
