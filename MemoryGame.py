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
def clearCardAtCoord(x, y, image, backgroundColor):
  startX = (x + 1)*margins  + (x * cardWidth)
  startY = (y + 1)*margins  + (y * cardHeight)
  for i in range(cardWidth):
    for j in range(cardHeight):
      pixel = getPixel(image, startX + i, startY + j)
      setColor(pixel, backgroundColor)
  return image

def hideCardAtCoord(x, y, image, cardBackColor):
  startX = (x + 1)*margins  + (x * cardWidth)
  startY = (y + 1)*margins  + (y * cardHeight)
  for i in range(cardWidth):
    for j in range(cardHeight):  
      pixel = getPixel(image, startX + i, startY + j)
#*****This code will be implemented once I create an image for back of card
#     backPixel = getPixel(cardBack, i, j)
#     color = getcolor
#     setColor(pixel, color)
      setColor(pixel, black)#cardBackColor)  
  return image
  #Draws/shows card at the given location
  
#Adds/draws image at the given location
def showImageAtCoord(x, y, gameBoardList, gameBoard):
  print x
  print y
  print gameBoardList
  print images[4]
  image = images[gameBoardList[y][x]] # gets one image from the cards/images list
  width = getWidth(image) #gets width of a single card
  height = getHeight(image)#gets height of a single care
  for m in range(width):
    for n in range (height):
      pixel = getPixel(image, m,n)
      color = getColor(pixel) 
      newPixel = getPixel(gameBoard, (width*x)+(margins*(x+1))+m , (height*y)+(margins*(y+1))+n ) 
      setColor(newPixel, color)
  return gameBoard

  
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
#Initilly shows the board with all flipped back cards
def initializeBoardImage():
  backImage =  makePicture(path+"\\back.jpg") # gets one image from the cards/images list
  ratio = cardWidth/float(getWidth(backImage)) #Percent required to match width
  if ratio > cardHeight/float(getHeight(backImage)):
    ratio = cardHeight/float(getHeight(backImage)) #Percent required to match height
  #Rescale by the smaller ratio, to ensure the new image fits into the card area, even if it isn't square
  backImage = scalePercent(backImage,ratio*100)
  width = getWidth(backImage) #gets width of a single card
  height = getHeight(backImage)#gets height of a single card
  for i in range(12):
    cd = intToCoord(i)
    x = cd.x
    y = cd.y
    for m in range(width):
      for n in range (height):
        pixel = getPixel(backImage, m,n)
        color = getColor(pixel) 
        newPixel = getPixel(boardImage, (width*x)+(margins*(x+1))+m , (height*y)+(margins*(y+1))+n ) 
        setColor(newPixel, color)
  show(boardImage)

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
backgroundColor = white # makeColor(31,31,31)
boardImage = makeEmptyPicture(800,600)
board =  [[0,0,1,1],
          [2,2,3,3],
          [4,4,5,5]]
imageFolder = os.path.dirname(os.path.abspath(__file__))+r"\MemoryGameImages"
print(imageFolder)
imagePaths = os.listdir(imageFolder)#Returns a list of all the file paths of the folder. As a unicode string.
print(imagePaths)
print(imagePaths)
images = []
maxInt = int(len(imagePaths))-1
print(maxInt)
validIndexes = []
print("Resizing images in folder.")

for i in range(0,6): #Resize 6 base images from the folder, and append the resized version to images[]
  ri = i# = random.randint(0,maxInt)
  resized = makePicture(imageFolder+"\\"+imagePaths[ri])
  imagePaths[ri] = imagePaths[maxInt]
  ratio = cardWidth/float(getWidth(resized)) #Percent required to match width
  if ratio > cardHeight/float(getHeight(resized)):
    ratio = cardHeight/float(getHeight(resized)) #Percent required to match height
  #Rescale by the smaller ratio, to ensure the new image fits into the card area, even if it isn't square
  resized = scalePercent(resized,ratio*100)
  images.append(resized)
  maxInt -= 1
#randomizeBoard()
#board = [[0,0,1,1], 
#         [2,2,3,3], 
#         [4,4,5,5]]

def intToCoord(i):
  coord = Coords(i)
  return coord
  
def hideAllCards(board, boardImage, backCardColor):
  numberOfCards = len(board) * len(board[0])
  for i in range(numberOfCards):
    c = Coords(i)
    boardImage = hideCardAtCoord(c.x, c.y, boardImage, backCardColor)
    
  return boardImage
    
def getInput():
  x = input("Guess 1 - 9")
  return x
    

boardImage = hideAllCards(board, boardImage, cardBackColor)
   
show(boardImage)
print board
wrongTurns = 0
matchesMade = 0
while true:
  guessOne = -1 #Reset guessOne, this variable is used in the getInput function, so you can't pick the same card twice.
  i1 = getInput()
  c1 = Coords(i1)
  print(c1.x)
  showImageAtCoord(c1.x, c1.y, board, boardImage)
  repaint(boardImage)
  guessOne = i1

  i2 = getInput()
  c2 = Coords(i2)
  boardImage = showImageAtCoord(c2.x, c2.y, board, boardImage)
  repaint(boardImage)

  if board[c1.y][c1.x] == board[c2.y][c2.x]:
    showInformation("Match!")
    print(c1.x)
    boardImage = clearCardAtCoord(c1.x, c1.y, boardImage, backgroundColor) #I added a boardImage Parameter. Not sure how this would be done without. Maybe I am missing something? - WB
    boardImage = clearCardAtCoord(c2.x, c2.y, boardImage, backgroundColor)  
    board[c1.y][c1.x] = -1
    board[c2.y][c2.x] = -1  
    matchesMade +=1

    repaint(boardImage)
    if matchesMade >=6:
      showInformation("You win!")
      break
  else:
    wrongTurns += 1
    showInformation("No match! %d/6 wrong moves"%wrongTurns)
    boardImage = hideCardAtCoord(c1.x, c1.y, boardImage, cardBackColor)
    boardImage = hideCardAtCoord(c2.x, c2.y, boardImage, cardBackColor)
    print("before repaint")
    repaint(boardImage)
    
    if wrongTurns >= 6:
      showInformation("You lose!")
      break
    
