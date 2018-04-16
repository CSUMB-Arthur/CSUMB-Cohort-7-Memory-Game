def getInput():
  x = int(raw_input('Pick from the 12 boxes numbered 1 to 11: '))    
  while x not in range(0,12,1): 
    x = int(raw_input('That entry is not valid, choose an available box: '))
  return x