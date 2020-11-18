import pygame
import sys


def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption("Game")
    icon = pygame.image.load("files/photo_nasa.jpg")
    pygame.display.set_icon(icon)

    pygame.mixer.music.load('files/Star Commander1.wav')
    pygame.mixer.music.play(-1)

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    speed = [0, 0]  # [30, 100]  [20, 30]
    accel = [0, 9.81]

    image = pygame.transform.scale(icon, size)

    surf_center = ((width - image.get_width()) / 2,
                   (height - image.get_height()) / 2)
    screen.blit(image, surf_center)

    ball = pygame.image.load("files/met_s.png")
    screen.blit(ball, (width / 2 - ball.get_width() / 2, height / 2 - ball.get_height() / 2))
    ballrect = ball.get_rect(center=(width / 2, height / 2))

    pygame.display.flip()

    pygame.time.delay(200)

    while True:
        clock.tick(60)
        # print((clock.get_fps()))
        pygame.time.delay(75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        speed[1] += accel[1]

        if ballrect.bottom + speed[1] >= height:
            ballrect = ballrect.move(0, height - ballrect.bottom)
            speed[1] = -speed[1]
        elif ballrect.left + speed[0] <= 0:
            ballrect = ballrect.move((-ballrect.left, 0))
            speed[0] = -speed[0]
        elif ballrect.right + speed[0] >= width:
            ballrect = ballrect.move((width - ballrect.right, 0))
            speed[0] = -speed[0]
        else:
            ballrect = ballrect.move(speed)

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()


pygame.init()

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
