import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

# Tạo một bề mặt có độ trong suốt
image = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.rect(image, (255, 0, 0, 128), (0, 0, 100, 100))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))  # Xóa màn hình bằng màu đen
    screen.blit(image, (100, 100))  # Vẽ bề mặt lên màn hình tại tọa độ (100, 100)

    pygame.display.update()

pygame.quit()
