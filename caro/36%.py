import pygame

pygame.init()

screen_width = 600
screen_height = 600
line_width = 1

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')
movement_sound1 = pygame.mixer.Sound('sound\\tic.wav')
movement_sound2 = pygame.mixer.Sound('sound\\ticc.wav')

markers = [[0 for _ in range(20)] for _ in range(20)]  #Lưu các ô đã được đánh dấu X và O
clicked = False  #Kiểm tra xem đã click hay chưa
player = 1          
winner = None       
game_over = False
cnt = 0    #Đếm xem bao nhiêu ô đã được đánh dấu

#Đĩnh nghĩa màu và font chữ
blue = (53, 126, 242)
green = (32, 230, 38)
red = (255, 0, 0)
gray = (186, 184, 179)
white = (255, 255, 255)
font = pygame.font.SysFont("monotype", 40)

#Hình vuông đánh lại
again_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 10, 300, 50)

#Vẽ lưới
def draw_grid():
    bg = ((255,255,255))
    screen.fill(bg)
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
            if markers[x][y] == -1:
                center_x = x * 30 + 15
                center_y = y * 30 + 15
                pygame.draw.circle(screen, green, (center_x + 0.75, center_y + 0.75), 10, line_width + 2)
            if markers[x][y] == 1:
                pygame.draw.line(screen, red, (x * 30 + 7, y * 30 + 7), ((x + 1) * 30 - 7, (y + 1) * 30 - 7), line_width + 2)
                pygame.draw.line(screen, red, (x * 30 + 7, (y + 1) * 30 - 7), ((x + 1) * 30 - 7, y * 30 + 7), line_width + 2)

#Kiểm tra người thắng
def check_winner(x, y, cnt):
    # Check hàng ngang
    if x <= 14 and sum(markers[x + i][y] for i in range(5)) == 5:
        return 1
    if x <= 14 and sum(markers[x + i][y] for i in range(5)) == -5:
        return 2

    if x <= 15 and x >= 2 and sum(markers[x + i][y] for i in range(-1, 4)) == 5:
        return 1
    if x <= 15 and x >= 2 and sum(markers[x + i][y] for i in range(-1, 4)) == -5:
        return 2

    if x <= 16 and x >= 3 and sum(markers[x + i][y] for i in range(-2, 3)) == 5:
        return 1
    if x <= 16 and x >= 3 and sum(markers[x + i][y] for i in range(-2, 3)) == -5:
        return 2

    if x <= 17 and x >= 4 and sum(markers[x + i][y] for i in range(-3, 2)) == 5:
        return 1
    if x <= 17 and x >= 4 and sum(markers[x + i][y] for i in range(-3, 2)) == -5:
        return 2

    if x <= 18 and x >= 4 and sum(markers[x + i][y] for i in range(-4, 1)) == 5:
        return 1
    if x <= 18 and x >= 4 and sum(markers[x + i][y] for i in range(-4, 1)) == -5:
        return 2
    #Check hàng dọc
    if y <= 14 and sum(markers[x][y + i] for i in range(5)) == 5:
        return 1
    if y <= 14 and sum(markers[x][y + i] for i in range(5)) == -5:
        return 2

    if y <= 15 and y >= 2 and sum(markers[x][y + i] for i in range(-1, 4)) == 5:
        return 1
    if y <= 15 and y >= 2 and sum(markers[x][y + i] for i in range(-1, 4)) == -5:
        return 2

    if y <= 16 and y >= 3 and sum(markers[x][y + i] for i in range(-2, 3)) == 5:
        return 1
    if y <= 16 and y >= 3 and sum(markers[x][y + i] for i in range(-2, 3)) == -5:
        return 2

    if y <= 17 and y >= 4 and sum(markers[x][y + i] for i in range(-3, 2)) == 5:
        return 1
    if y <= 17 and y >= 4 and sum(markers[x][y + i] for i in range(-3, 2)) == -5:
        return 2

    if y <= 18 and y >= 5 and sum(markers[x][y + i] for i in range(-4, 1)) == 5:
        return 1
    if y <= 18 and y >= 5 and sum(markers[x][y + i] for i in range(-4, 1)) == -5:
        return 2

    #Check hàng chéo góc phần tư thứ II và IV
    if x <= 14 and y <= 14 and sum(markers[x + i][y + i] for i in range(5)) == 5:
        return 1
    if x <= 14 and y <= 14 and sum(markers[x + i][y + i] for i in range(5)) == -5:
        return 2

    if x <= 15 and y <= 15 and x >= 2 and y >= 2 and sum(markers[x + i][y + i] for i in range(-1, 4)) == 5:
        return 1
    if x <= 15 and y <= 15 and x >= 2 and y >= 2 and sum(markers[x + i][y + i] for i in range(-1, 4)) == -5:
        return 2

    if x <= 16 and y <= 16 and x >= 3 and y >= 3 and sum(markers[x + i][y + i] for i in range(-2, 3)) == 5:
        return 1
    if x <= 16 and y <= 16 and x >= 3 and y >= 3 and sum(markers[x + i][y + i] for i in range(-2, 3)) == -5:
        return 2

    if x <= 17 and y <= 17 and x >= 4 and y >= 4 and sum(markers[x + i][y + i] for i in range(-3, 2)) == 5:
        return 1
    if x <= 17 and y <= 17 and x >= 4 and y >= 4 and sum(markers[x + i][y + i] for i in range(-3, 2)) == -5:
        return 2

    if x <= 18 and y <= 18 and x >= 5 and y >= 5 and sum(markers[x + i][y + i] for i in range(-4, 1)) == 5:
        return 1
    if x <= 18 and y <= 18 and x >= 5 and y >= 5 and sum(markers[x + i][y + i] for i in range(-4, 1)) == -5:
        return 2

    #Check chéo góc phần tư thứ I và III
    if x <= 14 and y >= 5 and sum(markers[x + i][y - i] for i in range(5)) == 5:
        return 1
    if x <= 14 and y >= 5 and sum(markers[x + i][y - i] for i in range(5)) == -5:
        return 2

    if x <= 15 and y <= 17 and y >= 4 and sum(markers[x + i][y - i] for i in range(-1, 4)) == 5:
        return 1
    if x <= 15 and y <= 17 and y >= 4 and sum(markers[x + i][y - i] for i in range(-1, 4)) == -5:
        return 2
    
    if x <= 16 and y <= 16 and y >= 3 and sum(markers[x + i][y - i] for i in range(-2, 3)) == 5:
        return 1
    if x <= 16 and y <= 16 and y >= 3 and sum(markers[x + i][y - i] for i in range(-2, 3)) == -5:
        return 2

    if x <= 17 and y <= 15 and y >= 2 and sum(markers[x + i][y - i] for i in range(-3, 2)) == 5:
        return 1
    if x <= 17 and y <= 15 and y >= 2 and sum(markers[x + i][y - i] for i in range(-3, 2)) == -5:
        return 2

    if x <= 18  and y <= 14 and sum(markers[x + i][y - i] for i in range(-4, 1)) == 5:
        return 1
    if x <= 18  and y <= 14 and sum(markers[x + i][y - i] for i in range(-4, 1)) == 5:
        return 2    

    # Nếu đánh hết bàn cờ mà chưa có người thắng thì là hòa
    if cnt == 18*18:
        return 0
    # Nếu chưa đánh hết thì chưa có người thắng
    return None

