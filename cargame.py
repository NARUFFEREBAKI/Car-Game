import pygame
import random 
from pygame.locals import *

size=width,height=(900,600)
road_w=int(width/2)
road_mark=int(width/80)

right_lane=width/2+road_w/4
left_lane=width/2-road_w/4
speed=1


pygame.init()
running=True

screen=pygame.display.set_mode(size)
pygame.display.set_caption("CAR GAME")
screen.fill((150,220,60))




pygame.display.update()

car=pygame.image.load(r"D:\projects python\car game\car.png")
car_loc=car.get_rect()  
car_loc.center=left_lane,height*0.75

car2=pygame.image.load(r"D:\projects python\car game\car2.png")
car2_loc=car.get_rect()  
car2_loc.center=right_lane,height*0.2 

counter=0
while running:
    counter+=1
    if counter==1000:
        speed+=0.25
        counter=0
        print("FASTER BABY!!!",speed)
    car2_loc[1]+=speed
    if car2_loc[1]>height:
        
        # if random.randint(0,1)==0:
        #     car2_loc.center=left_lane,-200
        # else:
        #     car2_loc.center=right_lane,-200
        car2_loc.center=random.choice([left_lane,right_lane]),-200
    #end_game
    if car_loc[0]==car2_loc[0] and car2_loc[1]>car_loc[1]-200:
        print("game over you lost")
        break

    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==KEYDOWN:
            if event.key in [K_a, K_LEFT]:  
                if car_loc.left > road_w/2:   
                     car_loc = car_loc.move(-int(road_w / 2), 0)  
            if event.key in [K_d, K_RIGHT]:  
                if car_loc.right < road_w / 2 + road_mark*2+road_w/2:  # Use < instead of >  
                    car_loc = car_loc.move(int(road_w / 2), 0) 

            
    pygame.draw.rect(
        screen,
        (30,30,30),
        (width/2-road_w/2,0,road_w,height)
    )

    pygame.draw.rect(
        screen,
        (255,240,60),
        (width/2-road_mark/2,0,road_mark,height)
    )

    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2-road_w/2+road_mark,0,road_mark,height)
    )
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2+road_w/2-road_mark*2,0,road_mark,height)
    )

    screen.blit(car,car_loc)
    screen.blit(car2,car2_loc)
    pygame.display.update()

print("your score is : ",speed*100)




pygame.quit()
