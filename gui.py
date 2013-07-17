#!/usr/bin/env python
import pygame
import time
from gol_classes import b, Cell
import os

live_cell_sprite = pygame.image.load(os.path.join('assets', 'live_cell.bmp'))
dead_cell_sprite = pygame.image.load(os.path.join('assets', 'dead_cell.bmp'))

WIDTH = 1280
HEIGTH = 1280

def draw_cell(surface, cell, alive):
    surface.blit(
        live_cell_sprite if alive else dead_cell_sprite,
        (cell.x * 40, cell.y * 40)
    )

pygame.init()
surface = pygame.display.set_mode((HEIGTH, WIDTH))
x, y = 0, 0

class Quit(Exception): pass
try:
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                 raise Quit()
            if evt.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                cell = Cell(x // 40, y // 40)
                b.live_cells.append(cell)
                draw_cell(surface, cell, b.is_cell_alive(cell))
            elif evt.type == pygame.KEYDOWN:
                b = b.next_generation()

        #cells_iter = b.matrix(HEIGTH, WIDTH)
        surface.fill((0, 0, 0))
        for x in range(WIDTH // 40):
            for y in range(HEIGTH // 40):
                cell = Cell(x, y)
                draw_cell(surface, cell, b.is_cell_alive(cell))

        time.sleep(0.1)
        pygame.display.flip()

except Quit:
    print('quit')
    
finally:
    pygame.quit()
