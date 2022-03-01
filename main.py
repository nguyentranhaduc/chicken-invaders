import random
import pygame
from pygame import mixer
import time

# list objects trong game
level1 = pygame.sprite.Group()
level2 = pygame.sprite.Group()
level3 = pygame.sprite.Group()
level4 = pygame.sprite.Group()

level1Enemies = pygame.sprite.Group()
level2Enemies = pygame.sprite.Group()
level3Enemies = pygame.sprite.Group()
level4Enemies = pygame.sprite.Group()

lazerList = pygame.sprite.Group()
smallEggList = pygame.sprite.Group()
chickenLegList = pygame.sprite.Group()

# cac bien toan cuc
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
LEVEL = 0
SCORE = 0

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

HEALTHBOSS = 100
HEALTHPLAYER = 5



class ChickenLeg(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("media/images/duiga.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 2

    def update(self):
        self.rect.y += self.speed

        # neu ra khoi man hinh thi se bi xoa
        if (self.rect.y > SCREEN_HEIGHT):
            chickenLegList.remove(self)


class Egg(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/egg/egg_-100.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_0.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_100.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_0.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-100.png"))

        self.current_sprite = 0

        self.IMAGE_INTERVAL = random.randint(10, 80)
        self.last_update_animation = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-800, 0)

        self.health = 5
        self.speed = random.randint(1, 5)

    def rotDuiGa(self):
        quyetdinh = random.randint(0, 3)
        if (quyetdinh == 1):
            chickenLegList.add(ChickenLeg(self.rect.x - self.image.get_width()/2, self.rect.y - self.image.get_height()/2))

    def update(self):
        self.rect.y += self.speed

        # neu ra khoi man hinh thi se xuat hien lai
        if (self.rect.y > SCREEN_HEIGHT):
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-800, 0)
            self.speed = random.randint(1, 5)

        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))

        # khi lazer ban trung egg
        for lazer in lazerList:
            if (pygame.sprite.collide_rect(self, lazer)):
                lazerList.remove(lazer)
                self.health -= 1
                if (self.health == 0):
                    level1Enemies.remove(self)
                    self.rotDuiGa()
                    self.sound = mixer.Sound("media/sounds/explosion.wav")
                    self.sound.play()
                    global SCORE
                    SCORE += 10
                    if not level1Enemies:
                        mixer.music.load("media/sounds/level_complete.wav")
                        mixer.music.play()
                        completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                        SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                        pygame.display.update()
                        time.sleep(10)
                        global LEVEL
                        LEVEL = 2
                        pygame.display.update()

class UFO(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-100.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_0.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_100.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_0.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-100.png"))

        self.current_sprite = 0

        self.IMAGE_INTERVAL = random.randint(10, 80)
        self.last_update_animation = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.width)
        self.rect.x = random.randint(-800, 0)

        self.health = 5
        self.speed = random.randint(1, 3)

    def rotDuiGa(self):
        quyetdinh = random.randint(0, 3)
        if (quyetdinh == 1):
            chickenLegList.add(ChickenLeg(self.rect.x - self.image.get_width()/2, self.rect.y - self.image.get_height()/2))

    def update(self):
        self.rect.x += self.speed

        # neu ra khoi man hinh thi se xuat hien lai
        if (self.rect.x > SCREEN_WIDTH):
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.width)
            self.rect.x = random.randint(-800, 0)
            self.speed = random.randint(1, 3)

        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))

        # khi lazer ban trung UFO
        for lazer in lazerList:
            if (pygame.sprite.collide_rect(self, lazer)):
                lazerList.remove(lazer)
                self.health -= 1
                if (self.health == 0):
                    level2Enemies.remove(self)
                    self.rotDuiGa()
                    self.sound = mixer.Sound("media/sounds/explosion.wav")
                    self.sound.play()
                    global SCORE
                    SCORE += 20

                    if not level2Enemies:
                        mixer.music.load("media/sounds/level_complete.wav")
                        mixer.music.play()
                        completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                        SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                        pygame.display.update()
                        time.sleep(10)
                        global LEVEL
                        LEVEL = 3
                        pygame.display.update()

