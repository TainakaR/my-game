import pygame

def start_minigame(screen):
    # ミニゲームの設定
    font = pygame.font.Font(None, 36)
    text_surface = font.render("ミニゲーム実行中...", True, (255, 255, 255))
    
    # ゲームのメインループ
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"  # 終了時
        
        # ゲームの処理を書く
        screen.fill((0, 0, 0))  # 背景を黒に
        screen.blit(text_surface, (400 - text_surface.get_width() // 2, 300))

        pygame.display.flip()
        
        # 一定の条件で結果表示へ遷移（仮の条件）
        # 念のため素早く結果に移行する
        return "result"