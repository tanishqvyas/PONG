#game_dev using pygame to make a game of pong ball

import os
import pygame
from pygame.locals import*
import time
#def play_ball():
clock = pygame.time.Clock()

def pause_screen():
	
	pygame.init()

	click_done = 1

	display = pygame.display.set_mode((1300,750),0,30)
	pygame.display.set_caption('XD BALLZ')

	while click_done:
		mouse_click = pygame.mouse.get_pressed()[0]

		mouse_pos = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()

		display.fill((0,200,200))	

		myFont = pygame.font.SysFont("Times New Roman", 50)	
		msg = myFont.render("CLICK ANYWHERE TO RESUME", 1, (0,0,0))
		
		if mouse_click:
			click_done = 0


		display.blit(msg,(250,250))

		pygame.display.update()

def play_xdball():
	#PYGAME INITIALIZATION...........................................................
	pygame.init()

	#DEFINNING RSULTS DISPLAYING FUNCTION............................................
	
	
	def result(x):
		highscore = open("highscore.txt","r")
		
		if x > int(highscore.readline())+1:
			highscore.close()
			highscore = open("highscore.txt","w")
			highscore.write(str(x))
			highscore.close()
			myFont = pygame.font.SysFont("Times New Roman", 90)	
			print_score = myFont.render("NEW HIGHSCORE !!! ", 1, (0,0,255))
			final_score = myFont.render(str(x), 1, (0,0,255))
			display.blit(print_score,(120,200))
			display.blit(final_score,(450,450))
			pygame.display.update()
			time.sleep(2)
		
		else:
			myFont = pygame.font.SysFont("Times New Roman", 100)	
			print_score = myFont.render("YOUR SCORE : ", 1, (0,0,255))
			final_score = myFont.render(str(x), 1, (0,0,255))
			display.blit(print_score,(250,200))
			display.blit(final_score,(450,450))
			pygame.display.update()
			time.sleep(2)

	posx1 = 450
	posx2 = 1100
	optimization_const = True
	speed = 8
	ball_speed = [10,10]
	highlight_height = 450
	#MANAGING THE DISPLAY
	display = pygame.display.set_mode((1300,750),0,30)
	pygame.display.set_caption('XD BALLZ')
	#managing pause play staus...........
	game_status = True #TRUE WHEN PLAYING....................
	#IMAGE LOADING.......
	bar1 = pygame.image.load('bar.png')
	bar2 = pygame.image.load('bar.png')
	midline = pygame.image.load('midline.png') 
	ball = pygame.image.load('ball.png')
	scoreboard = pygame.image.load('scoreboard.png')
	playgame = pygame.image.load('playgame.png')
	pausegame = pygame.image.load('pausegame.png')
	quitgame = pygame.image.load('quit.png')
	highlighter = pygame.image.load('highlighter.png')
	#taking the ball's rectangle frame
	ballrect = ball.get_rect()
	status_pause = True       #True when game is paused
	speed_changer = 0
	first_handling = 0
	score = 0

	highscore = open("highscore.txt","r")
	curr_highscore = int(highscore.readline())
	highscore.close()
	#MAIN LOOP...................

	fps = 0
	time = 0

	while True:
		mouse_click = pygame.mouse.get_pressed()[0]

		mouse_pos = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()

	
		pressed_key1 = pygame.key.get_pressed()
		myfont = pygame.font.SysFont("monospace", 16)
		
		
		if pressed_key1[K_LEFT]:
			posx1 -= speed
		elif pressed_key1[K_RIGHT]:
			posx1 += speed
		
		#ADDING ALL SORTS OF BOUNDARY CONDITIONS..................
		#main boundaries of screen................................
		if posx1 < 0:
			posx1 = 0
		if posx1 > 1000:
			posx1 = 1000
		if posx2 > 1000:
			posx2 = 1000
		if posx2 < 0:
			posx2 = 0
	
		#getting the co ordinates of the ball in the form of the co ordinates of the sides of square in which its enclosed
		ballrect = ballrect.move(ball_speed)
		#managing the bouncing back of ball as it hits the walls and bars....................................................
		if (ballrect.left < 0 or ballrect.right > 1200):
			ball_speed[0] =- ball_speed[0]
		if (ballrect.top < 50 and ballrect.left in range(posx2-50,posx2+251) ) or (ballrect.bottom > 700 and ballrect.left in range(posx1-50,posx1+251) ):
			ball_speed[1] =- ball_speed[1]
	

		#managing the computer's bar...........................................(basically code to make bar move on its own as the ball moves )

		if ballrect.left in range(1000,1100):
			posx2 = 1000
		if ballrect.left in range(100,1001):
			posx2 = ballrect.left - 100
		if ballrect.left in range(0,100):
			posx2 = 0

		#just preventing the game to stop in the beginning
		if first_handling in range(0,100):
			posx2 = 400		
			first_handling += 1
		#highlighting the selected button as the mouse hovers above it.................................	
		if mouse_pos[0] in range(1200,1300) and mouse_pos[1] in range(450,600):
			highlight_height = 450
			pygame.display.update()
		if mouse_pos[0] in range(1200,1300) and mouse_pos[1] in range(600,750):
			highlight_height = 600
			pygame.display.update()
		#score updation..........................................................
		if ballrect.bottom > 700 and ballrect.left in range(posx1-50,posx1+251):
			score += 10	
		myFont = pygame.font.SysFont("Times New Roman", 15)	
		print_score = myFont.render("SCORE : ", 1, (0,0,0))
		current_score = myFont.render(""+str(score), 1, (0,0,0))
		if (curr_highscore - score > 0):
			rem_score = myFont.render(str(curr_highscore-score), 1, (200,200,200))
		else:
			rem_score = myFont.render("GOOD JOB!", 1, (200,200,200))	
		



		#QUIT HANDLING
		if (mouse_pos[0] in range(1200,1300) and mouse_pos[1] in range(600,750)) and mouse_click:
			menu()
		#pause button...............................
		if (mouse_pos[0] in range(1200,1300) and mouse_pos[1] in range(450,600)) and mouse_click:
			pause_screen()	

		if (fps %87 == 0):
			time += 1
		disp_time = myFont.render(str(time), 1, (0,0,0))
		clock_time = myFont.render("TIME : ", 1, (0,0,0))			
		fps += 1
		 
		#DISPLAYING THE UPDATED SCREEN AFTER KEYS ARE PRESSED

		display.fill((0,0,0))      # 0 for red , green and blue to get black background
	
		#displaying mid line..................................................................
		display.blit(midline,(0,375))
		#displaying the bars..................................................................
		display.blit(bar1,(posx1,700))
		display.blit(bar2,(posx2,0))
		display.blit(ball,ballrect)
		display.blit(scoreboard,(1200,0))
		display.blit(print_score,(1221,50))
		display.blit(current_score,(1221,100))	
	
		display.blit(rem_score,(1221,400))
		display.blit(disp_time,(1221,250))
		display.blit(clock_time,(1221,220))

		display.blit(playgame,(1200,300))
		display.blit(pausegame,(1200,450))
		display.blit(quitgame,(1200,600))	
		display.blit(highlighter,(1200,highlight_height))
		display.blit(rem_score,(1212,350))

		if ballrect.bottom == 750:	
			result(score)
			menu()

		pygame.display.update()	

