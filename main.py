import pygame
import sys

# 初期化
pygame.init()

# 画面サイズとタイトル設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My Pygame Project"

# 色の定義 (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# ゲーム画面の設定
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# フレームレート設定
clock = pygame.time.Clock()
FPS = 60

# メインゲームループ
def main():
    # ゲームの初期化
    running = True

    # プレイヤーの四角いオブジェクト (デモ用)
    player_rect = pygame.Rect(50, 50, 50, 50)
    player_speed = 5

    while running:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ウィンドウを閉じる
                running = False

        # キー入力処理
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed

        # 画面の更新
        screen.fill(WHITE)  # 背景色を白にする
        pygame.draw.rect(screen, BLUE, player_rect)  # プレイヤーを描画

        pygame.display.flip()  # 描画内容を反映
        clock.tick(FPS)  # フレームレートを維持

    pygame.quit()
    sys.exit()

# エントリーポイント
if __name__ == "__main__":
    main()