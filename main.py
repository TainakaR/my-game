import pygame
import sys
from menu import show_menu  # メニューを表示する関数をインポート

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game Title')

    show_menu(screen)  # メニューを表示

    pygame.quit()

if __name__ == "__main__":
    main()