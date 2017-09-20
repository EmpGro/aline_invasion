import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#初始化并创建一个游戏对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船
	ship = Ship(screen,ai_settings)

	#创建一个子弹编组
	bullets = Group()

	#开始游戏主循环
	while True:

		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()

		#删除已经消失的子弹
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets) ,end='')

		gf.update_screen(ai_settings, screen, ship, bullets)

		
run_game()
