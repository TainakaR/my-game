import pygame
import time
from minigame import total_score

# 初期化
pygame.init()

# ウィンドウの設定
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Result")

font_path = 'assets/fonts/g_brushtappitsu_freeR.ttf'

# 画像の読み込み
background_image = pygame.image.load("assets/images/result_background1.png")
background_image2 = pygame.image.load("assets/images/result_background2.png")
face_1 = pygame.image.load("assets/images/face_1.png")  # 49以下の場合
face_2 = pygame.image.load("assets/images/face_2.png")  # 50～89の場合
face_3 = pygame.image.load("assets/images/face_3.png")  # 90以上の場合

def show_result(screen, score_manager):
    # 最初の背景を表示
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
    
    # 1秒間待機
    time.sleep(1)

    # 新しい背景を表示
    screen.blit(background_image2, (0, 0))

    # 画面左側にスコアを表示
    font = pygame.font.Font(font_path, 300)
    score_display = score_manager.get_score()
    score_text = font.render(str(score_display), True, (0, 0, 0))
    screen.blit(score_text, (20, 200))  # 位置は調整可能
    
    # 画面右側に顔の画像を表示
    if score_display <= 59:
        screen.blit(face_1, (300, 0))  # 49以下
    elif 60 <= score_display <= 99:
        screen.blit(face_2, (300, 0))  # 50 ~ 89
    else:  # 90以上
        screen.blit(face_3, (300, 0))  # 90以上

    # 最終的な画面を更新
    pygame.display.flip()

    print(f"Total Score: {score_manager.get_score()}")

    # 終了までの待機
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESCキーが押された場合
                    waiting = False
    
    pygame.quit() 