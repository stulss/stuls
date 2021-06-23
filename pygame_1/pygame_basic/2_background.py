import pygame

pygame.init() # 반드시 필요

# 화면 크기  설정
screen_width = 1020 # 가로크기
screen_height = 840 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("gun geli") # 게임이름

# 배경이미지 불러오기
background = pygame.image.load("D:/frorm/편집툴/코딩/python/활용편_game/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
    
    screen.blit(background, (0, 0)) # 배경 그리기
    pygame.display.update() # 게임화면을 다시 그리기!
# pygame 종료
pygame.quit()