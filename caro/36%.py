import pygame

pygame.init()

screen_width = 600
screen_height = 600
line_width = 1

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cờ Caro')

movement_sound0 = pygame.mixer.Sound('sound\\tic.wav')
movement_sound1 = pygame.mixer.Sound('sound\\ticc.wav')
hover_sound = pygame.mixer.Sound('sound\\hover_sound.wav')
hover_sound.set_volume(0.1)

x_marker = pygame.image.load('assets\\x.png')
o_marker = pygame.image.load('assets\\o.png')
l_marker = pygame.image.load('assets\\1.png')
xx_marker = pygame.image.load('assets\\xx.png')
menu_background = pygame.image.load('assets\\menu_background.jpg')
menu_img = pygame.image.load('assets\\menu.png')
menuu_img = pygame.image.load('assets\\menuu.png')
mode_img = pygame.image.load('assets\\mode.png')
mode1_img = pygame.image.load('assets\\mode1.png')
mode11_img = pygame.image.load('assets\\mode11.png')
mode2_img = pygame.image.load('assets\\mode2.png')
mode22_img = pygame.image.load('assets\\mode22.png')
mode3_img = pygame.image.load('assets\\mode3.png')
mode33_img = pygame.image.load('assets\\mode33.png')
player1_won_img = pygame.image.load('assets\\player1_won.png')
player2_won_img = pygame.image.load('assets\\player2_won.png')
player3_won_img = pygame.image.load('assets\\player3_won.png')
draw_img = pygame.image.load('assets\\draw.png')
play_gain_img = pygame.image.load('assets\\play_again.png')
play_gain_hover_img = pygame.image.load('assets\\play_again_hover.png')


markers = [[-1 for _ in range(20)] for _ in range(20)]  #Lưu các ô đã được đánh dấu X và O
clicked = False  #Kiểm tra xem đã click hay chưa
player = 0   
winner = None       
game_over = False
cnt = 0   #Đếm xem bao nhiêu ô đã được đánh dấu
mode = None
x = None
y = None
isPlaysound = False

#Đĩnh nghĩa màu và font chữ
blue = (53, 126, 242, 120)
green = (32, 230, 38, 120)
red = (255, 0, 0, 120)
gray = (186, 184, 179, 120)
white = (255, 255, 255, 120)
black = (0, 0, 0, 120)
yellow = (209, 201, 42, 180)
pink = (235, 19, 199, 120)
gray = (180, 185, 194, 120)
font = pygame.font.SysFont("VCR OSD Mono", 35)
font1 = pygame.font.SysFont("VCR OSD Mono", 45)
font2 = pygame.font.SysFont("VCR OSD Mono", 25)

#Hình vuông đánh lại
again_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 10, 300, 50)
menu_rect = pygame.Rect(250, 0, 80, 27)
mode_rect = pygame.Rect(100, 50, 400, 50)
mode1_rect = pygame.Rect(80, 200, 440, 50)
mode2_rect = pygame.Rect(80, 300, 440, 50)
mode3_rect = pygame.Rect(80, 400, 440, 50)

gray_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.rect(gray_surface, gray, (0, 0, 30, 30))
red_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.rect(red_surface, red, (0, 0, 30, 30))
green_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.rect(green_surface, green, (0, 0, 30, 30))
blue_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.rect(blue_surface, blue, (0, 0, 30, 30))


def draw_menu():
    global isPlaysound
    screen.blit(menu_background, (0, 0))
    screen.blit(mode_img, (70, 64))
    pos = pygame.mouse.get_pos()
    if 80 <= pos[0] <= 520 and 200 <= pos[1] <= 250:
        screen.blit(mode11_img, (80, 205))
        if not isPlaysound:
            hover_sound.play()
            isPlaysound = True 
    else:
        screen.blit(mode1_img, (80, 200))

    if not mode1_rect.collidepoint(pos) and not mode2_rect.collidepoint(pos) and not mode3_rect.collidepoint(pos):
        isPlaysound = False
    
    if 80 <= pos[0] <= 520 and 300 <= pos[1] <= 350:
        screen.blit(mode22_img, (80, 305))
        if not isPlaysound:
            hover_sound.play()
            isPlaysound = True 
    else:
        screen.blit(mode2_img, (80, 300))

    if not mode1_rect.collidepoint(pos) and not mode2_rect.collidepoint(pos) and not mode3_rect.collidepoint(pos):
        isPlaysound = False
    
    if 80 <= pos[0] <= 520 and 400 <= pos[1] <= 450:
        screen.blit(mode33_img, (80, 405))
        if not isPlaysound:
            hover_sound.play()
            isPlaysound = True 
    else:
        screen.blit(mode3_img, (80, 400))

    if not mode1_rect.collidepoint(pos) and not mode2_rect.collidepoint(pos) and not mode3_rect.collidepoint(pos):
        isPlaysound = False
