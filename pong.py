import pygame

pygame.init()

#Makes a black screen pop-up
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  

#Need this to change the FPS (frames per second) later.
clock = pygame.time.Clock()

#Ball
ball_x_position = screen_width / 2
ball_y_position = screen_height / 2
ball_x_direction = -1 # (1) = right and (-1) = left
ball_y_direction = 1
ball_width = 10
ball_height = 10
ball_speed = 4

#Player 1
p1_x_position = 30
p1_y_position = screen_height/2
p1_width=10
p1_height=60
p1_speed = 5

#Player 2
p2_x_position = screen_width - 40
p2_y_position = screen_height/2
p2_width=10
p2_height=60
p2_speed = 5

#Game Loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Move p1 paddle up or down
    if pygame.key.get_pressed()[pygame.K_a] and p1_y_position >= 0: 
        p1_y_position -= p1_speed
    if pygame.key.get_pressed()[pygame.K_z] and p1_y_position + p1_height <= screen_height: 
        p1_y_position += p1_speed

    #Move p2 paddle up or down
    if pygame.key.get_pressed()[pygame.K_UP] and p2_y_position >= 0:
        p2_y_position -= p2_speed
    if pygame.key.get_pressed()[pygame.K_DOWN] and p2_y_position + p2_height <= screen_height:
        p2_y_position += p2_speed
    
    ball_x_position += ball_speed*ball_x_direction
    ball_y_position += ball_speed*ball_y_direction





    #top-collision
    if ball_y_position < 0: ball_y_direction = 1


    #bottom-collision
    if ball_y_position > screen_height - ball_height: ball_y_direction = -1


    #left-collision
    ball_hits_p1_x_dimension = ball_x_position <= 40 and ball_x_position >= 30 
    ball_hits_p1_y_dimension = ball_y_position <= (p1_y_position+60)   and   ball_y_position >= (p1_y_position-10) 

    if ball_hits_p1_x_dimension and ball_hits_p1_y_dimension: ball_x_direction = 1





    #right-collision
    ball_hits_p2_x_dimension = ball_x_position + 10 > p2_x_position and ball_x_position + 10 < p2_x_position + 10 
    ball_hits_p2_y_dimension = ball_y_position <= (p2_y_position+60)   and   ball_y_position >= (p2_y_position-10) 

    #if ball_x_position + 10 > p2_x_position: ball_x_direction = -1
    if ball_hits_p2_x_dimension and ball_hits_p2_y_dimension: ball_x_direction = -1





    #Losing the game
    if ball_x_position < 30: done = True
    if ball_x_position > p2_x_position+10: done = True



    #without this the moving around square would leave a trailing tail.
    screen.fill((255, 255, 255)) 

    #Draw Ball
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(ball_x_position, ball_y_position, 10, 10))
    
    #Draw Paddle
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(p1_x_position, p1_y_position, 10, 60))
    
    #draw Opponent
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(p2_x_position, p2_y_position, 10, 60))


    pygame.display.flip()
    clock.tick(120)







