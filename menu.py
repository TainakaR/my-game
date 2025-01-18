import pygame
import sys
from epilogue import show_epilogue  # エピローグを表示する関数をインポート
from minigame import run_minigame  # ミニゲームを実行する関数をインポート

def show_menu(screen):
    start_button = pygame.image.load('assets/images/menu_start_button.png')
    rules_button = pygame.image.load('assets/images/menu_rules_button.png')

    while True:
        screen.fill((0, 0, 0))  # 背景を黒に
        screen.blit(start_button, (300, 200))  # Startボタンを描画
        screen.blit(rules_button, (300, 300))  # Rulesボタンを描画
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Startボタンがクリックされた場合
                if 300 <= mouse_pos[0] <= 500 and 200 <= mouse_pos[1] <= 250:
                    # エピローグを表示
                    show_epilogue(screen)  
                    # ミニゲームを開始
                    run_minigame(screen)

                # Rulesボタンがクリックされた場合（処理はまだ未実装）
                elif 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:
                    print("Rules button clicked - implementation required.")