#Vẽ lưới
def draw_grid():
    global isPlaysound
    screen.blit(menu_background, (0, 0))
    pygame.draw.rect(screen, white, (30, 30, 540, 540))
    x = 1
    pygame.draw.line(screen, gray, (30, x * 30), (screen_width - 30, x * 30), line_width + 2)
    pygame.draw.line(screen, gray, (x * 30, 30), (x * 30, screen_height - 30), line_width + 2)
    x = 19
    pygame.draw.line(screen, gray, (30, x * 30), (screen_width - 30, x * 30), line_width + 2)
    pygame.draw.line(screen, gray, (x * 30, 30), (x * 30, screen_height - 30), line_width + 2)
    for x in range(2, 19):
        pygame.draw.line(screen, gray, (30, x * 30), (screen_width - 30, x * 30), line_width)
        pygame.draw.line(screen, gray, (x * 30, 30), (x * 30, screen_height - 30), line_width)

    pos = pygame.mouse.get_pos()
    if 250 <= pos[0] <= 330 and 0 <= pos[1] <= 27:
        screen.blit(menuu_img, (250, -5))
        if not isPlaysound:
            hover_sound.play()
            isPlaysound = True 
    else:
        screen.blit(menu_img, (250, -5))
    if not again_rect.collidepoint(pos) and not menu_rect.collidepoint(pos):
        isPlaysound = False

#Vẽ X và O    
def draw_markers():
    for x in range(1, 19):
        for y in range(1, 19):
            if markers[x][y] == 0:
                screen.blit(x_marker, (x * 30 + 3, y * 30 + 3))
            if markers[x][y] == 1:
                screen.blit(o_marker, (x * 30 + 3, y * 30 + 3))
            if markers[x][y] == 2:
                screen.blit(l_marker, (x * 30 + 3, y * 30 + 3))
#Vẽ O cho chế độ cờ mù
def draw_markers3():            
    for x in range(1, 19):
        for y in range(1, 19):
            if markers[x][y] != -1:
                screen.blit(xx_marker, (x * 30 + 3, y * 30 + 3))
