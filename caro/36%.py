import pygame
import random

pygame.init()

screen_width = 600
screen_height = 600
line_width = 1

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')
movement_sound0 = pygame.mixer.Sound('sound\\tic.wav')
movement_sound1 = pygame.mixer.Sound('sound\\ticc.wav')

markers = [[-1 for _ in range(20)] for _ in range(20)]  #Lưu các ô đã được đánh dấu X và O
clicked = False  #Kiểm tra xem đã click hay chưa
player = 0   
winner = None       
game_over = False
cnt = 0    #Đếm xem bao nhiêu ô đã được đánh dấu
mode = None

#Đĩnh nghĩa màu và font chữ
blue = (53, 126, 242)
green = (32, 230, 38)
red = (255, 0, 0)
gray = (186, 184, 179)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (209, 201, 42)
font = pygame.font.SysFont("monotype", 40)

#Hình vuông đánh lại
again_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 10, 300, 50)
mode_rect = pygame.Rect(100, 50, 400, 50)
mode_rect1 = pygame.Rect(100, 200, 400, 50)
mode_rect2 = pygame.Rect(100, 300, 400, 50)
mode_rect3 = pygame.Rect(100, 400, 400, 50)

def draw_menu():
    pygame.draw.rect(screen, white, mode_rect)
    text = "SELECT MODE"
    text_img = font.render(text, True, black)
    screen.blit(text_img, (170, 50))
    pygame.draw.rect(screen, white, mode_rect1)

    text = "2 PLAYERS"
    text_img = font.render(text, True, black)
    screen.blit(text_img, (180, 200))
    pygame.draw.rect(screen, white, mode_rect2)

    text = "3 PLAYERS"
    text_img = font.render(text, True, black)
    screen.blit(text_img, (180, 300))
    pygame.draw.rect(screen, white, mode_rect3)

    text = "BLIND TIC TAC TOE"
    text_img = font.render(text, True, black)
    screen.blit(text_img, (95, 400))

#Vẽ lưới
def draw_grid():
    screen.fill(white)
    x = 1
    pygame.draw.line(screen, gray, (30, x * 30), (screen_width - 30, x * 30), line_width + 2)
    pygame.draw.line(screen, gray, (x * 30, 30), (x * 30, screen_height - 30), line_width + 2)
    x = 19
    pygame.draw.line(screen, gray, (30, x * 30), (screen_width - 30, x * 30), line_width + 2)
    pygame.draw.line(screen, gray, (x * 30, 30), (x * 30, screen_height - 30), line_width + 2)
    for x in range(2, 19):
        pygame.draw.line(screen, gray, (30, x * 30), (screen_width - 30, x * 30), line_width)
        pygame.draw.line(screen, gray, (x * 30, 30), (x * 30, screen_height - 30), line_width)

#Vẽ X và O    
def draw_markers():
    for x in range(1, 19):
        for y in range(1, 19):
            if markers[x][y] == 0:
                pygame.draw.line(screen, red, (x * 30 + 7, y * 30 + 7), ((x + 1) * 30 - 7, (y + 1) * 30 - 7), line_width + 2)
                pygame.draw.line(screen, red, (x * 30 + 7, (y + 1) * 30 - 7), ((x + 1) * 30 - 7, y * 30 + 7), line_width + 2)
            if markers[x][y] == 1:
                center_x = x * 30 + 15
                center_y = y * 30 + 15
                pygame.draw.circle(screen, green, (center_x + 0.75, center_y + 0.75), 10, line_width + 2)
            if markers[x][y] == 2:
                pygame.draw.line(screen, blue, (x * 30 + 7, (y + 1) * 30 - 7), ((x + 1) * 30 - 7, y * 30 + 7), line_width + 2)

def draw_markers3():            
    for x in range(1, 19):
        for y in range(1, 19):
            if markers[x][y] != -1:
                center_x = x * 30 + 15
                center_y = y * 30 + 15
                pygame.draw.circle(screen, yellow, (center_x + 0.75, center_y + 0.75), 10, line_width + 2)
