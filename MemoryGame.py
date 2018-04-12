import random
import java.awt.Font as Font
import os
#import java.awt.FontMetrics
#http://www.java2s.com/Tutorial/Java/0261__2D-Graphics/Centertext.htm
#Drawing centered text, should figure this out someday
class Coords:
  def __init__(self,i):
    self.x = i%cols
    self.y = i//cols

#Takes the list of coordinates [x, y] as an input
def clearCardAtCoord(c, image):
  startX = (c[0] + 1)*margins  + (c[0] * cardWidth)
  startY = (c[1] + 1)*margins  + (c[1] * cardHeight)
  for i in range(cardWidth):
    for j in range(cardHeight):
      pixel = getPixel(image, cardWidth + i, cardHeight + j)
      setColor(pixel, backgroundColor)
      return image

def hideCardAtCoord(c, image, back):
  startX = (c[0] + 1)*margins  + (c[0] * cardWidth)
  startY = (c[1] + 1)*margins  + (c[1] * cardHeight)
  for i in range(cardWidth):
    for j in range(cardHeight):  
      pixel = getPixel(image, startX + i, startY + j)
#*****This code will be implemented once I create an image for back of card
#     backPixel = getPixel(cardBack, i, j)
#     color = getcolor
#     setColor(pixel, color)
      setColor(pixel, cardBackColor)   
      return image
  
def scalePercent(pic,percent):
  percent = percent*0.01
  w1 = getWidth(pic)
  h1 = getHeight(pic)
  w2 = int(getWidth(pic)*percent)
  h2 = int(getHeight(pic)*percent)
  newpic = makeEmptyPicture(w2, h2)
  for y in range(0,h2):
    for x in range(0,w2):
      drawn = getPixel(newpic,x,y)
      sampled = getPixel(pic,int(x/percent),int(y/percent))
      setColor(drawn,getColor(sampled))
  return newpic

boardWidth = 800
boardHeight = 600
cols = 4
rows = 3
margins = 5
cardWidth = (boardWidth-margins*(cols+1))/cols
cardHeight = (boardHeight-margins*(rows+1))/rows
cardBackColor = makeColor(127,127,127)
#cardBack = makePicture("C:\******\cardReverse.jpg") once a make a card back image
#cardBack = scalePercent
backgroundColor = makeColor(31,31,31)
boardImage = makeEmptyPicture(800,600)
board =  [[0,0,1,1],
          [2,2,3,3],
          [4,4,5,5]]
imageFolder = os.path.dirname(os.path.abspath(__file__))+r"\MemoryGameImages"
imagePaths = os.listdir(imageFolder)#Returns a list of all the file paths of the folder. As a unicode string.
images = []
maxInt = len(imagePaths)-1
validIndexes = []
print("Resizing images in folder.")

for i in range(0,6): #Resize 6 base images from the folder, and append the resized version to images[]
  ri = random.randint(0,maxInt)
  resized = makePicture(imageFolder+"\\"+imagePaths[ri])
  imagePaths[ri] = imagePaths[maxInt]
  ratio = cardWidth/float(getWidth(resized)) #Percent required to match width
  if ratio > cardHeight/float(getHeight(resized)):
    ratio = cardHeight/float(getHeight(resized)) #Percent required to match height
  #Rescale by the smaller ratio, to ensure the new image fits into the card area, even if it isn't square
  resized = scalePercent(resized,ratio*100)
  images.append(resized)
  maxInt -= 1
randomizeBoard()
hideAllCards()
show(boardImage)
print board
wrongTurns = 0
matchesMade = 0
while true:
  guessOne = -1 #Reset guessOne, this variable is used in the getInput function, so you can't pick the same card twice.
  i1 = getInput()
  c1 = intToCoord(i1)
  showCardAtCoord(c1)
  repaint(boardImage)
  guessOne = i1

  i2 = getInput()
  c2 = intToCoord(i2)
  showCardAtCoord(c2)
  repaint(boardImage)

  if board[c1.y][c1.x] == board[c2.y][c2.x]:
    board[c1.y][c1.x] = -1
    board[c2.y][c2.x] = -1
    showInformation("Match!")
    boardImage = clearCardAtCoord(c1, boardImage) #I added a boardImage Parameter. Not sure how this would be done without. Maybe I am missing something? - WB
    boardImage = clearCardAtCoord(c2, boardImage)
    matchesMade +=1
    if matchesMade >=6:
      showInformation("You win!")
      break
  else:
    wrongTurns += 1
    showInformation("No match! %d/6 wrong moves"%wrongTurns)
    boardImage = hideCardAtCoord(c1, boardImage)
    boardImage = hideCardAtCoord(c2, boardImage)
    if wrongTurns >= 6:
      showInformation("You lose!")
      break
  repaint(boardImage)
