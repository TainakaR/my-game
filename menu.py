import pygame
import sys
from epilogue import show_epilogue  # エピローグを表示する関数をインポート
from minigame import run_minigame  # ミニゲームを実行する関数をインポート
from result import show_result  # 結果画面を表示する関数をインポート

class ScoreManager:
    def __init__(self):
        self.total_score = 10

    def add_score(self, score):
        self.total_score += score

    def get_score(self):
        return self.total_score

def show_menu(screen):
    score_manager = ScoreManager()
    # 画像を読み込む
    try:
        background = pygame.image.load('assets/images/menu_background.png')
        background = pygame.transform.scale(background, (800, 600))  # ウィンドウサイズに合わせる
    except pygame.error as e:
        print(f"Could not load background.png: {e}")
        return  # 背景画像が読み込めない場合、メニュー表示を終了

    try:
        logo = pygame.image.load('assets/images/menu_logo.png')
        logo_rect = logo.get_rect(center=(400, 200))  # 位置を中心に設定
    except pygame.error as e:
        print(f"Could not load logo.png: {e}")
        return  # ロゴ画像が読み込めない場合、メニュー表示を終了

    start_button = pygame.image.load('assets/images/menu_start_button.png')

    while True:
        screen.blit(background, (0, 0))  # 背景を描画
        screen.blit(logo, logo_rect)  # ロゴを描画
        screen.blit(start_button, (300, 350))  # Startボタンを描画
        pygame.display.flip()  # 画面を更新

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
                    run_minigame(screen, score_manager)
                    # 結果画面の表示
                    show_result(screen, score_manager)