#Kiểm tra người thắng
def check_winner(x, y, cnt):
    # Check hàng ngang
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if x + r <= 19 and x + l >= 1 and markers[x + l][y] == markers[x + l + 1][y] == markers[x + l + 2][y] == markers[x + l + 3][y] == markers[x + l + 4][y] == 0:
            pygame.draw.line(screen, red, ((x + l) * 30, y * 30 + 15), ((x + r) * 30, y * 30 + 15), line_width + 3)
            return 1
        if x + r <= 19 and x + l >= 1 and markers[x + l][y] == markers[x + l + 1][y] == markers[x + l + 2][y] == markers[x + l + 3][y] == markers[x + l + 4][y] == 1:
            pygame.draw.line(screen, green, ((x + l) * 30, y * 30 + 15), ((x + r) * 30, y * 30 + 15), line_width + 3)
            return 2
        if x + r <= 19 and x + l >= 1 and markers[x + l][y] == markers[x + l + 1][y] == markers[x + l + 2][y] == markers[x + l + 3][y] == markers[x + l + 4][y] == 2:
            pygame.draw.line(screen, blue, ((x + l) * 30, y * 30 + 15), ((x + r) * 30, y * 30 + 15), line_width + 3)
            return 3
        l -= 1
        r -= 1
    #Check hàng dọc
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if y + r <= 19 and y + l >= 1 and markers[x][y + l] == markers[x][y + l + 1] == markers[x][y + l + 2] == markers[x][y + l + 3] == markers[x][y + l + 4] == 0:
            pygame.draw.line(screen, red, (x * 30 + 15, (y + l) * 30), (x * 30 + 15, (y + r) * 30), line_width + 3)
            return 1
        if y + r <= 19 and y + l >= 1 and markers[x][y + l] == markers[x][y + l + 1] == markers[x][y + l + 2] == markers[x][y + l + 3] == markers[x][y + l + 4] == 1:
            pygame.draw.line(screen, green, (x * 30 + 15, (y + l) * 30), (x * 30 + 15, (y + r) * 30), line_width + 3)
            return 2
        if y + r <= 19 and y + l >= 1 and markers[x][y + l] == markers[x][y + l + 1] == markers[x][y + l + 2] == markers[x][y + l + 3] == markers[x][y + l + 4] == 2:
            pygame.draw.line(screen, blue, (x * 30 + 15, (y + l) * 30), (x * 30 + 15, (y + r) * 30), line_width + 3)
            return 2
        l -= 1
        r -= 1
    #Check hàng chéo góc phần tư thứ II và IV
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if x + r <= 19 and y + r <= 19 and x + l >= 1 and y + l >= 1 and markers[x + l][y + l] == markers[x + l + 1][y + l + 1] == markers[x + l + 2][y + l + 2] == markers[x + l + 3][y + l + 3] == markers[x + l + 4][y + l + 4] == 0:
            pygame.draw.line(screen, red, ((x + r) * 30, (y + r) * 30), ((x + l) * 30, (y + l) * 30), line_width + 3)
            return 1
        if x + r <= 19 and y + r <= 19 and x + l >= 1 and y + l >= 1 and markers[x + l][y + l] == markers[x + l + 1][y + l + 1] == markers[x + l + 2][y + l + 2] == markers[x + l + 3][y + l + 3] == markers[x + l + 4][y + l + 4] == 1:
            pygame.draw.line(screen, green, ((x + r) * 30, (y + r) * 30), ((x + l) * 30, (y + l) * 30), line_width + 3)
            return 2
        if x + r <= 19 and y + r <= 19 and x + l >= 1 and y + l >= 1 and markers[x + l][y + l] == markers[x + l + 1][y + l + 1] == markers[x + l + 2][y + l + 2] == markers[x + l + 3][y + l + 3] == markers[x + l + 4][y + l + 4] == 2:
            pygame.draw.line(screen, blue, ((x + r) * 30, (y + r) * 30), ((x + l) * 30, (y + l) * 30), line_width + 3)
            return 3
        l -= 1
        r -= 1
    #Check chéo góc phần tư thứ I và III
    l, r = 0, 5
    while l >= -4 and r >= 1:
        if x + r <= 19 and y - r >= 0 and x + l >= 1 and y - l <= 18 and markers[x + l][y - l] == markers[x + l + 1][y - l - 1] == markers[x + l + 2][y - l - 2] == markers[x + l + 3][y - l - 3] == markers[x + l + 4][y - l - 4] == 0:
            pygame.draw.line(screen, red, ((x + l) * 30, (y - l + 1) * 30), ((x + r) * 30, (y - r + 1) * 30), line_width + 3)
            return 1
        if x + r <= 19 and y - r >= 0 and x + l >= 1 and y - l <= 18 and markers[x + l][y - l] == markers[x + l + 1][y - l - 1] == markers[x + l + 2][y - l - 2] == markers[x + l + 3][y - l - 3] == markers[x + l + 4][y - l - 4] == 1:
            pygame.draw.line(screen, green, ((x + l) * 30, (y - l + 1) * 30), ((x + r) * 30, (y - r + 1) * 30), line_width + 3)
            return 2
        if x + r <= 19 and y - r >= 0 and x + l >= 1 and y - l <= 18 and markers[x + l][y - l] == markers[x + l + 1][y - l - 1] == markers[x + l + 2][y - l - 2] == markers[x + l + 3][y - l - 3] == markers[x + l + 4][y - l - 4] == 2:
            pygame.draw.line(screen, blue, ((x + l) * 30, (y - l + 1) * 30), ((x + r) * 30, (y - r + 1) * 30), line_width + 3)
            return 3
        l -= 1
        r -= 1
    # Nếu đánh hết bàn cờ mà chưa có người thắng thì là hòa
    if cnt == 18 * 18:
        return 0
    # Nếu chưa đánh hết thì chưa có người thắng
    return None

