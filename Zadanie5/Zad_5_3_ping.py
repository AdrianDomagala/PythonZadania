import pygame
from random import randint

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)


class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def move_left(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 600:
            self.rect.x = 600


class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(-8, 8), randint(5, 7)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-8, 8)


# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong Single Player")

rakietka = Rakietka(BIALY, 100, 10)
rakietka.rect.x = 300
rakietka.rect.y = 480

pileczka = Pilka(BIALY, 10, 10)
pileczka.rect.x = randint(150, 550)
pileczka.rect.y = randint(20, 100)

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie rakietki i piłeczki do listy
all_sprites_list.add(rakietka)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowe wyniki graczy
score = 0
best = [0, 0, 0]

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    # ruchy Rakietki
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rakietka.move_right(5)
    if keys[pygame.K_LEFT]:
        rakietka.move_left(5)

    # aktualizacja listy duszków
    all_sprites_list.update()

    # sprawdzenie czy piłeczka nie uderza w którąś ścianę
    # i odpowiednie naliczenie punktu
    if pygame.sprite.collide_mask(pileczka, rakietka):
        score += 1
        pileczka.bounce()

    if pileczka.rect.y >= 490:
        screen.fill(CZARNY)

        best.append(score)
        best.sort(reverse=1)
        best = best[:3]
        score = 0

        screen.blit(font.render('GAME OVER', 1, BIALY), (200, 100))
        font = pygame.font.Font(None, 50)
        screen.blit(font.render('Scoreboard:', 1, BIALY), (200, 200))
        scoreboard = 'GAME OVER' + "\n" + 'Scoreboard' + '\n\n'
        for i, scr in enumerate(best, 1):
            text = f'{i})     {scr}'
            screen.blit(font.render(text, 1, BIALY), (200, (i + 4) * 50))
        font = pygame.font.Font(None, 35)
        screen.blit(font.render('press space to play again', 1, BIALY), (340, 430))
        pygame.display.flip()

        wait = True
        while wait:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                kontynuuj = False
                wait = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                wait = False
            clock.tick(60)

        pileczka.rect.x = randint(150, 550)
        pileczka.rect.y = randint(20, 100)
        rakietka.rect.x = 300
        rakietka.rect.y = 480

    if pileczka.rect.x > 690:
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.x < 0:
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.y < 0:
        pileczka.velocity[1] = -pileczka.velocity[1]

    # RYSOWANIE
    # czarny ekran
    screen.fill(CZARNY)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyników
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, BIALY)
    screen.blit(text, (332, 10))

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()