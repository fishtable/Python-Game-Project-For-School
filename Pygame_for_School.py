#Created by Ethan Nauta
#Bring in pygame module
import pygame, sys

pygame.init()

#define screen size and amount of tiles on screen
screen_x = 800
screen_y = 400
screen = pygame.display.set_mode((screen_x, screen_y))

#create a matrix of size screen to fit all 100x100 tiles
matrix_columns = int(16)
matrix_rows = int(16)
matrix_column_count = 0
matrix_row_count = 0
matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0],
          [0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0],
          [0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0],
          [0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0],
          [0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0],
          [0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0],
          [0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0],
          [0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,0],
          [0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
          [0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0],
          [0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
          [0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,0],
          [0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0],
          [0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]


#initialize player object, a yellow 50 pixel by 50 pixel square.
test_surface = pygame.Surface((50, 50))
test_surface.fill(pygame.Color("gold"))

clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

#x position of the player object.
x_pos = 0
y_pos = 0

#state of players available keyboard inputs.
w_state = 0
a_state = 0
s_state = 0
d_state = 0

#players speed in the game
x_speed = 10
y_speed = 10

#allow us to push player without interrupting controls
x_collide = 0
y_collide = 0


#core loop
while True:
    
    #at the start of every step of the game, check for all events.
    for event in pygame.event.get():
        
        #assures game will be completely closed.
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
       
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                
                w_state = -1
            if event.key == pygame.K_a:
                
                a_state = -1
            if event.key == pygame.K_s:
                
                s_state = 1
            if event.key == pygame.K_d:
            
                d_state = 1
                
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_w:
                
                w_state = 0
            if event.key == pygame.K_a:
                
                a_state = 0
            if event.key == pygame.K_s:
                
                s_state = 0
            if event.key == pygame.K_d:
            
                d_state = 0
                

            
    #either pass a pygame base color or a RGB tuple
    screen.fill(pygame.Color("blue"))
    
    
    #for each row, adjust the position of each tile in each column
    for rows in range(matrix_rows):
        
        for columns in range(matrix_columns):

                
            if matrix[rows][columns] == 0:
                
                #if check left true, then left of box is in player hitbox
                #if check right true, then right of box is in player hitbox
                check_left = (columns*100 - x_pos > 375 and columns*100 - x_pos < 425)
                check_right = (columns*100 - x_pos + 100 > 375 and columns*100 - x_pos + 100 < 425)
                
                #if check top true, then top of box is in the player hitbox
                #if check bottom true, then bottom of box is in the player hitbox
                check_top = (rows*100 - y_pos > 175 and rows*100 - y_pos < 225)
                check_bottom = (rows*100 - y_pos + 100 > 175 and rows*100 - y_pos + 100 < 225)
             
                #if player is in y range of square, can trigger x collisions
                check_y = (rows*100 - y_pos >= 75 and rows*100 - y_pos <= 225)
                check_x = (columns*100 - x_pos >= 275 and columns*100 - x_pos <= 425)

                
                if check_left and check_y:
                        
                    #checks which side of the player the block is hitting
                    dist_check_left = ((columns*100 - x_pos)-375)**2
                    
                    #if closer to left of player
                    if dist_check_left < 625:
                        
                        #side of player block is colliding with
                        print("left of player!")
                        x_collide = 10
                        
                    if dist_check_left >= 625:
                        
                        #side of player block is colliding with
                        print("right of player!")
                        x_collide = -10
                        
                if check_right and check_y:
                    
                    #checks which side of the player the block is hitting
                    dist_check_right = ((columns*100 - x_pos + 100)-375)**2
                    
                    #if closer to left of player
                    if dist_check_right < 625:
                        
                        #side of player block is colliding with
                        print("left of player!")
                        x_collide = 10
                        
                    if dist_check_right >= 625:
                        
                        #side of player block is colliding with
                        print("right of player!")
                        x_collide = 10
                        
                if check_top and check_x:
                    
                    #checks which side of the player the block is hitting
                    dist_check_top = ((rows*100 - y_pos)-175)**2
                   
                    #if closer to left of player
                    if dist_check_top < 625:
                           
                        #side of player block is colliding with
                        print("top of player!")
                        y_collide = 10
                        
                    if dist_check_top >= 625:
                        
                        #side of player block is colliding with
                        print("bottom of player!")
                        y_collide = -10
                        
                if check_bottom and check_x:
                    
                    #checks which side of the player the block is hitting
                    dist_check_bottom = ((rows*100 - y_pos + 100)-175)**2
                   
                    #if closer to left of player
                    if dist_check_bottom < 625:
                           
                        #side of player block is colliding with
                        print("top of player!")
                        y_collide = 10
                        
                    if dist_check_bottom >= 625:
                        
                        #side of player block is colliding with
                        print("bottom of player!")
                        y_collide = 10
                        
            if matrix[rows][columns] == 1:
                
                grass = pygame.Surface((100,100))
                grass.fill(pygame.Color("green"))
                
                screen.blit(grass, (columns*100 - x_pos, rows*100 - y_pos))
                
            if matrix[rows][columns] == 0:
                
                water = pygame.Surface((100,100))
                water.fill(pygame.Color("white"))
                
                screen.blit(water, (columns*100 - x_pos, rows*100 - y_pos))
                
                    
                        
                
            columns += 1
        
        rows += 1
             
        
    
    #if a and d active, dont move, else move
    x_pos += (a_state + d_state)*x_speed
    y_pos += (w_state + s_state)*y_speed
    
    
    #pushes the player in the direction of the collide factor
    x_pos += x_collide
    y_pos += y_collide
    
    x_collide = 0
    y_collide = 0
    
    
    #Positions the test surface on the screen relative to top left of object
    screen.blit(test_surface,(0.5*screen_x - 25, 0.5*screen_y - 25))
    
    #draw all elems each step
    pygame.display.update()
    
    #sets the fps of the game, game may still run too slow.
    clock.tick(30)