class Chicken(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-100.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-90.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-80.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-70.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-60.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-50.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-40.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-30.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-20.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-10.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_0.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_10.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_20.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_30.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_40.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_50.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_60.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_70.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_80.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_90.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_100.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_90.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_80.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_70.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_60.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_50.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_40.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_30.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_20.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_10.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_0.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-10.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-20.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-30.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-40.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-50.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-60.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-70.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-80.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-90.png"))
        self.sprites.append(pygame.image.load("media/images/chicken/chicken_-100.png"))

        self.current_sprite = 0

        self.IMAGE_INTERVAL = random.randint(10, 80)
        self.last_update_animation = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 800)
        self.rect.y = random.randint(0, 800)

        self.health = 5
        self.speed = random.randint(1, 3)

    def rotDuiGa(self):
        quyetdinh = random.randint(0, 3)
        if (quyetdinh == 1):
            chickenLegList.add(ChickenLeg(self.rect.x - self.image.get_width()/2, self.rect.y - self.image.get_height()/2))

    def update(self):
        self.rect.x -= self.speed

        # neu ra khoi man hinh thi se xuat hien lai
        if (self.rect.x < 0):
            self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 800)
            self.rect.y = random.randint(0, 800)
            self.speed = random.randint(1, 3)

        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))

        # khi lazer ban trung Chicken
        for lazer in lazerList:
            if (pygame.sprite.collide_rect(self, lazer)):
                lazerList.remove(lazer)
                self.health -= 1
                if (self.health == 0):
                    level3Enemies.remove(self)
                    self.rotDuiGa()
                    self.sound = mixer.Sound("media/sounds/explosion.wav")
                    self.sound.play()
                    global SCORE
                    SCORE += 30
                    if not level3Enemies:
                        mixer.music.load("media/sounds/level_complete.wav")
                        mixer.music.play()
                        completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                        SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                        pygame.display.update()
                        time.sleep(10)
                        global LEVEL
                        LEVEL = 4
                        pygame.display.update()


