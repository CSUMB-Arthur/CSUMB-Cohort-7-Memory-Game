import random
import java.awt.Font as Font
#import java.awt.FontMetrics
#http://www.java2s.com/Tutorial/Java/0261__2D-Graphics/Centertext.htm
#Drawing centered text, should figure this out someday
class Coords:
  def __init__(self,i):
    self.x = i%cols
    self.y = i//cols
#blah blah blah, testing
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
backgroundColor = makeColor(31,31,31)
boardImage = makeEmptyPicture(800,600)
board =  [[0,0,1,1],
          [2,2,3,3],
          [4,4,5,5]]
imageFolder = r"F:\Users\Fireplace\Desktop\Not Hacks\csumb\Week014\MemoryGameImages"
images = []
maxint = 5
validIndexes = []
print("Resizing images in folder.")
for i in range(0,6):
  validIndexes.append(i)
for i in range(0,6):
  ri = random.randint(0,maxint)
  resized = makePicture(imageFolder+"\\%02d.png"%validIndexes[ri])
  validIndexes[ri] = validIndexes[maxint]
  ratio = cardWidth/float(getWidth(resized)) #Percent required to match width
  if ratio > cardHeight/float(getHeight(resized)):
    ratio = cardHeight/float(getHeight(resized)) #Percent required to match height
  #Rescale by the smaller ratio, to ensure the new image fits into the card area, even if it isn't square
  resized = scalePercent(resized,ratio*100)
  images.append(resized)
  maxint -= 1
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
    clearCardAtCoord(c1)
    clearCardAtCoord(c2)
    matchesMade +=1
    if matchesMade >=6:
      showInformation("You win!")
      break
  else:
    hideCardAtCoord(c1)
    hideCardAtCoord(c2)
    wrongTurns += 1
    showInformation("No match! %d/6 wrong moves"%wrongTurns)
    if wrongTurns >= 6:
      showInformation("You lose!")
      break
  repaint(boardImage)
