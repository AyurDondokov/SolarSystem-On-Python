
from Planet import Planet
from Button import *
from Colors import *

WIDTH = 1080
HEIGHT = 800
FPS = 60

BUTTON_POS = 50

def read_planets_file(screen, fileWay):
    f = open(fileWay)
    c = 0
    planets = []
    buttons = []
    for l in f:
        c += 1
        info = l.split()
        planets.append(Planet(screen, info[0], float(info[1]), float(info[2]), info[3], 1 / float(info[4])))
        buttons.append(Button(screen, [BUTTON_POS, 100 + BUTTON_POS*c], "sprites/"+info[0]+".png", planet_info(planets[c-1])))
    return planets, buttons

def planet_info(planet):
    return ( planet.get_info() )


def RunSolarSistem():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Solar System")
    clock = pygame.time.Clock()

    screenColor = (0, 0, 0)

    planets, buttons = read_planets_file(screen, "planets.txt")
    text = Text(screen, "Click on planet!", (10, 50), 40, "Pixel.ttf", get_color("red"))

    # Цикл игры
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m = pygame.mouse.get_pos()
                for b in buttons:
                    if b.is_press(m):
                        text.text = b.function
                for p in planets:
                    if p.press(m):
                        text.text = p.get_info()
        pygame.draw.circle(screen, get_color("yellow"), (WIDTH/2, HEIGHT/2), 5)
        screen.fill(screenColor)
        clock.tick(FPS)
        text.out()
        for i in planets:
            i.output()
        for i in buttons:
            i.out()

        pygame.display.flip()

RunSolarSistem()

pygame.quit()