class SmallEgg(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("media/images/egg_bullet.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 2

        self.sound = mixer.Sound("media/sounds/smallegg_sound.wav")
        self.sound.play()

    def update(self):
        self.rect.y += self.speed

        # neu ra khoi man hinh thi se bi xoa
        if (self.rect.y > SCREEN_HEIGHT):
            smallEggList.remove(self)


class Boss(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/boss/boss_-100.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-90.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-80.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-70.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-60.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-50.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-40.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-30.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-20.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-10.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_0.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_10.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_20.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_30.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_40.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_50.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_60.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_70.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_80.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_90.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_100.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_90.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_80.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_70.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_60.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_50.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_40.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_30.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_20.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_10.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_0.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-10.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-20.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-30.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-40.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-50.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-60.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-70.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-80.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-90.png"))
        self.sprites.append(pygame.image.load("media/images/boss/boss_-100.png"))

        self.current_sprite = 0

        self.IMAGE_INTERVAL = random.randint(10, 80)
        self.last_update_animation = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (300, 300))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(- self.image.get_height(), 0)

        self.speed = 2

        # huong di chuyen cua boss:
        # 0: di xuong
        # 1: di len
        # 2: di qua trai
        # 3: di qua phai
        self.moveWay = 0

    def diChuyen(self):
        if (self.moveWay == 0):
            self.rect.y += self.speed
        elif (self.moveWay == 1):
            self.rect.y -= self.speed
        elif (self.moveWay == 2):
            self.rect.x -= self.speed
        elif (self.moveWay == 3):
            self.rect.x += self.speed

    def randomHuongDiChuyen(self):
        self.moveWay = random.randint(0, 3)

    def deTrung(self):
        quyetdinh = random.randint(0, 110)
        if (quyetdinh == 100):
            randomx = random.randint(self.rect.x, self.rect.x + self.image.get_width())
            smallEggList.add(SmallEgg(randomx, self.rect.y + self.image.get_height()))

    def update(self):
        # su dung cac bien toan cuc
        global HEALTHBOSS
        global SCORE
        global LEVEL
        global HEALTHPLAYER

        # reset hoat anh
        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (300, 300))

        # boss de trung
        if (HEALTHBOSS != 0):
            self.deTrung()

        # neu cham vao ria man hinh thi doi huong di chuyen
        # cham goc tren + trai
        if (self.rect.x < 0 and self.rect.y < 0):
            while (self.moveWay == 1 or self.moveWay == 2):
                self.randomHuongDiChuyen()
        # cham goc tren + phai
        elif ( ( self.rect.x > ( SCREEN_WIDTH - self.image.get_width() ) ) and self.rect.y < 0):
            while (self.moveWay == 1 or self.moveWay == 3):
                self.randomHuongDiChuyen()
        # cham goc duoi _ trai
        elif ( ( self.rect.y > (SCREEN_HEIGHT - self.image.get_height() ) ) and self.rect.x < 0):
            while (self.moveWay == 0 or self.moveWay == 2):
                self.randomHuongDiChuyen()
        # cham goc duoi + phai
        elif ( ( self.rect.x > ( SCREEN_WIDTH - self.image.get_width() ) ) and ( self.rect.y > ( SCREEN_HEIGHT - self.image.get_height() ) ) ):
            while (self.moveWay == 0 or self.moveWay == 3):
                self.randomHuongDiChuyen()
        # cham ria duoi
        elif ( ( self.rect.y > ( SCREEN_HEIGHT - self.image.get_height() ) ) and ( self.moveWay == 0 ) ):
            while (self.moveWay == 0):
                self.randomHuongDiChuyen()
        # cham ria tren
        elif (self.rect.y < 0 and (self.moveWay == 1)):
            while (self.moveWay == 1):
                self.randomHuongDiChuyen()
        # cham ria phai
        elif ( ( self.rect.x > ( SCREEN_WIDTH - self.image.get_width() ) ) and ( self.moveWay == 3 ) ):
            while (self.moveWay == 3):
                self.randomHuongDiChuyen()
        # cham ria trai
        elif (self.rect.x < 0 and (self.moveWay == 2)):
            while (self.moveWay == 2):
                self.randomHuongDiChuyen()

        self.diChuyen()

        # khi lazer ban trung Boss
        for lazer in lazerList:
            if (pygame.sprite.collide_rect(self, lazer)):
                lazerList.remove(lazer)
                HEALTHBOSS -= 1
                if (HEALTHBOSS == 0):
                    level4Enemies.remove(self)
                    self.sound = mixer.Sound("media/sounds/explosion.wav")
                    self.sound.play()
                    SCORE += 100
                    if not level4Enemies:
                        mixer.music.load("media/sounds/level_complete.wav")
                        mixer.music.play()
                        completedlevel_label = pygame.image.load("media/images/win_text.png")
                        SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 26))
                        pygame.display.update()
                        time.sleep(10)
                        LEVEL = 0
                        HEALTHPLAYER = 5
                        SCORE = 0
                        HEALTHBOSS = 100

                        pygame.display.update()


class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/pixel_laser_yellow.png"))
        self.sprites.append(pygame.image.load("media/images/pixel_laser_blue.png"))
        self.sprites.append(pygame.image.load("media/images/pixel_laser_red.png"))
        self.sprites.append(pygame.image.load("media/images/pixel_laser_green.png"))

        self.current_sprite = -1
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 90))

        self.IMAGE_INTERVAL = 100
        self.last_update_animation = 0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 7

        self.sound = mixer.Sound("media/sounds/shot.wav")
        self.sound.play()

    def update(self):
        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 90))

        self.rect.y -= self.speed

        # neu ra khoi man hinh thi se bi xoa
        if (self.rect.y < -10):
            lazerList.remove(self)




