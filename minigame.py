import pygame
import sys

# ミニゲームの設定
BOX_WIDTH = 200
BOX_HEIGHT = 400
BAR_WIDTH = 150
BAR_HEIGHT = 26
FPS = 60

def draw_box(screen, box_image, box_rect):
    screen.blit(box_image, box_rect)

def draw_bar(screen, bar_image, bar_rect):
    screen.blit(bar_image, bar_rect)

def calculate_score(bar_pos):
    # 上端、中央、下端の位置を指定
    top_position = 50  # ボックスの上からの位置
    bottom_position = 350  # ボックスの下からの位置

    if bar_pos <= top_position:
        return 30
    elif bar_pos >= bottom_position:
        return 0
    else:
        # 相対的な点数を計算
        return int(30 - ((bar_pos - top_position) / (bottom_position - top_position) * 30))

def run_minigame(screen):
    pygame.font.init()
    font = pygame.font.Font(None, 74)

    # 画像の読み込み
    box_image = pygame.image.load('box.png').convert_alpha()
    bar_image = pygame.image.load('bar.png').convert_alpha()

    boxes = [
        {'name': 'A', 'rect': pygame.Rect(100, 100, BOX_WIDTH, BOX_HEIGHT)},
        {'name': 'B', 'rect': pygame.Rect(320, 100, BOX_WIDTH, BOX_HEIGHT)},
        {'name': 'C', 'rect': pygame.Rect(540, 100, BOX_WIDTH, BOX_HEIGHT)},
    ]

    for box in boxes:
        # バーの初期位置をボックスの中央に設定
        bar_rect = pygame.Rect(
            box['rect'].centerx - (BAR_WIDTH // 2),  # 中央揃え
            box['rect'].centery - (BAR_HEIGHT // 2),  # 中央揃え
            BAR_WIDTH,
            BAR_HEIGHT
        )
        y_velocity = 5  # バーの上下速度
        bar_moving = True

        clock = pygame.time.Clock()

        while bar_moving:
            screen.fill((0, 0, 0))  # 画面を黒に

            # 各ボックスを描画
            for b in boxes:
                draw_box(screen, box_image, b['rect'])

            # バーを描画
            draw_bar(screen, bar_image, bar_rect)
            pygame.display.flip()  # 画面を更新

            # バーを上下させる
            bar_rect.y += y_velocity

            # ボックス内での制限
            if bar_rect.top <= box['rect'].top:
                bar_rect.top = box['rect'].top
                y_velocity = -y_velocity  # 反転（下に移動）
            elif bar_rect.bottom >= box['rect'].bottom:
                bar_rect.bottom = box['rect'].bottom
                y_velocity = -y_velocity  # 反転（上に移動）

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # スペースキーでバーを止める
                        score = calculate_score(bar_rect.y)
                        print(f"Box {box['name']} Score: {score}")  # スコア表示
                        bar_moving = False  # バーを止める
            
            clock.tick(FPS)

        # 各ボックスのバーが停止した位置を表示
        screen.fill((0, 0, 0))  # 画面を黒に
        for b in boxes:
            draw_box(screen, box_image, b['rect'])
        draw_bar(screen, bar_image, bar_rect)  # 停止したバーを描画
        pygame.display.flip()

        # 次のボックスのために待機
        pygame.time.wait(2000)  # 2秒間待つ
        
    print("ミニゲームが終了しました。再帰的にメニュー画面に戻ります。")