def how_to_play():
	pygame.init()
	display = pygame.display.set_mode((1000,600),0,30)
	howtoplay_mannual = pygame.image.load('howtoplayimage.png')	
	
	while True:
		mouse_click = pygame.mouse.get_pressed()[0]

		mouse_pos = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
		
		
		if (mouse_pos[0] in range(800,1000) and mouse_pos[1] in range(530,600)) and mouse_click:
			menu_ball()
		display.blit(howtoplay_mannual,(0,0))
		pygame.display.update()



		
def menu_ball():
	pygame.init()
	display = pygame.display.set_mode((1000,600),0,30)
	
	highlight_height = 100 #controls the highlighting of the correct option	

	#image loading stuff 
	menu_bg = pygame.image.load('menubackground.png')
	play = pygame.image.load('play.png')
	howtoplay = pygame.image.load('howtoplay.png')
	quit_game = pygame.image.load('quitgame.png')
	highlight = pygame.image.load('highlight.png')

#game loop..................................................................	
	while True:
		mouse_click = pygame.mouse.get_pressed()[0]

		mouse_pos = pygame.mouse.get_pos()
		pressed_key = pygame.key.get_pressed()	
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
		if (mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>100 and mouse_pos[1]<150):
			highlight_height = 100
			clock.tick(10)
		if (mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>200 and mouse_pos[1]<250):
			highlight_height = 200
			clock.tick(10)
		if (mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>300 and mouse_pos[1]<350):
			highlight_height = 300
			clock.tick(10)
		
		if ((mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>100 and mouse_pos[1]<150)) and mouse_click:                  #opens robo menu
			display.blit(menu_bg,(0,0))
			clock.tick(10)

			pygame.display.update()
		
			play_xdball()	
		if((mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>200 and mouse_pos[1]<250)) and mouse_click:                      #how to play
			display.blit(menu_bg,(0,0))
			clock.tick(10)
			how_to_play()
			pygame.display.update()
		
		if ((mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>300 and mouse_pos[1]<350)) and mouse_click:                       # quit
			pygame.quit()
			quit()
				
	
		#Displaying all stuff..............

		display.blit(menu_bg,(0,0))
		display.blit(play,(400,100))
		display.blit(howtoplay,(400,200))
		display.blit(quit_game,(400,300))
		display.blit(highlight,(400,highlight_height))
		pygame.display.update()









def menu():

	#pygame initialization
	pygame.init()
	display = pygame.display.set_mode((1000,600),0,30)
	pygame.display.set_caption("game")	
	#IMAGE LOADING OF menu

	#variables......................
	
	highlight_height = 100

	menu_bg = pygame.image.load('menubackground.png')
	gamelist = pygame.image.load('gamelist.png')
	quit_game = pygame.image.load('quitgame.png')
	highlight = pygame.image.load('highlight.png')
	while True:
		mouse_click = pygame.mouse.get_pressed()[0]		 
		mouse_pos = pygame.mouse.get_pos()		
		pressed_key = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
		
		if (mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>100 and mouse_pos[1]<150):

			highlight_height = 100
			clock.tick(10)
		if (mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>200 and mouse_pos[1]<250):
			highlight_height = 200
			clock.tick(10)

		if  ((mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>100 and mouse_pos[1]<150)) and mouse_click:
			display.blit(menu_bg,(0,0))
			clock.tick(10)
			pygame.display.update()
			menu_ball()
		if ((mouse_pos[0]>400 and mouse_pos[0]<600) and (mouse_pos[1]>200 and mouse_pos[1]<250)) and mouse_click:
			pygame.quit()
			quit()

		display.blit(menu_bg,(0,0))
		display.blit(gamelist,(400,100))
		display.blit(quit_game,(400,200))	
		display.blit(highlight,(400,highlight_height))

		pygame.display.update()
menu()	