class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-100.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_0.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_100.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_0.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-100.png"))

        self.IMAGE_INTERVAL = 10
        self.last_update_animation = 0

        self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 93))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 3

    def update(self):
        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 93))

        global SCORE
        global LEVEL
        global HEALTHPLAYER
        global HEALTHBOSS

        # neu player cham vao dui ga
        for duiga in chickenLegList:
            if (pygame.sprite.collide_rect(self, duiga)):
                self.sound = mixer.Sound("media/sounds/earnduiga.wav")
                self.sound.play()
                chickenLegList.remove(duiga)
                SCORE += 5
                pygame.display.update()

        # neu player cham vao egg
        for egg in level1Enemies:
            if (pygame.sprite.collide_rect(self, egg)):
                self.sound = mixer.Sound("media/sounds/playerbehit.wav")
                self.sound.play()
                level1Enemies.remove(egg)
                HEALTHPLAYER -= 1
                SCORE += 10
                pygame.display.update()

                if (HEALTHPLAYER == 0):
                    self.sound = mixer.Sound("media/sounds/game_over_background_music.wav")
                    pygame.mixer.music.stop()
                    gameover_label = pygame.image.load("media/images/gameover_text.png")
                    SCREEN.blit(gameover_label, (SCREEN_WIDTH / 2 - 260, SCREEN_HEIGHT / 2 - 33))
                    pygame.display.update()
                    self.sound.play()
                    time.sleep(10)
                    LEVEL = 0
                    SCORE = 0
                    HEALTHPLAYER = 5
                    self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)
                    for enemy in level1Enemies:
                        level1Enemies.remove(enemy)

                elif not level1Enemies:
                    mixer.music.load("media/sounds/level_complete.wav")
                    mixer.music.play()
                    completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                    SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                    pygame.display.update()
                    time.sleep(8)
                    LEVEL = 2
                    pygame.display.update()

        # neu player cham vao UFO
        for ufo in level2Enemies:
            if (pygame.sprite.collide_rect(self, ufo)):
                self.sound = mixer.Sound("media/sounds/playerbehit.wav")
                self.sound.play()
                level2Enemies.remove(ufo)
                HEALTHPLAYER -= 1
                SCORE += 20
                pygame.display.update()

                if (HEALTHPLAYER == 0):
                    self.sound = mixer.Sound("media/sounds/game_over_background_music.wav")
                    pygame.mixer.music.stop()
                    gameover_label = pygame.image.load("media/images/gameover_text.png")
                    SCREEN.blit(gameover_label, (SCREEN_WIDTH / 2 - 260, SCREEN_HEIGHT / 2 - 33))
                    pygame.display.update()
                    self.sound.play()
                    time.sleep(10)
                    LEVEL = 0
                    SCORE = 0
                    HEALTHPLAYER = 5
                    self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)
                    for enemy in level2Enemies:
                        level2Enemies.remove(enemy)

                elif not level2Enemies:
                    mixer.music.load("media/sounds/level_complete.wav")
                    mixer.music.play()
                    completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                    SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                    pygame.display.update()
                    time.sleep(8)
                    LEVEL = 3
                    pygame.display.update()

        # neu player cham vao Chicken
        for chicken in level3Enemies:
            if (pygame.sprite.collide_rect(self, chicken)):
                self.sound = mixer.Sound("media/sounds/playerbehit.wav")
                self.sound.play()
                level3Enemies.remove(chicken)
                HEALTHPLAYER -= 1
                SCORE += 30
                pygame.display.update()

                if (HEALTHPLAYER == 0):
                    self.sound = mixer.Sound("media/sounds/game_over_background_music.wav")
                    pygame.mixer.music.stop()
                    gameover_label = pygame.image.load("media/images/gameover_text.png")
                    SCREEN.blit(gameover_label, (SCREEN_WIDTH / 2 - 260, SCREEN_HEIGHT / 2 - 33))
                    pygame.display.update()
                    self.sound.play()
                    time.sleep(10)
                    LEVEL = 0
                    SCORE = 0
                    HEALTHPLAYER = 5
                    self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 330)
                    for enemy in level3Enemies:
                        level3Enemies.remove(enemy)

                elif not level3Enemies:
                    mixer.music.load("media/sounds/level_complete.wav")
                    mixer.music.play()
                    completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                    SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                    pygame.display.update()
                    time.sleep(8)
                    LEVEL = 4
                    pygame.display.update()

        # neu player cham vao Boss
        for boss in level4Enemies:
            if (pygame.sprite.collide_rect(self, boss)):
                self.sound = mixer.Sound("media/sounds/playerbehit.wav")
                self.sound.play()
                HEALTHPLAYER -= 1
                HEALTHBOSS -= 1
                self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                pygame.display.update()

                if (HEALTHPLAYER == 0):
                    self.sound = mixer.Sound("media/sounds/game_over_background_music.wav")
                    pygame.mixer.music.stop()
                    gameover_label = pygame.image.load("media/images/gameover_text.png")
                    SCREEN.blit(gameover_label, (SCREEN_WIDTH / 2 - 260, SCREEN_HEIGHT / 2 - 33))
                    pygame.display.update()
                    self.sound.play()
                    time.sleep(10)
                    LEVEL = 0
                    SCORE = 0
                    HEALTHPLAYER = 5
                    self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 330)
                    for enemy in level4Enemies:
                        level4Enemies.remove(enemy)

                elif not level4Enemies:
                    mixer.music.load("media/sounds/level_complete.wav")
                    mixer.music.play()
                    completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                    SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                    pygame.display.update()
                    time.sleep(8)
                    LEVEL = 0
                    self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)
                    pygame.display.update()

        # neu player cham vao SmallEgg
        for smallegg in smallEggList:
            if (pygame.sprite.collide_rect(self, smallegg)):
                self.sound = mixer.Sound("media/sounds/playerbehit.wav")
                self.sound.play()
                smallEggList.remove(smallegg)
                HEALTHPLAYER -= 1
                SCORE += 1
                pygame.display.update()

                if (HEALTHPLAYER == 0):
                    self.sound = mixer.Sound("media/sounds/game_over_background_music.wav")
                    pygame.mixer.music.stop()
                    gameover_label = pygame.image.load("media/images/gameover_text.png")
                    SCREEN.blit(gameover_label, (SCREEN_WIDTH / 2 - 260, SCREEN_HEIGHT / 2 - 33))
                    pygame.display.update()
                    self.sound.play()
                    time.sleep(10)
                    LEVEL = 0
                    SCORE = 0
                    HEALTHPLAYER = 5
                    self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 330)
                    for enemy in smallEggList:
                        smallEggList.remove(enemy)
                    for enemy in level4Enemies:
                        level4Enemies.remove(enemy)

