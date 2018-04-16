from random import *
gameBoardList =[[0,0,1,1], #init board values, assuming 4x3
               [2,2,3,3], #Set value to -1, if the image has been matched.
               [4,4,5,5]] 
def welcome():
  showInformation("Welcome to Team 2's Memory Game" )
  print("As the player, you flip two cards by entering the numbers on the cards")
  print("If the cards match, they are removed and the player scores one point.")
  print("If they do not match, they are flipped over and the player gets one missed attempt. ")
  print("The game is over when you fail to match cards 6 times. If all the cards are matched, you win the game. Good luck!")
  
def randomizeGameBoard():
  for x in range(3):
    for y in range(4):
      randX = randint(0,2)
      randY = randint(0,3)
      gameBoardList[x][y], gameBoardList[randX][randY]  = gameBoardList[randX][randY], gameBoardList[x][y]
  return gameBoardList
