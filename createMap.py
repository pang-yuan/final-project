vocrect = voc.get_rect()

def createMap(i, score):
	screen.fill((255, 255, 255))     # 填充顏色
    screen.blit(background, (0, 0))  # 填入到背景
    speed = [0,5]
    vocrect = vocrect.move(speed)
    screen.blit(voc.vocStatus[voc.status], vocrect)  # voc指單字本身，voc_pic指承載單字的底圖方塊

    # 顯示分數
    screen.blit(font.render('Score:' + str(score), -1, (255, 255, 255)), (100, 50))  # 設定顏色及座標位置
    pygame.display.update()    # 更新顯示