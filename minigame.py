import pygame

# 定数の定義
WIDTH = 600
HEIGHT = 800
BOX_WIDTH = 150
BOX_HEIGHT = 400
BAR_HEIGHT = 20
BAR_SPEED = 2
FPS = 30

def run_minigame(screen):
    # Pygameの初期化
    pygame.init()
    clock = pygame.time.Clock()

    # 画面の設定
    screen_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Minigame')

    # 画像の読み込み
    box_images = [
        pygame.image.load('assets/images/box_1.png'),
        pygame.image.load('assets/images/box_2.png'),
        pygame.image.load('assets/images/box_3.png')
    ]
    bar_images = [
        pygame.image.load('assets/images/bar_1.png'),
        pygame.image.load('assets/images/bar_2.png'),
        pygame.image.load('assets/images/bar_3.png')
    ]

    # ボックスの位置を設定
    boxes_positions = [
        (75, 100),   # ボックス1の位置
        (225, 100),  # ボックス2の位置
        (375, 100)   # ボックス3の位置
    ]

    # バーの初期位置と状態の設定
    bars_positions = [0, 0, 0]              # 各バーのY位置
    bar_moving = [True, False, False]       # 各バーの動きの状態
    bar_directions = [1, 1, 1]              # 各バーの移動方向

    # 点数の初期化
    scores = [0, 0, 0]  # 各バーの得点
    current_bar = 0  # 現在動かしているバーのインデックス

    # ゲームループ
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and bar_moving[current_bar]:
                    bar_moving[current_bar] = False  # 現在のバーを停止させる
                    
                    # 得点計算
                    position = bars_positions[current_bar]
                    if position == 0:
                        scores[current_bar] = 0
                    elif position >= (BOX_HEIGHT - BAR_HEIGHT):
                        scores[current_bar] = 30
                    else:
                        scores[current_bar] = max(30 - (30 * position // (BOX_HEIGHT - BAR_HEIGHT)), 0)
                    
                    current_bar += 1  # 次のバーに移動
                    if current_bar < 3:
                        bar_moving[current_bar] = True  # 次のバーを動かし始める

        # バーの動き
        for i in range(len(bar_moving)):
            if bar_moving[i]:
                bars_positions[i] += BAR_SPEED * bar_directions[i]
                # 上下の制限
                if bars_positions[i] >= (BOX_HEIGHT - BAR_HEIGHT):
                    bars_positions[i] = (BOX_HEIGHT - BAR_HEIGHT)
                    bar_directions[i] = -1  # 上に移動
                elif bars_positions[i] <= 0:
                    bars_positions[i] = 0
                    bar_directions[i] = 1   # 下に移動

        # スクリーンの描画
        screen.fill((255, 255, 255))  # 背景を白に設定
        for i in range(3):
            screen.blit(box_images[i], boxes_positions[i])
            bar_y = boxes_positions[i][1] + bars_positions[i]  # ボックスの下にバーを表示
            screen.blit(bar_images[i], (boxes_positions[i][0], bar_y))

        pygame.display.flip()
        clock.tick(FPS)

    # 得点の合計計算
    total_score = sum(scores)
    print(f'Score A: {scores[0]}, Score B: {scores[1]}, Score C: {scores[2]}, Total Score D: {total_score}')

    pygame.quit()