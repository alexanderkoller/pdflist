
import pygame

from helpers import *

import synchronize

# WIDTH = 640
# HEIGHT = 480
# COLOR_DEPTH = 32

BG_SCREEN = (255,255,255)

UNSEL_TEXT_COLOR = (0,0,0)
UNSEL_TEXT_BG = (255,255,255)

SEL_TEXT_COLOR = (0,0,0)
SEL_TEXT_BG = (200,200,200)



pygame.init()

def create_screen():
    if conf.getboolean("General", "fullscreen"):
        return pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # modes = pygame.display.list_modes(COLOR_DEPTH)
        # WIDTH, HEIGHT = modes[0]
        # return pygame.display.set_mode(modes[0], pygame.FULLSCREEN, COLOR_DEPTH) # modes[0] is highest resolution with this depth

    else:
        return pygame.display.set_mode((640, 480))


screen = create_screen()

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

X_PROJECT = int(WIDTH*0.5)
X_MODTIME = int(WIDTH*0.8)
fontsize = WIDTH//40




font = pygame.font.SysFont("Helvetica", fontsize)
files = synchronize.synchronize()
selected_index = 0

files.sort(key=lambda x: x.date, reverse=True)


# TODO - if needed, crop texts using extra argument of blit

def draw_link(pdflink, y, selected, surface):
    name_text = font.render(pdflink.name, True, (0,0,0))
    proj_text = font.render(pdflink.project, True, (0,0,0))
    time_text = font.render(pdflink.sdate(), True, (0,0,0))

    h = name_text.get_height()
    ypos = h*y

    if selected:
        pygame.draw.rect(surface, SEL_TEXT_BG, pygame.Rect(0, ypos, WIDTH, h))

    screen.blit(name_text, (0, ypos))
    screen.blit(proj_text, (X_PROJECT, ypos))
    screen.blit(time_text, (X_MODTIME, ypos))


def open(pdflink):
    cmd = conf.get("General", "command")
    sp(cmd % pdflink.abs_filename)


# configure keys
keydict = {}
for key in range(300):
    if pygame.key.name(key):
        keydict[pygame.key.name(key)] = key

up_key = keydict[conf.get("General", "up_key")]
down_key = keydict[conf.get("General", "down_key")]
quit_key = keydict[conf.get("General", "quit_key")]
select_key = keydict[conf.get("General", "select_key")]



clock = pygame.time.Clock()
done = False

# main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == down_key and selected_index < len(files)-1:
                selected_index += 1
            elif event.key == up_key and selected_index > 0:
                selected_index -= 1
            elif event.key == select_key:
                open(files[selected_index])
            elif event.key == quit_key:
                done = True

    if not done:
        screen.fill(BG_SCREEN)

        for row, pdflink in enumerate(files):
            draw_link(pdflink, row, (row == selected_index), screen)

        pygame.display.flip()
        clock.tick(60)


