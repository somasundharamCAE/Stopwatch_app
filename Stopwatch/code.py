#Stopwatch App

import pygame
import time
from pygame.locals import *

class preview():
    def __init__(self,window):
        self.stopwatch_img=pygame.image.load("stopwatch.png").convert()
        self.start_img=pygame.image.load("start.png").convert()
        self.start_img_2=pygame.image.load("start_2.png").convert()
        self.start_image_rect = self.start_img.get_rect(topleft=(200,400))
        self.screen=window

    def draw(self):
        self.screen.fill((135, 168, 50))
        self.screen.blit(self.stopwatch_img,(150,100))

class timer:
    def __init__(self,window):
        self.screen=window
        self.clock=pygame.time.Clock()
        self.clock.tick(60.0)
        self.pause_button=pygame.image.load("pause.jpg").convert()
        self.pause_rect=self.pause_button.get_rect(topleft=(200,400))
        self.pause_button_2=pygame.image.load("pause_2.png").convert()

    def draw(self,sec,min):
        self.screen.fill((135, 168, 50))
        line_1=pygame.font.SysFont('arial',90)
        timer_text=line_1.render(f"{min}:{sec}",True,(61, 51, 56))
        self.screen.blit(timer_text,(200,200))

class freeze:
    def __init__(self,window):
        self.screen=window
        self.restart_button=pygame.image.load("restart.jpg").convert()
        self.restart_rect=self.restart_button.get_rect(topleft=(200,400))
        self.restart_button_2=pygame.image.load("restart_2.png").convert()

    def draw(self,sec,min):
        self.screen.fill((135, 168, 50))
        line_1=pygame.font.SysFont('arial',90)
        timer_text=line_1.render(f"{min}:{sec}",True,(61, 51, 56))
        self.screen.blit(timer_text,(200,200))

class stopwatch:
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode((500,750))
        pygame.display.set_caption("Stopwatch")
        self.c_preview=preview(self.window)
        self.c_timer=timer(self.window)
        self.c_freeze=freeze(self.window)
        self.start=False
        self.click_count=0
        self.screen_freeze=False
        self.preview=True
        self.reset=False


    def collision(self,button_rect,button_img_1,button_img_2):
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            self.window.blit(button_img_2,button_rect)
            if pygame.mouse.get_pressed()[0] ==1 and self.click_count==0:
                if self.preview:
                    self.start=True
                    self.preview=False
                    self.start_time=pygame.time.get_ticks()
                elif self.start:
                    self.screen_freeze=True
                    self.start=False
                elif self.screen_freeze:
                    self.screen_freeze=False
                    self.reset=True
                self.click_count=1
        else:
            self.window.blit(button_img_1,button_rect)
            self.click_count=0

    def game_reset(self):
        self.start=False
        self.screen_freeze=False
        self.preview=True


    def game_run(self):
        run=True
        sec=0
        min=0
        while run:
            if not self.start and self.preview:
                self.c_preview.draw()
                self.collision(self.c_preview.start_image_rect,self.c_preview.start_img,self.c_preview.start_img_2)
                pygame.display.update()

            elif self.start:
                current_time=pygame.time.get_ticks()
                if (current_time-self.start_time)//1000 == 1:
                    sec+=1
                    self.start_time=pygame.time.get_ticks()
                self.c_timer.draw(sec,min)
                if sec==60:
                    min+=1
                    sec=0
                self.collision(self.c_timer.pause_rect,self.c_timer.pause_button,self.c_timer.pause_button_2)
                pygame.display.update()

            elif self.screen_freeze:
                self.c_freeze.draw(sec,min)
                self.collision(self.c_freeze.restart_rect,self.c_freeze.restart_button,self.c_freeze.restart_button_2)
                pygame.display.update()
            
            elif self.reset:
                self.game_reset()
                sec=0
                pygame.display.update()

            for event in pygame.event.get():
                if event.type==QUIT:
                    run=False
        pygame.quit()

if __name__=='__main__':
    game=stopwatch()
    game.game_run()