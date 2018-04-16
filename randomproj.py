from random import *
gameBoardList =[[0,0,1,1], #init board values, assuming 4x3
               [2,2,3,3], #Set value to -1, if the image has been matched.
               [4,4,5,5]] 
def randomizeGameBoard():
  for x in range(3):
    for y in range(4):
      randX = randint(0,2)
      randY = randint(0,3)
      gameBoardList[x][y], gameBoardList[randX][randY]  = gameBoardList[randX][randY], gameBoardList[x][y]
  print gameBoardList
