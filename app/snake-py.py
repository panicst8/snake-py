""" Snake the game """

import random
import pygame
from typing import Any, List


class Cube(object):
    """ Cube class """

    def __init__(
        self,
        start: Any,
        width: int,
        rows: int,
        dirnx: int = 1,
        dirny: int = 0,
        color: Any = (255, 0, 0),
    ):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color
        self.width = width
        self.rows = rows

    def move(self, dirnx: int, dirny: int) -> Any:
        """ move method """
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, win: Any, eyes: bool = False) -> Any:
        """ draw method """
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(win, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(win, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(win, (0, 0, 0), circleMiddle2, radius)


class Snake(object):
    """ Snake class """

    body: List[Any] = []
    turns = {}  # type: ignore

    def __init__(self, color: Any, pos: Any, width: int, rows: int):
        self.color = color
        self.head = Cube(pos, width, rows)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.width = width
        self.rows = rows

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

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny)

    def reset(self, pos: Any) -> Any:
        """ reset method """
        self.head = Cube(pos, self.width, self.rows)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self) -> Any:
        """ addcube method """
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(
                Cube((tail.pos[0] - 1, tail.pos[1]), self.width, self.rows)
            )
        elif dx == -1 and dy == 0:
            self.body.append(
                Cube((tail.pos[0] + 1, tail.pos[1]), self.width, self.rows)
            )
        elif dx == 0 and dy == 1:
            self.body.append(
                Cube((tail.pos[0], tail.pos[1] - 1), self.width, self.rows)
            )
        elif dx == 0 and dy == -1:
            self.body.append(
                Cube((tail.pos[0], tail.pos[1] + 1), self.width, self.rows)
            )

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, win: Any) -> Any:
        """ draw method """
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(win, True)
            else:
                c.draw(win)


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


def redrawWindow(
    win: Any, height: int, width: int, rows: int, snake: Any, snack: Any
) -> Any:
    """ redrawWindow function """
    win.fill((0, 0, 0))
    drawGrid(height, width, rows, win)
    snake.draw(win)
    snack.draw(win)
    pygame.display.update()


def randomSnack(rows: Any, item: Any) -> Any:
    """ randomSnack function """
    positions = item.body

    while True:
        x = random.randrange(1, rows - 1)
        y = random.randrange(1, rows - 1)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def main() -> None:
    """ main function """
    width = 500
    height = 500
    rows = 20
    snake = Snake((255, 0, 0), (10, 10), width, rows)

    snake.addCube()
    snack = Cube(randomSnack(rows, snake), width, rows, color=(0, 255, 0))

    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake -- The Game")
    run = True
    clock = pygame.time.Clock()

    while run:
        pygame.time.delay(50)
        clock.tick(10)

        snake.move()
        headPos = snake.head.pos
        if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
            print("Score:", len(snake.body))
            snake.reset((10, 10))

        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(randomSnack(rows, snake), width, rows, color=(0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1 :])):  # type: ignore
                print("Score:", len(snake.body))
                snake.reset((10, 10))
                break

        redrawWindow(win, height, width, rows, snake, snack)


if __name__ == "__main__":
    main()
