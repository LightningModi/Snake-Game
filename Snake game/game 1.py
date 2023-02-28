import pygame
import random
import os

pygame.mixer.init()
pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 200)
purple = (59, 43, 104)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font=pygame.font.SysFont(None, 55)

inimg=pygame.image.load("intro.png")
inimg=pygame.transform.scale(inimg, (screen_width/3, screen_height/2.7)).convert_alpha()

enimg=pygame.image.load("enter.png")
enimg=pygame.transform.scale(enimg, (screen_width/3, screen_height/5.5)).convert_alpha()
  
bgimg=pygame.image.load("top-view-dry-grass.jpg")
bgimg=pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

sg=pygame.image.load("sg.png")
sg=pygame.transform.scale(sg, (screen_width/2, screen_height/7)).convert_alpha()

def welcome():
    pygame.mixer.music.load("Undertale Start Menu.mp3")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        
        gameWindow.fill(purple)
        gameWindow.blit(sg, (220,70))
        gameWindow.blit(inimg, (300,170))
        gameWindow.blit(enimg, (300, 450))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
                
        pygame.display.update()
        clock.tick(60)

def text_screen(text,color,x,y):
    screen_text=font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
                    


'''Game Loop'''
def gameloop():
    
    L=["Castlevania_ Bloodlines.mp3",
       "One Must Fall 2097.mp3",
       "Sonic 2 - Chemical Plant Zone.mp3",
       "Kirby's Return to Dream Land.mp3",
       "Klagmar's Top VGM.mp3",
       "Cirno Fortress Stage 2.mp3",
       "Undertale - Megalovania.mp3"]
    filename = random.choice(L)
    pygame.mixer.music.load( filename )
    pygame.mixer.music.play()

    exit_game = False
    game_over = False
    snake_x = 100
    snake_y = 100
    v_x=0
    v_y=0


    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_width/2)
    score=0
    v=10

    snake_size = 20
    fps = 30
    snk_list=[]
    snk_length=1

    if (not os.path.exists("High_Score.txt")):
        f=open("High_Score.txt","w")
        f.write("0")
        f.close()
    
    f=open("High_Score.txt", "r")
    HS=f.read()
    f.close()  

    while not exit_game:
        
        if game_over:
            f=open("High_Score.txt", "w")
            f.write(str(HS))
            f.close()
            gameWindow.fill(black)
            text_screen("Game Over!!!", red, screen_width/2.8, screen_height/3)
            text_screen("Press ENTER to Continue", red, screen_width/4, screen_height/2)
            text_screen("Your score:", white, screen_width/4, screen_height/1.5 + 50)
            text_screen("High score:", white, screen_width/4, screen_height/1.5)
            text_screen(str(score), blue, 450, screen_height/1.5 + 50)
            text_screen(str(HS), blue, 450, screen_height/1.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                    
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        v_x=v
                        v_y=0
                    if event.key == pygame.K_LEFT:
                        v_x=-v
                        v_y=0
                    if event.key == pygame.K_UP:
                        v_x=0
                        v_y=-v
                    if event.key == pygame.K_DOWN:
                        v_x=0
                        v_y=v
            snake_x=snake_x+v_x
            snake_y=snake_y+v_y

            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                
                score+=10
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(10,screen_width/2)
                snk_length+=5
                if score>int(HS):
                    HS=score
                       

            gameWindow.fill(white)
            
            
            
            gameWindow.blit(bgimg, (0,0)) 
            text_screen("score: "+str(score)+ "  High Score: "+str(HS), red, 5, 5)
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])


            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)



            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("Ending.mp3")
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("Ending.mp3")
                pygame.mixer.music.play()              
            
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()