def draw_winner():
    if winner == 1:
        win_text = "Player 1 won"
    elif winner == 2:
        win_text = "Player 2 won"
    else:
        win_text = "Draw"
    win_img = font.render(win_text, True, white)
    if winner == 1:
        pygame.draw.rect(screen, red, (screen_width // 2 - 150, screen_height // 2 - 50, 300, 50))
    elif winner == 2:
        pygame.draw.rect(screen, green, (screen_width // 2 - 150, screen_height // 2 - 50, 300, 50))
    screen.blit(win_img, (screen_width // 2 - 150, screen_height // 2 - 50))

    again_text = "Play again?"
    again_img = font.render(again_text, True, white)
    pygame.draw.rect(screen, blue, again_rect)
    screen.blit(again_img, (screen_width // 2 - 125, screen_height // 2 + 10))

# Khởi tạo lại trò chơi
def restart():
    global markers, player, winner, game_over
    markers = [[0 for _ in range(20)] for _ in range(20)] 
    player = 1          
    winner = None       
    game_over = False
    cnt = 0

run = True

while run:

    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if winner == None:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #Nếu click chuột trái thì mới được tính là đã click
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP  and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 30
                cell_y = pos[1] // 30
                if markers[cell_x][cell_y] != 0 or cell_x == 19 or cell_x == 0 or cell_y == 19 or cell_y == 0:    #Nếu 1 ô đã được đánh dấu rồi thì không được thao tác trên ô đó nữa
                    continue
                if player == 1:             #Player 1 thì dùng sound1
                    movement_sound1.play()
                else:                       #Player 2 thì dùng sound1
                    movement_sound2.play()
                cnt += 1
                markers[cell_x][cell_y] = player    #Gán giá trị của ô cho player 1 hoặc -1
                player *= -1                        #Đổi người chơi
                print(cell_x, cell_y, cnt)
                winner = check_winner(cell_x, cell_y, cnt)
                if winner != None:
                    game_over = True
    
    if game_over == True:
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