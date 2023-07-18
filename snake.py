import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define the Snake class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT / 2
        self.direction = "right"
        self.speed = 10

    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

# Define the Food class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - 10, 10)
        self.rect.y = random.randrange(0, SCREEN_HEIGHT - 10, 10)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the game window
pygame.display.set_caption("Snake Game")

# Create the Snake and Food sprites
snake = Snake()
food = Food()

# Create a Group for all the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(food)

# Set the clock for the game
clock = pygame.time.Clock()

# Set the font for the score
font = pygame.font.Font(None, 36)

# Set the initial score to 0
score = 0

# Set the initial game over state to False
game_over = False

# Start the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"

    # Update the Snake and Food sprites
    all_sprites.update()

    # Check for collisions with the Food sprite
    if pygame.sprite.collide_rect(snake, food):
        food.kill()
        food = Food()
        all_sprites.add(food)
        score += 10

    # Check for collisions with the walls
    if snake.rect.x < 0 or snake.rect.x > SCREEN_WIDTH - 10 or snake.rect.y < 0 or snake.rect.y > SCREEN_HEIGHT - 10:
        game_over = True

    # Check for collisions with the Snake's body
    if len(pygame.sprite.spritecollide(snake, all_sprites, False)) > 1:
        game_over = True

    # Clear the screen
    screen.fill(BLACK)

    # Draw all the sprites
    all_sprites.draw(screen)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(20)

# Quit Pygame
pygame.quit()