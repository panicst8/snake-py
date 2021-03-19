""" Snake the game """

import math
import random
import pygame
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

    def __init__(self, color: Any, pos: Any):
        pass

    def move(self) -> Any:
        """ move method """

    def reset(self, pos: Any) -> Any:
        """ reset method """

    def addCube(self) -> Any:
        """ addcube method """

    def draw(self, surface: Any) -> Any:
        """ draw method """


def drawGrid(w: Any, rows: Any, surface: Any) -> Any:
    """ drawGrid function """


def redrawWindow(surface: Any) -> Any:
    """ redrawWindow function """


def randomSnack(rows: Any, items: Any) -> Any:
    """ randomSnack function """


def message_box(subject: Any, content: Any) -> Any:
    """ message_box function """


def main() -> None:
    """ main function """
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = Snake((255, 0, 0), (10, 10))
    run = True
    clock = pygame.time.Clock()
    while run:
        pygame.time.delay(50)
        clock.tick(10)


if __name__ == "__main__":
    main()
