""" Snake the game """

import math
import random
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox
from typing import Any


class Cube(object):
    """ Cube class """

    rows = 0
    w = 0

    def __init__(
        self, start: Any, dirnx: int = 1, dirny: int = 0, color: Any = (255, 0, 0)
    ):
        pass

    def move(self, dirnx: int, dirny: int) -> Any:
        """ move method """

    def draw(self, surface: Any, eyes: bool = False) -> Any:
        """ draw method """


class Snake(object):
    """ Snake class """

    body: list = []
    turns: set = {}

    def __init__(self, color: Any, pos: Any):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self) -> Any:
        """ move method """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def reset(self, pos: Any) -> Any:
        """ reset method """

    def addCube(self) -> Any:
        """ addcube method """

    def draw(self, surface: Any) -> Any:
        """ draw method """


def drawGrid(height: int, width: int, rows: int, win: Any) -> Any:
    """ drawGrid function """
    size_between = width // rows
    x = 0
    y = 0
    for _ in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(win, (255, 255, 255), (x, 0), (x, height))
        pygame.draw.line(win, (255, 255, 255), (0, y), (width, y))


def redrawWindow(win: Any, height: int, width: int, rows: int) -> Any:
    """ redrawWindow function """
    win.fill((0, 0, 0))
    drawGrid(height, width, rows, win)
    pygame.display.update()


def randomSnack(rows: Any, items: Any) -> Any:
    """ randomSnack function """


def message_box(subject: Any, content: Any) -> Any:
    """ message_box function """


def main() -> None:
    """ main function """
    width = 500
    height = 500
    rows = 20
    s = Snake((255, 0, 0), (10, 10))

    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake -- The Game")
    run = True
    clock = pygame.time.Clock()
    pygame.event.get()  # TODO: remove once event loop setup later

    while run:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win, height, width, rows)


if __name__ == "__main__":
    main()
