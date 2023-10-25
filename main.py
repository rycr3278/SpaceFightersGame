import pygame
import os

# initialize pygame modules
pygame.font.init()
pygame.mixer.init()

# constants
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game!")

# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game elements
BORDER = pygame.Rect((WIDTH//2) - 3, 0, 6, HEIGHT)
BACKPLATE_L = pygame.Rect(5, 10, 250, 45)
BACKPLATE_R = pygame.Rect(645, 10, 250, 45)
BACKPLATE_WINNER = pygame.Rect(50, 200, 770, 100)

# sounds
BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/mixkit-electronic-retro-block-hit-2185.wav')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/mixkit-explainer-video-game-alert-sweep-236.wav')
WINNER_MUSIC = pygame.mixer.Sound('Assets/mixkit-arcade-mechanical-bling-210.wav')
MUSIC = pygame.mixer.Sound('Assets/digital-love-127441.mp3')

#fonts
HEALTH_FONT = pygame.font.SysFont('couriernew', 40)
WINNER_FONT = pygame.font.SysFont('couriernew', 100)

# game settings
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# custom events
player1_HIT = pygame.USEREVENT + 1
player2_HIT = pygame.USEREVENT + 2

# spaceship images
player1_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'ship1.png'))
player1_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        player1_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

player2_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'ship2.png'))
player2_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        player2_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# background image
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background2.png')), (WIDTH, HEIGHT))

# draw game window
def draw_window(player2, player1, player2_bullets, player1_bullets, player2_health, player1_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.draw.rect(WIN, BLACK, BACKPLATE_L)
    pygame.draw.rect(WIN, BLACK, BACKPLATE_R)
    player2_health_text = HEALTH_FONT.render("Health: " + str(player2_health), 1, WHITE)
    player1_health_text = HEALTH_FONT.render("Health: " + str(player1_health), 1, WHITE)
    WIN.blit(player2_health_text, (WIDTH - player2_health_text.get_width() - 10, 10))
    WIN.blit(player1_health_text, (10, 10))
    
    
    WIN.blit(player1_SPACESHIP, (player1.x, player1.y))
    WIN.blit(player2_SPACESHIP, (player2.x, player2.y))
    
    for bullet in player2_bullets:
        pygame.draw.rect(WIN, RED, bullet)
        
    for bullet in player1_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()

# player1 movement
def player1_handle_movement(keys_pressed, player1):
    if keys_pressed[pygame.K_a] and player1.x - VEL > 0: # left
        player1.x -= VEL
    if keys_pressed[pygame.K_d] and player1.x + VEL + player1.width < BORDER.x: # right
        player1.x += VEL
    if keys_pressed[pygame.K_w] and player1.y - VEL > 0: # up
        player1.y -= VEL
    if keys_pressed[pygame.K_s] and player1.y + VEL  + player1.height < HEIGHT - 20: # down
        player1.y += VEL

# player2 movement            
def player2_handle_movement(keys_pressed, player2):
    if keys_pressed[pygame.K_LEFT] and player2.x - VEL > BORDER.x + 20: # left
        player2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player2.x + VEL + player2.width < WIDTH + 10: # right
        player2.x += VEL
    if keys_pressed[pygame.K_UP] and player2.y - VEL > 0: # up
        player2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player2.y + VEL  + player2.height < HEIGHT - 20: # down
        player2.y += VEL

# bullet movement and collisions
def handle_bullets(player1_bullets, player2_bullets, player1, player2):
    for bullet in player1_bullets:
        bullet.x += BULLET_VEL
        if player2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(player2_HIT))
            player1_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            player1_bullets.remove(bullet)
            
    for bullet in player2_bullets:
        bullet.x -= BULLET_VEL
        if player1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(player1_HIT))
            player2_bullets.remove(bullet)
        elif bullet.x < 0:
            player2_bullets.remove(bullet)
       
# display winner       
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    pygame.draw.rect(WIN, BLACK, BACKPLATE_WINNER)    
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# main game loop    
def main():
    #MUSIC.play()
    player2 = pygame.Rect(800, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player1 = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    player2_bullets = []
    player1_bullets = []
    
    player2_health = 10
    player1_health = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(player1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player1.x + player1.width, player1.y + player1.height//2 + 5, 10, 5)
                    player1_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                
                if event.key == pygame.K_RCTRL and len(player2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player2.x, player2.y + player2.height//2 + 5, 10, 5)
                    player2_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            
            if event.type == player2_HIT:
                player2_health -= 1
                BULLET_HIT_SOUND.play()
            
            if event.type == player1_HIT:
                player1_health -= 1
                BULLET_HIT_SOUND.play()
        
        winner_text = ""
        if player2_health <= 0:
            winner_text = "player1 Wins!"
        
        if player1_health <= 0:
            winner_text = "player2 Wins!"
        
        if winner_text != "":
            draw_winner(winner_text)
            WINNER_MUSIC.play()
            break
        
        keys_pressed = pygame.key.get_pressed()
        player1_handle_movement(keys_pressed, player1)
        player2_handle_movement(keys_pressed, player2)

        handle_bullets(player1_bullets, player2_bullets, player1, player2)
        
        
        draw_window(player2, player1, player2_bullets, player1_bullets, player2_health, player1_health)        

main()    
    
# entry point    
if __name__ == "__main__":
    main()