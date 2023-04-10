
```python
import pygame
import random

pygame.init()

size = (7, 7)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("go")

pieces = ["X", "O"]

player1 = 1
player2 = 2

player1pieces = [[random.randint(0, 6) for i in range(size[0])] for j in range(size[1])]
player2pieces = [[random.randint(0, 6) for i in range(size[0])] for j in range(size[1])]

random_num = random.Random()

定义棋子移动函数
def movepiece(x, y, newx, newy):
global player1pieces, player2pieces
if x < 0 or x >= size[0] or y < 0 or y >= size[1]:
return False
if player1pieces[x][y]!= " ":
player1pieces[x][y] = " "
player1pieces[newx][y] = pieces[player1]
return True
if player2pieces[x][y]!= " ":
player2pieces[x][y] = " "
player2pieces[new_x][y] = pieces[player2]