class Game():

    def __init__(self):
        pygame.init()

        # FPS
        self.__FPS = 144

        # chinh sua cua so game
        icon = pygame.image.load("media/images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Chicken Invaders")

        # tao va set player o vi tri (x, y) (o giua + phia duoi man hinh)
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)


    def playIntro(self):
        # load nhac nen intro
        mixer.music.load("Media/Sounds/welcome_background_music.wav")
        mixer.music.play(-1)

        # load intro background image
        backgroundImage = pygame.image.load("media/images/galaxy_background_pixel_1280x800.jpg")
        introText = pygame.image.load("media/images/intro_text.png")
        introTitle = pygame.image.load("media/images/intro_title.png")
        introAuthor = pygame.image.load("media/images/intro_author.png")

        # hien thi thong tin o man hinh intro
        SCREEN.blit(backgroundImage, (0, 0))
        SCREEN.blit(introText, (((SCREEN_WIDTH/2) - 750/2), (SCREEN_HEIGHT/2) - 31/2 + 350))
        SCREEN.blit(introTitle, (((SCREEN_WIDTH/2) - 914/2), (SCREEN_HEIGHT/2) - 80/2 - 100))
        SCREEN.blit(introAuthor, (((SCREEN_WIDTH/2) - 750/2 + 80), (SCREEN_HEIGHT / 2) - 31/2 + 200))
        pygame.display.update()

        gameIsBeingOpened = True
        while (gameIsBeingOpened):

            # su kien tat cua so
            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingOpened = False
                    pygame.quit()

            # lang nghe
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # thay doi state cua game
                global LEVEL
                LEVEL = 1
                gameIsBeingOpened = False


    def playLevel1(self):
        # add player
        level1.add(self.player)

        # load nhac nen gameplay
        mixer.music.load("media/sounds/level1_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.transform.scale(pygame.image.load("media/images/play_background.jpg"), (1280, 800))

        # khai bao clock
        clock = pygame.time.Clock()

        # ra linh
        for i in range(12):
            level1Enemies.add(Egg())
        # --------------------------------------------------------------------------------------------------------------
        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            # Vong lap game: Su kien thay doi -> cap nhat va xu li thong tin -> ve lai game -> Su kien thay doi ...
            if (LEVEL == 0):
                gameIsBeingPlayed = False
            SCREEN.blit(backgroundImage, (0, 0))
            # thiet lap FPS
            clock.tick(self.__FPS)

            # su kien tat cua so window
            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()

                # player ban lazer bang phim SPACE
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        lazerList.add(Laser(self.player.rect.x, self.player.rect.y))
            # ----------------------------------------------------------------------------------------------------------
            ### lien tuc lang nghe su kien va thay doi:
            keys = pygame.key.get_pressed()
            #global LEVEL
            # di chuyen player
            if (keys[pygame.K_LEFT] and (self.player.rect.x > 0)):
                self.player.rect.x -= self.player.speed
            elif (keys[pygame.K_RIGHT] and (self.player.rect.x < (SCREEN_WIDTH - self.player.image.get_width()))):
                self.player.rect.x += self.player.speed
            elif (keys[pygame.K_UP] and self.player.rect.y > 0):
                self.player.rect.y -= self.player.speed
            elif (keys[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - self.player.image.get_height())):
                self.player.rect.y += self.player.speed
            elif (keys[pygame.K_RETURN] and LEVEL == 2):
                gameIsBeingPlayed = False

            #----------------------------------------------------------------------------------------------------------
            #### lien tuc ve lai game
            # ve thong tin diem so cua player
            mainFont = pygame.font.SysFont("comicsans", 40)
            scoreLabel = mainFont.render(f"Score: {SCORE}", 1, (255, 255, 255))
            SCREEN.blit(scoreLabel, (0, 0))
            # ve thong tin health cua player
            healthOfPlayerLabel = mainFont.render(f"Player's health: {HEALTHPLAYER}", 1, (255, 255, 255))
            SCREEN.blit(healthOfPlayerLabel, (0, 770))
            # ve thong tin level
            levelLabel = mainFont.render(f"Level: {LEVEL}", 1, (255, 255, 255))
            SCREEN.blit(levelLabel, (1175, 0))
            # ve chi dan qua level 2
            if (LEVEL == 2):
                hdchuyenlv_label = pygame.image.load("media/images/chidanqualevel_text.png")
                SCREEN.blit(hdchuyenlv_label, (SCREEN_WIDTH / 2 - 83, SCREEN_HEIGHT / 2 + 250))

            # draw va update cac SpriteGroup
            level1Enemies.draw(SCREEN)
            level1Enemies.update()

            level1.draw(SCREEN)
            level1.update()

            lazerList.draw(SCREEN)
            lazerList.update()

            chickenLegList.draw(SCREEN)
            chickenLegList.update()

            pygame.display.update()
            # ----------------------------------------------------------------------------------------------------------

    def playLevel2(self):
        # add player
        level2.add(self.player)
        # load nhac nen gameplay
        mixer.music.load("media/sounds/level2_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.transform.scale(pygame.image.load("media/images/level2_background.jpg"), (1280, 800))

        # khai bao clock
        clock = pygame.time.Clock()

        # ra linh
        for i in range(12):
            level2Enemies.add(UFO())
        # --------------------------------------------------------------------------------------------------------------
        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            global LEVEL
            if (LEVEL == 0):
                gameIsBeingPlayed = False
            # thiet lap FPS
            clock.tick(self.__FPS)

            SCREEN.blit(backgroundImage, (0, 0))

            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()

                # player ban lazer bang phim SPACE
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        lazerList.add(Laser(self.player.rect.x, self.player.rect.y))
            #-------------------------------------------------------------------------------------------------------
            ### lien tuc lang nghe su kien va thay doi:
            keys = pygame.key.get_pressed()
            #global LEVEL
            # di chuyen player
            if (keys[pygame.K_LEFT] and (self.player.rect.x > 0)):
                self.player.rect.x -= self.player.speed
            elif (keys[pygame.K_RIGHT] and (self.player.rect.x < (SCREEN_WIDTH - self.player.image.get_width()))):
                self.player.rect.x += self.player.speed
            elif (keys[pygame.K_UP] and self.player.rect.y > 0):
                self.player.rect.y -= self.player.speed
            elif (keys[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - self.player.image.get_height())):
                self.player.rect.y += self.player.speed
            elif (keys[pygame.K_RETURN] and LEVEL == 3):
                gameIsBeingPlayed = False
            # ----------------------------------------------------------------------------------------------------------
            #### lien tuc ve lai game
            # ve thong tin diem so cua player
            mainFont = pygame.font.SysFont("comicsans", 40)
            scoreLabel = mainFont.render(f"Score: {SCORE}", True, (255, 255, 255))
            SCREEN.blit(scoreLabel, (0, 0))
            # ve thong tin health cua player
            healthOfPlayerLabel = mainFont.render(f"Player's health: {HEALTHPLAYER}", 1, (255, 255, 255))
            SCREEN.blit(healthOfPlayerLabel, (0, 770))
            # ve thong tin level
            levelLabel = mainFont.render(f"Level: {LEVEL}", 1, (255, 255, 255))
            SCREEN.blit(levelLabel, (1175, 0))
            # ve chi dan qua level 3
            if (LEVEL == 3):
                hdchuyenlv_label = pygame.image.load("media/images/chidanqualevel_text.png")
                SCREEN.blit(hdchuyenlv_label, (SCREEN_WIDTH / 2 - 83, SCREEN_HEIGHT / 2 + 200))

            level2Enemies.draw(SCREEN)
            level2Enemies.update()

            level2.draw(SCREEN)
            level2.update()

            lazerList.draw(SCREEN)
            lazerList.update()

            chickenLegList.draw(SCREEN)
            chickenLegList.update()

            pygame.display.update()
            # ----------------------------------------------------------------------------------------------------------

    def playLevel3(self):
        # add player
        level3.add(self.player)
        # load nhac nen gameplay
        mixer.music.load("media/sounds/level3_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.transform.scale(pygame.image.load("media/images/level3_background.jpg"), (1280, 800))

        # khai bao clock
        clock = pygame.time.Clock()

        # ra linh
        for i in range(12):
            level3Enemies.add(Chicken())
        # --------------------------------------------------------------------------------------------------------------
        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            global LEVEL
            if (LEVEL == 0):
                gameIsBeingPlayed = False
            # thiet lap FPS
            clock.tick(self.__FPS)

            SCREEN.blit(backgroundImage, (0, 0))

            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()

                # player ban lazer bang phim SPACE
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        lazerList.add(Laser(self.player.rect.x, self.player.rect.y))
            #-------------------------------------------------------------------------------------------------------
            ### lien tuc lang nghe su kien va thay doi:
            keys = pygame.key.get_pressed()
            #global LEVEL
            # di chuyen player
            if (keys[pygame.K_LEFT] and (self.player.rect.x > 0)):
                self.player.rect.x -= self.player.speed
            elif (keys[pygame.K_RIGHT] and (self.player.rect.x < (SCREEN_WIDTH - self.player.image.get_width()))):
                self.player.rect.x += self.player.speed
            elif (keys[pygame.K_UP] and self.player.rect.y > 0):
                self.player.rect.y -= self.player.speed
            elif (keys[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - self.player.image.get_height())):
                self.player.rect.y += self.player.speed
            elif (keys[pygame.K_RETURN] and LEVEL == 4):
                gameIsBeingPlayed = False
            # ----------------------------------------------------------------------------------------------------------
            #### lien tuc ve lai game
            # ve thong tin diem so cua player
            mainFont = pygame.font.SysFont("comicsans", 40)
            scoreLabel = mainFont.render(f"Score: {SCORE}", True, (255, 255, 255))
            SCREEN.blit(scoreLabel, (0, 0))
            # ve thong tin health cua player
            healthOfPlayerLabel = mainFont.render(f"Player's health: {HEALTHPLAYER}", 1, (255, 255, 255))
            SCREEN.blit(healthOfPlayerLabel, (0, 770))
            # ve thong tin level
            levelLabel = mainFont.render(f"Level: {LEVEL}", 1, (255, 255, 255))
            SCREEN.blit(levelLabel, (1175, 0))
            # ve chi dan qua level 3
            if (LEVEL == 4):
                hdchuyenlv_label = pygame.image.load("media/images/chidanqualevel_text.png")
                SCREEN.blit(hdchuyenlv_label, (SCREEN_WIDTH / 2 - 83, SCREEN_HEIGHT / 2 + 200))

            level3Enemies.draw(SCREEN)
            level3Enemies.update()

            level3.draw(SCREEN)
            level3.update()

            lazerList.draw(SCREEN)
            lazerList.update()

            chickenLegList.draw(SCREEN)
            chickenLegList.update()

            pygame.display.update()
            # ----------------------------------------------------------------------------------------------------------

    def playLevel4(self):
        # add player
        level4.add(self.player)
        # load nhac nen gameplay
        mixer.music.load("media/sounds/level_boss_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.transform.scale(pygame.image.load("media/images/level4_background.jpg"), (1422, 800))

        # khai bao clock
        clock = pygame.time.Clock()

        # ra boss
        level4Enemies.add(Boss())

        # --------------------------------------------------------------------------------------------------------------
        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            global LEVEL
            if (LEVEL == 0):
                gameIsBeingPlayed = False
            # thiet lap FPS
            clock.tick(self.__FPS)

            SCREEN.blit(backgroundImage, (0, 0))

            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()

                # player ban lazer bang phim SPACE
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        lazerList.add(Laser(self.player.rect.x, self.player.rect.y))
            #-------------------------------------------------------------------------------------------------------
            ### lien tuc lang nghe su kien va thay doi:
            keys = pygame.key.get_pressed()
            #global LEVEL
            # di chuyen player
            if (keys[pygame.K_LEFT] and (self.player.rect.x > 0)):
                self.player.rect.x -= self.player.speed
            elif (keys[pygame.K_RIGHT] and (self.player.rect.x < (SCREEN_WIDTH - self.player.image.get_width()))):
                self.player.rect.x += self.player.speed
            elif (keys[pygame.K_UP] and self.player.rect.y > 0):
                self.player.rect.y -= self.player.speed
            elif (keys[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - self.player.image.get_height())):
                self.player.rect.y += self.player.speed
            elif (keys[pygame.K_RETURN] and LEVEL == 5):
                gameIsBeingPlayed = False
            # ----------------------------------------------------------------------------------------------------------
            #### lien tuc ve lai game
            # ve thong tin diem so cua player
            mainFont = pygame.font.SysFont("comicsans", 40)
            scoreLabel = mainFont.render(f"Score: {SCORE}", True, (255, 255, 255))
            SCREEN.blit(scoreLabel, (0, 0))
            # ve thong tin health cua player
            healthOfPlayerLabel = mainFont.render(f"Player's health: {HEALTHPLAYER}", 1, (255, 255, 255))
            SCREEN.blit(healthOfPlayerLabel, (0, 770))
            # ve thong tin level
            levelLabel = mainFont.render(f"Level: {LEVEL}", 1, (255, 255, 255))
            SCREEN.blit(levelLabel, (1175, 0))
            # ve thong tin health cua boss
            healthBossLabel = mainFont.render(f"Boss's health: {HEALTHBOSS}", 1, (255, 255, 255))
            SCREEN.blit(healthBossLabel, (0, 50))
            # ve chi dan qua level 3
            if (LEVEL == 5):
                hdchuyenlv_label = pygame.image.load("media/images/chidanqualevel_text.png")
                SCREEN.blit(hdchuyenlv_label, (SCREEN_WIDTH / 2 - 83, SCREEN_HEIGHT / 2 + 200))

            level4Enemies.draw(SCREEN)
            level4Enemies.update()

            level4.draw(SCREEN)
            level4.update()

            lazerList.draw(SCREEN)
            lazerList.update()

            smallEggList.draw(SCREEN)
            smallEggList.update()

            pygame.display.update()
            # ----------------------------------------------------------------------------------------------------------


    def start(self):
        while (True):
            global LEVEL
            if (LEVEL == 0):
                self.playIntro()
            elif (LEVEL == 1):
                self.playLevel1()
            elif (LEVEL == 2):
                self.playLevel2()
            elif (LEVEL == 3):
                self.playLevel3()
            elif (LEVEL == 4):
                self.playLevel4()


gameOb = Game()
gameOb.start()