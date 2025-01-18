import pygame

def show_result(screen):
    # 結果画面の設定
    font = pygame.font.Font(None, 36)
    result_text_surface = font.render("ゲームの結果を表示します", True, (255, 255, 255))
    back_button_surface = font.render("メニューに戻る", True, (255, 255, 255))

    # ボタンの位置を設定
    back_button_rect = back_button_surface.get_rect(center=(400, 500))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"  # 終了時
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return "menu"  # メニューに戻る

        screen.fill((0, 0, 0))  # 背景を黒に
        screen.blit(result_text_surface, (400 - result_text_surface.get_width() // 2, 200))
        screen.blit(back_button_surface, back_button_rect.topleft)
        
        pygame.display.flip()