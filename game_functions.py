import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	'''响应按键'''
	if event.key == pygame.K_RIGHT:
			ship.moving_right = True
	if event.key == pygame.K_LEFT:
			ship.moving_left = True
	if event.key == pygame.K_SPACE:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	'''响应按键'''
	if event.key == pygame.K_RIGHT:
			ship.moving_right = False
	if event.key == pygame.K_LEFT:
			ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	'''响应键盘鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
			

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)



def update_screen(ai_settings, screen, ship, bullets):
	'''更新屏幕上图像，并切换到新屏幕'''
	#每次循环时重绘屏幕
	screen.fill(ai_settings.bg_color)
	
	#让最近的屏幕可见
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	pygame.display.flip()
