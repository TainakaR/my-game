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
    top_position = 50     # ボックスの上からの位置
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
        {'name': 'A', 'rect': pygame.Rect(100, 100, BOX_WIDTH, BOX_HEIGHT), 
         'bar_y': 200, 'bar_moving': True, 'score': 0},
        {'name': 'B', 'rect': pygame.Rect(320, 100, BOX_WIDTH, BOX_HEIGHT), 
         'bar_y': 200, 'bar_moving': False, 'score': 0},
        {'name': 'C', 'rect': pygame.Rect(540, 100, BOX_WIDTH, BOX_HEIGHT), 
         'bar_y': 200, 'bar_moving': False, 'score': 0},
    ]

    for box_index in range(len(boxes)):
        current_box = boxes[box_index]
        y_velocity = 5  # バーの上下速度
        clock = pygame.time.Clock()

        while True:
            screen.fill((0, 0, 0))  # 画面を黒に

            # 各ボックスを描画
            for i, box in enumerate(boxes):
                draw_box(screen, box_image, box['rect'])
                
                # バーの位置を更新
                bar_rect = pygame.Rect(
                    box['rect'].centerx - (BAR_WIDTH // 2),
                    box['bar_y'] - (BAR_HEIGHT // 2),
                    BAR_WIDTH,
                    BAR_HEIGHT
                )
                
                # 動いているバーだけ更新
                if box['bar_moving']:
                    bar_rect.y += y_velocity

                    # ボックス内での制限
                    if bar_rect.top <= box['rect'].top:
                        bar_rect.top = box['rect'].top
                        y_velocity = -y_velocity  # 反転（下に移動）
                    elif bar_rect.bottom >= box['rect'].bottom:
                        bar_rect.bottom = box['rect'].bottom
                        y_velocity = -y_velocity  # 反転（上に移動）

                # バーを描画
                draw_bar(screen, bar_image, bar_rect)

                # スペースキーでバーを止める
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and box['bar_moving']:  # スペースキーでバーを止める
                            box['bar_y'] = bar_rect.y  # バーの位置を保持
                            box['score'] = calculate_score(bar_rect.y)
                            print(f"Box {box['name']} Score: {box['score']}")  # スコア表示
                            box['bar_moving'] = False  # バーを止める

            pygame.display.flip()  # 画面を更新
            clock.tick(FPS)

            # 他のボックスのバーを中央に配置
            for i, box in enumerate(boxes):
                if i != box_index and not box['bar_moving']:
                    box['bar_y'] = 200  # 中央に戻す

            if not current_box['bar_moving']:
                break  # 現在