#Vẽ người thắng
def draw_winner():
    global isPlaysound
    if winner == 1:
        screen.blit(player1_won_img,(screen_width // 2 - 150, screen_height // 2 - 50))
    elif winner == 2:
        screen.blit(player2_won_img,(screen_width // 2 - 150, screen_height // 2 - 50))
    elif winner == 3:
        screen.blit(player3_won_img,(screen_width // 2 - 150, screen_height // 2 - 50))
    else:
        screen.blit(draw_img,(screen_width // 2 - 150, screen_height // 2 - 50)) 
    pos = pygame.mouse.get_pos()
    if 150 <= pos[0] <= 450 and 310 <= pos[1] <= 360:
        screen.blit(play_gain_hover_img, (150, 310)) 
        if not isPlaysound:
            hover_sound.play()
            isPlaysound = True
    else:
        screen.blit(play_gain_img, (150, 310))

    if not again_rect.collidepoint(pos) and not menu_rect.collidepoint(pos):
        isPlaysound = False
#Kiểm tra người thắng
def check_winner(x, y, cnt):
    # Check hàng ngang
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if x + r <= 19 and x + l >= 1 and markers[x + l][y] == markers[x + l + 1][y] == markers[x + l + 2][y] == markers[x + l + 3][y] == markers[x + l + 4][y] == 0:
            for i in range(l, r):
                screen.blit(red_surface,((x + i) * 30, y * 30))
            return 1
        if x + r <= 19 and x + l >= 1 and markers[x + l][y] == markers[x + l + 1][y] == markers[x + l + 2][y] == markers[x + l + 3][y] == markers[x + l + 4][y] == 1:
            for i in range(l, r):
                screen.blit(green_surface,((x + i) * 30, y * 30))
            return 2
        if x + r <= 19 and x + l >= 1 and markers[x + l][y] == markers[x + l + 1][y] == markers[x + l + 2][y] == markers[x + l + 3][y] == markers[x + l + 4][y] == 2:
            for i in range(l, r):
                screen.blit(blue_surface,((x + i) * 30, y * 30))
            return 3
        l -= 1
        r -= 1
    #Check hàng dọc
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if y + r <= 19 and y + l >= 1 and markers[x][y + l] == markers[x][y + l + 1] == markers[x][y + l + 2] == markers[x][y + l + 3] == markers[x][y + l + 4] == 0:
            for i in range(l, r):
                screen.blit(red_surface,(x * 30, (y + i) * 30))
            return 1
        if y + r <= 19 and y + l >= 1 and markers[x][y + l] == markers[x][y + l + 1] == markers[x][y + l + 2] == markers[x][y + l + 3] == markers[x][y + l + 4] == 1:
            for i in range(l, r):
                screen.blit(green_surface,(x * 30, (y + i) * 30))
            return 2
        if y + r <= 19 and y + l >= 1 and markers[x][y + l] == markers[x][y + l + 1] == markers[x][y + l + 2] == markers[x][y + l + 3] == markers[x][y + l + 4] == 2:
            for i in range(l, r):
                screen.blit(blue_surface,(x * 30, (y + i) * 30))
            return 3
        l -= 1
        r -= 1
    #Check hàng chéo góc phần tư thứ II và IV
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if x + r <= 19 and y + r <= 19 and x + l >= 1 and y + l >= 1 and markers[x + l][y + l] == markers[x + l + 1][y + l + 1] == markers[x + l + 2][y + l + 2] == markers[x + l + 3][y + l + 3] == markers[x + l + 4][y + l + 4] == 0:
            for i in range(l, r):
                screen.blit(red_surface, ((x + i) * 30, (y + i) * 30))
            return 1
        if x + r <= 19 and y + r <= 19 and x + l >= 1 and y + l >= 1 and markers[x + l][y + l] == markers[x + l + 1][y + l + 1] == markers[x + l + 2][y + l + 2] == markers[x + l + 3][y + l + 3] == markers[x + l + 4][y + l + 4] == 1:
            for i in range(l, r):
                screen.blit(green_surface, ((x + i) * 30, (y + i) * 30))
            return 2
        if x + r <= 19 and y + r <= 19 and x + l >= 1 and y + l >= 1 and markers[x + l][y + l] == markers[x + l + 1][y + l + 1] == markers[x + l + 2][y + l + 2] == markers[x + l + 3][y + l + 3] == markers[x + l + 4][y + l + 4] == 2:
            for i in range(l, r):
                screen.blit(blue_surface, ((x + i) * 30, (y + i) * 30))
            return 3
        l -= 1
        r -= 1
    #Check chéo góc phần tư thứ I và III
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if x + r <= 19 and y - r >= 0 and x + l >= 1 and y - l <= 18 and markers[x + l][y - l] == markers[x + l + 1][y - l - 1] == markers[x + l + 2][y - l - 2] == markers[x + l + 3][y - l - 3] == markers[x + l + 4][y - l - 4] == 0:
            for i in range(l, r):
                screen.blit(red_surface, ((x + i) * 30, (y - i) * 30))
            return 1
        if x + r <= 19 and y - r >= 0 and x + l >= 1 and y - l <= 18 and markers[x + l][y - l] == markers[x + l + 1][y - l - 1] == markers[x + l + 2][y - l - 2] == markers[x + l + 3][y - l - 3] == markers[x + l + 4][y - l - 4] == 1:
            for i in range(l, r):
                screen.blit(green_surface, ((x + i) * 30, (y - i) * 30))
            return 2
        if x + r <= 19 and y - r >= 0 and x + l >= 1 and y - l <= 18 and markers[x + l][y - l] == markers[x + l + 1][y - l - 1] == markers[x + l + 2][y - l - 2] == markers[x + l + 3][y - l - 3] == markers[x + l + 4][y - l - 4] == 2:
            for i in range(l, r):
                screen.blit(blue_surface, ((x + i) * 30, (y - i) * 30))
            return 3
        l -= 1
        r -= 1
    # Nếu đánh hết bàn cờ mà chưa có người thắng thì là hòa
    if cnt == 18 * 18:
        return 0
    # Nếu chưa đánh hết thì chưa có người thắng
    return None

# Khởi tạo lại trò chơi
def restart():
    global markers, player, winner, game_over, cnt, x, y
    markers = [[-1 for _ in range(20)] for _ in range(20)] 
    player = 0          
    winner = None       
    game_over = False
    cnt = 0
    x = None
    y = None

run = True

while run:
    if mode == None:
        #Vẽ menu
        draw_menu()
    elif mode == 1 or mode == 2:
        draw_grid()
        if x != None and y != None:
            screen.blit(gray_surface, (x * 30, y * 30))
            draw_markers()

    elif mode == 3:
        draw_grid()
        if x != None and y != None:
            screen.blit(gray_surface, (x * 30, y * 30))
            draw_markers3()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if mode == None:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                clicked = True
                
            if event.type == pygame.MOUSEBUTTONUP  and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if mode1_rect.collidepoint(pos):
                    mode = 1
                if mode2_rect.collidepoint(pos):
                    mode = 2
                if mode3_rect.collidepoint(pos):
                    mode = 3
        else:
            if mode == 1:
                if winner == None:
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #Nếu click chuột trái thì mới được tính là đã click
                        clicked = True
                    if event.type == pygame.MOUSEBUTTONUP  and clicked == True:
                        clicked = False
                        pos = pygame.mouse.get_pos()
                        if menu_rect.collidepoint(pos): #Nếu click vào ô menu thì sẽ quay trở lại menu
                            restart()
                            mode = None
                            continue
                        cell_x = pos[0] // 30
                        cell_y = pos[1] // 30
                        if markers[cell_x][cell_y] != -1 or cell_x == 19 or cell_x == 0 or cell_y == 19 or cell_y == 0:    #Nếu 1 ô đã được đánh dấu rồi thì không được thao tác trên ô đó nữa
                            continue
                        if player == 0:             #Player 1 thì dùng sound0
                            movement_sound0.play()
                        else:                       #Player 2 thì dùng sound1
                            movement_sound1.play()
                        x, y = cell_x, cell_y                           
                        cnt += 1
                        markers[cell_x][cell_y] = player    #Gán giá trị của ô cho player 1 hoặc -1
                        player = (player + 1) % 2                        #Đổi người chơi
                        winner = check_winner(cell_x, cell_y, cnt)
                        if winner != None:
                            game_over = True

            if mode == 2:
                if winner == None:
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #Nếu click chuột trái thì mới được tính là đã click
                        clicked = True
                    if event.type == pygame.MOUSEBUTTONUP  and clicked == True:
                        clicked = False
                        pos = pygame.mouse.get_pos()
                        if menu_rect.collidepoint(pos): #Nếu click vào ô menu thì sẽ quay trở lại menu
                            restart()
                            mode = None
                            continue
                        cell_x = pos[0] // 30
                        cell_y = pos[1] // 30
                        if markers[cell_x][cell_y] != -1 or cell_x == 19 or cell_x == 0 or cell_y == 19 or cell_y == 0:    #Nếu 1 ô đã được đánh dấu rồi thì không được thao tác trên ô đó nữa
                            continue
                        if player == 0:             #Player 1 thì dùng sound0
                            movement_sound0.play()
                        else:                       #Player 2, 3 thì dùng sound1
                            movement_sound1.play()
                        x, y = cell_x, cell_y
                        cnt += 1
                        markers[cell_x][cell_y] = player    #Gán giá trị của ô cho player 1 hoặc -1
                        player = (player + 1) % 3                        #Đổi người chơi
                        winner = check_winner(cell_x, cell_y, cnt)
                        if winner != None:
                            game_over = True
            if mode == 3:
                if winner == None:
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #Nếu click chuột trái thì mới được tính là đã click
                        clicked = True
                    if event.type == pygame.MOUSEBUTTONUP  and clicked == True:
                        clicked = False
                        pos = pygame.mouse.get_pos()
                        if menu_rect.collidepoint(pos): #Nếu click vào ô menu thì sẽ quay trở lại menu
                            restart()
                            mode = None
                            continue
                        cell_x = pos[0] // 30
                        cell_y = pos[1] // 30
                        if markers[cell_x][cell_y] != -1 or cell_x == 19 or cell_x == 0 or cell_y == 19 or cell_y == 0:    #Nếu 1 ô đã được đánh dấu rồi thì không được thao tác trên ô đó nữa
                            continue
                        if player == 0:             #Player 1 thì dùng sound0
                            movement_sound0.play()
                        else:                       #Player 2 thì dùng sound1
                            movement_sound1.play()
                        x, y = cell_x, cell_y
                        cnt += 1
                        markers[cell_x][cell_y] = player    #Gán giá trị của ô cho player 1 hoặc -1
                        player = (player + 1) % 2                        #Đổi người chơi
                        winner = check_winner(cell_x, cell_y, cnt)
                        if winner != None:
                            game_over = True
    
    if game_over == True:
        draw_grid()
        draw_markers()
        check_winner(cell_x, cell_y, cnt)
        draw_winner()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP  and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                restart()
            if menu_rect.collidepoint(pos): #Nếu click vào ô menu thì sẽ quay trở lại menu
                restart()
                screen.fill(black)
                mode = None
    pygame.display.update()

pygame.quit()