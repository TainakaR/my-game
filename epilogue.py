import pygame

def show_epilogue(screen):
    # エピローグ画面の設定や画像の読み込み
    font = pygame.font.Font(None, 36)
    text_surface = font.render("ゲームルール説明", True, (255, 255, 255))
    back_button_rect = text_surface.get_rect(center=(400, 300))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"  # 終了時
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return "menu"  # メニューに戻る

        screen.fill((0, 0, 0))  # 背景を黒に
        screen.blit(text_surface, back_button_rect.topleft)
        
        pygame.display.flip()