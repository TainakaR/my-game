import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
BOX_WIDTH = 150
BOX_HEIGHT = 400
BOX_SPACING = 50
BAR_HEIGHT = 10
BAR_SPEED = 5

# Game variables
current_box = 0  # 現在操作するボックスのインデックス
scores = [0, 0, 0]  # ボックスごとのスコア

def calculate_score(bar_y, box_y, box_height):
    """Calculate the score based on the bar's position."""
    top = box_y
    bottom = box_y + box_height
    return max(0, int(((bottom - bar_y) / box_height) * 100))

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vertical Box Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Box positions
boxes = [
    ((i * (BOX_WIDTH + BOX_SPACING)) + BOX_SPACING, (SCREEN_HEIGHT - BOX_HEIGHT) // 2)
    for i in range(3)
]

# Bar positions and movement states
bars = [
    {"y": box[1] + BOX_HEIGHT - BAR_HEIGHT, "moving_up": True, "stopped": False}
    for box in boxes
]

# Load bar image
bar_image = pygame.image.load("assets/images/bar.png")  # 画像をロード

# Main game loop
while True:
    screen.fill(WHITE)  # 背景を白で塗りつぶす

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bars[current_box]["stopped"]:
                bars[current_box]["stopped"] = True
                scores[current_box] = calculate_score(
                    bars[current_box]["y"], boxes[current_box][1], BOX_HEIGHT
                )
                if current_box < len(boxes) - 1:
                    current_box += 1
                else:
                    print("Final Scores:", scores)
                    pygame.time.wait(2000)
                    pygame.quit()
                    sys.exit()

    # Draw boxes and bars
    for i, (box_x, box_y) in enumerate(boxes):
        # Draw box
        pygame.draw.rect(screen, BLACK, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT), 2)

        # Move and draw the bar
        if i == current_box and not bars[i]["stopped"]:
            if bars[i]["moving_up"]:
                bars[i]["y"] -= BAR_SPEED
                if bars[i]["y"] <= box_y:
                    bars[i]["moving_up"] = False
            else:
                bars[i]["y"] += BAR_SPEED
                if bars[i]["y"] >= box_y + BOX_HEIGHT - BAR_HEIGHT:
                    bars[i]["moving_up"] = True

        # Draw bar image
        bar_position = (box_x, bars[i]["y"])
        screen.blit(bar_image, bar_position)

    # Display scores
    for i, score in enumerate(scores):
        score_text = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (boxes[i][0], boxes[i][1] - 40))

    pygame.display.flip()
    clock.tick(60)

