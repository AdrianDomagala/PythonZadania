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

    speed = [0, 0]
    accel = [0.15, 0.15]

    image = pygame.transform.scale(icon, size)

    surf_center = ((width - image.get_width()) / 2,
                   (height - image.get_height()) / 2)
    screen.blit(image, surf_center)

    ball = pygame.image.load("files/met_s.png")
    screen.blit(ball, (width / 2 - ball.get_width() / 2, height / 2 - ball.get_height() / 2))
    ballrect = ball.get_rect(center=(width / 2, height / 2))

    pygame.display.flip()

    while True:
        clock.tick(60)
        # print((clock.get_fps()))
        pygame.time.delay(17)

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            speed[1] -= accel[1]
        elif keys[pygame.K_DOWN]:
            speed[1] += accel[1]
        elif keys[pygame.K_LEFT]:
            speed[0] -= accel[0]
        elif keys[pygame.K_RIGHT]:
            speed[0] += accel[0]

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()


pygame.init()

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
