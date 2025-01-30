import pygame

def show_epilogue(screen):
    # 画像ファイル名のリスト
    images = ['assets/images/epilogue_image1.png', 'assets/images/epilogue_image2.png', 'assets/images/epilogue_image3.png']
    image_count = len(images)
    
    # スライドショーを実行する回数
    for i in range(image_count):
        # メインループ
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # 終了時
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # ESCキーで戻る
                    return
                
            # 画像を読み込む
            try:
                background = pygame.image.load(images[i])
                background = pygame.transform.scale(background, (800, 600))  # ウィンドウサイズにスケーリング
            except pygame.error as e:
                print(f"Could not load image: {images[i]}. {e}")
                return  # エラーが発生した場合は終了
            
            screen.blit(background, (0, 0))  # 背景を描画
            pygame.display.flip()  # 画面を更新
            
            # 0.5秒待つ
            pygame.time.delay(500)  # 500ミリ秒 (1.5秒) の遅延
            
            # 画像が表示されたらループを抜ける
            break