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
    self.up = 0 # Initially card facedown 0 for facedown, 1 for face up, -1 for clear
  
#Adds/draws image at the given location
def showCardAtCoord(cd, boardImage):
  x = cd.x
  y = cd.y
  if cd.up == 0:
    image = backImages[backboard[y][x]]
  elif cd.up == -1:
    image = clearImage
  elif cd.up ==1:
    image = images[board[y][x]] # gets one image from the cards/images list
  width = getWidth(image) #gets width of a single card
  height = getHeight(image)#gets height of a single care
  for m in range(width):
    for n in range (height):
      pixel = getPixel(image, m,n)
      color = getColor(pixel) 
      newPixel = getPixel(boardImage, (width*x)+(margins*(x+1))+m , (height*y)+(margins*(y+1))+n ) 
      setColor(newPixel, color)
  repaint (boardImage)
  return boardImage

  
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

#Plays a sound according to the event happening i.e. winning, losing, match or wrong
def playSound(num): #num corresponds to the sound we want to play. It is the key which corresponds to a sound in the dictionary SoundDict
  soundFolder = os.path.dirname(os.path.abspath(__file__))+r"\MemoryGameSounds"
  win = makeSound(soundFolder+"\\win.wav")
  lose = makeSound(soundFolder + "\\lose.wav")
  match = makeSound(soundFolder+ "\\match.wav")
  wrong = makeSound (soundFolder + "\\boing.wav")
  soundDict = {1:win, 2:lose, 3:match, 4:wrong}
  play(soundDict[num])
  
def initializeBoardImage(boardImage):
  for i in range(12):
    cd = intToCoord(i)
    x = cd.x
    y = cd.y
    cd.up = 0
    boardImage = showCardAtCoord(cd, boardImage)
  return boardImage
    
def intToCoord(i):
  coord = Coords(i)
  return coord
    
def getInput():
  x = int(requestString("Enter the number of image you want to turn up. 0-11"))
  return x
boardWidth = 800
boardHeight = 600
cols = 4
rows = 3
margins = 5
cardWidth = (boardWidth-margins*(cols+1))/cols
cardHeight = (boardHeight-margins*(rows+1))/rows
boardImage = makeEmptyPicture(800,600,blue)
backboard =[[0,1,2,3],
           [4,5,6,7],
           [8,9,10,11]]
board =  [[0,0,1,1],
          [2,2,3,3],
          [4,4,5,5]]
imageFolder = os.path.dirname(os.path.abspath(__file__))+r"\MemoryGameImages"
imagePaths = os.listdir(imageFolder)#Returns a list of all the file paths of the folder. As a unicode string.
images = []
maxInt = len(imagePaths)-1
validIndexes = []
print("Resizing images in folder.")

images = []
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

backImageFolder = os.path.dirname(os.path.abspath(__file__))+r"\MemoryGameBackImages"
backImagesPath= os.listdir(backImageFolder)
backImages= []
for i in range(len(backImagesPath)):
  backImage = makePicture(backImageFolder+"\\"+backImagesPath[i])
  ratio = cardWidth/float(getWidth(backImage)) #Percent required to match width
  if ratio > cardHeight/float(getHeight(backImage)):
    ratio = cardHeight/float(getHeight(backImage)) #Percent required to match height
  #Rescale by the smaller ratio, to ensure the new image fits into the card area, even if it isn't square
  backImages.append(scalePercent(backImage,ratio*100))
 
clearImage = makePicture(path+"\\clearImage.png")
ratio = cardWidth/float(getWidth(clearImage)) #Percent required to match width
if ratio > cardHeight/float(getHeight(clearImage)):
  ratio = cardHeight/float(getHeight(clearImage)) #Percent required to match height
  #Rescale by the smaller ratio, to ensure the new image fits into the card area, even if it isn't square
clearImage = scalePercent(clearImage,ratio*100)
 
boardImage = initializeBoardImage(boardImage)
wrongTurns = 0
matchesMade = 0
while true:
  #guessOne = -1 #Reset guessOne, this variable is used in the getInput function, so you can't pick the same card twice.
  i1 = getInput()
  c1 = intToCoord(i1)
  while (board[c1.y][c1.x]== -1):
    print "You have already matched that card. Please pick another card"
    i1 = getInput()
    c1 = intToCoord(i1)    
  c1.up =1 #Show card faceup
  print i1, c1.x, c1.y
  boardImage = showCardAtCoord(c1, boardImage)
  repaint(boardImage)

  i2 = getInput()
  c2 = intToCoord(i2)
  while (board[c2.y][c2.x]== -1) or (i1 == i2):
    print "You have already matched/picked that card. Please pick another card"
    i2 = getInput()  
    c2 = intToCoord(i2)  
  c2.up =1 #show card faceup
  boardImage=showCardAtCoord(c2,boardImage)
  repaint(boardImage)

  if board[c1.y][c1.x] == board[c2.y][c2.x]:
    board[c1.y][c1.x] = -1
    board[c2.y][c2.x] = -1
    playSound(3) #plays the sound for key 3 in soundDict
    showInformation("Match!")
    c1.up = -1
    c2.up = -1
    boardImage = showCardAtCoord(c1, boardImage)
    boardImage = showCardAtCoord(c2, boardImage)
    matchesMade +=1
    if matchesMade >=6:
      playSound(1)
      showInformation("You win!")
       #plays the sound for key 1 in soundDict
      break
  else:
    wrongTurns += 1
    playSound(4) #plays sound for key 4 in soundDict
    c1.up = 0
    boardImage = showCardAtCoord(c1, boardImage)
    c2.up = 0
    boardImage = showCardAtCoord(c2, boardImage)
    showInformation("No match! %d/6 wrong moves"%wrongTurns)
    if wrongTurns >= 6:
      playSound(2) #plays sound for key 2
      showInformation("You lose!")
      break
  repaint(boardImage)