def draw_winner():
    if winner == 1:
        win_text = "Player 1 won"
    elif winner == 2:
        win_text = "Player 2 won"
    elif winner == 3:
        win_text = "Player 3 won"
    else:
        win_text = "Draw"
    win_img = font.render(win_text, True, white)
    if winner == 1:
        pygame.draw.rect(screen, red, (screen_width // 2 - 150, screen_height // 2 - 50, 300, 50))
    elif winner == 2:
        pygame.draw.rect(screen, green, (screen_width // 2 - 150, screen_height // 2 - 50, 300, 50))
    elif winner == 3:
        pygame.draw.rect(screen, blue, (screen_width // 2 - 150, screen_height // 2 - 50, 300, 50))
    else:
        pygame.draw.rect(screen, yellow, (screen_width // 2 - 150, screen_height // 2 - 50, 300, 50))
    screen.blit(win_img, (screen_width // 2 - 150, screen_height // 2 - 50))
        
    again_text = "Play again?"
    again_img = font.render(again_text, True, white)
    pygame.draw.rect(screen, blue, again_rect)
    screen.blit(again_img, (screen_width // 2 - 125, screen_height // 2 + 10))

# Khởi tạo lại trò chơi
def restart():
    global markers, player, winner, game_over
    markers = [[-1 for _ in range(20)] for _ in range(20)] 
    player = 0          
    winner = None       
    game_over = False
    cnt = 0

run = True

while run:

    if mode == None:
        #Vẽ menu
        draw_menu()
    elif mode == 1 or mode == 2:
        draw_grid()
        draw_markers()
    elif mode == 3:
        draw_grid()
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
                if mode_rect1.collidepoint(pos):
                    mode = 1
                if mode_rect2.collidepoint(pos):
                    mode = 2
                if mode_rect3.collidepoint(pos):
                    mode = 3
        else:
            if mode == 1:
                if winner == None:
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #Nếu click chuột trái thì mới được tính là đã click
                        clicked = True
                    if event.type == pygame.MOUSEBUTTONUP  and clicked == True:
                        clicked = False
                        pos = pygame.mouse.get_pos()
                        cell_x = pos[0] // 30
                        cell_y = pos[1] // 30
                        if markers[cell_x][cell_y] != -1 or cell_x == 19 or cell_x == 0 or cell_y == 19 or cell_y == 0:    #Nếu 1 ô đã được đánh dấu rồi thì không được thao tác trên ô đó nữa
                            continue
                        if player == 0:             #Player 1 thì dùng sound0
                            movement_sound0.play()
                        else:                       #Player 2 thì dùng sound1
                            movement_sound1.play()
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
                        cell_x = pos[0] // 30
                        cell_y = pos[1] // 30
                        if markers[cell_x][cell_y] != -1 or cell_x == 19 or cell_x == 0 or cell_y == 19 or cell_y == 0:    #Nếu 1 ô đã được đánh dấu rồi thì không được thao tác trên ô đó nữa
                            continue
                        if player == 0:             #Player 1 thì dùng sound0
                            movement_sound0.play()
                        else:                       #Player 2, 3 thì dùng sound1
                            movement_sound1.play()
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
                        cell_x = pos[0] // 30
                        cell_y = pos[1] // 30
                        if markers[cell_x][cell_y] != -1 or cell_x == 19 or cell_x == 0 or cell_y == 19 or cell_y == 0:    #Nếu 1 ô đã được đánh dấu rồi thì không được thao tác trên ô đó nữa
                            continue
                        if player == 0:             #Player 1 thì dùng sound0
                            movement_sound0.play()
                        else:                       #Player 2 thì dùng sound1
                            movement_sound1.play()
                        cnt += 1
                        markers[cell_x][cell_y] = player    #Gán giá trị của ô cho player 1 hoặc -1
                        player = (player + 1) % 2                        #Đổi người chơi
                        winner = check_winner(cell_x, cell_y, cnt)
                        if winner != None:
                            game_over = True
    
    if game_over == True:
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

    pygame.display.update()

pygame.quit()