import pygame

def show_menu(screen):
    # メニュー画面の設定や画像の読み込み
    background_image = pygame.image.load("menu_background.png")
    logo_image = pygame.image.load("menu_logo.png")
    start_button_image = pygame.image.load("menu_start_button.png")
    rules_button_image = pygame.image.load("menu_rules_button.png")

    # ボタンの位置
    start_button_rect = start_button_image.get_rect(center=(400, 250))
    rules_button_rect = rules_button_image.get_rect(center=(400, 350))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"  # 終了時
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return "minigame"  # ゲームスタート
                elif rules_button_rect.collidepoint(event.pos):
                    return "epilogue"  # ルール説明

        screen.blit(background_image, (0, 0))
        screen.blit(logo_image, (400 - logo_image.get_width() // 2, 50))
        screen.blit(start_button_image, start_button_rect.topleft)
        screen.blit(rules_button_image, rules_button_rect.topleft)
        
        pygame.display.flip()