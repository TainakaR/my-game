import pygame
import sys
from menu import show_menu
from epilogue import show_epilogue
from minigame import start_minigame
from result import show_result

# Pygameの初期化
pygame.init()

# ウィンドウの設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ミニゲーム")

def main():
    current_state = "menu"  # 初期状態はメニュー

    while True:
        if current_state == "menu":
            current_state = show_menu(screen)
        elif current_state == "epilogue":
            current_state = show_epilogue(screen)
        elif current_state == "minigame":
            current_state = start_minigame(screen)
        elif current_state == "result":
            current_state = show_result(screen)
        else:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()