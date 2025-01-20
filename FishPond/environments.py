import gc
from thumbySprite import Sprite
from thumbyGraphics import display
Number = int
import thumbyButton as buttons
import time

river_bg = None
lake_bg = None
ocean_sun = None
pond_bg = None
birds_sprite = None
lake_clouds = None
ocean_bg_1 = None
ocean_bg_2 = None
counter = None
secret_bg = None

def tutorial_screen():
  gc.collect()
  display.setFont("/lib/font5x7.bin", 5, 7, display.textSpaceWidth)
  display.drawText(str('How to Play'), 4, 1, 1)
  display.drawLine(0, 10, 72, 10, 1)
  display.drawText(str('Hold A &'), 4, 13, 1)
  display.drawText(str('release to'), 4, 22, 1)
  display.drawText(str('cast!'), 4, 31, 1)
  display.update()
  display.fill(0)
  while True:
    if buttons.inputJustPressed():
      break
  display.drawText(str('Catch Fish'), 4, 1, 1)
  display.drawLine(0, 10, 72, 10, 1)
  display.drawText(str('Press A'), 4, 13, 1)
  display.drawText(str('when !!!'), 4, 22, 1)
  display.drawText(str('appears'), 4, 31, 1)
  display.update()
  display.fill(0)
  while True:
    if buttons.inputJustPressed():
      break

ocean_sun = Sprite(1,1,bytearray([1]))

ocean_bg_1 = Sprite(1,1,bytearray([1]))

ocean_bg_2 = Sprite(1,1,bytearray([1]))

def ocean_screen():
  global ocean_sun, ocean_bg_1, ocean_bg_2, counter
  gc.collect()
  ocean_sun = Sprite(13,11,bytearray([0,16,1,186,68,130,130,130,68,186,1,16,0,0,0,1,0,0,0,2,0,0,0,1,0,0,16,16,0,186,68,130,130,130,68,186,0,16,16,0,0,0,0,0,0,6,0,0,0,0,0,0]),ocean_sun.x,ocean_sun.y,ocean_sun.key,ocean_sun.mirrorX,ocean_sun.mirrorY)
  ocean_bg_1 = Sprite(72,40,bytearray([192,192,192,192,192,192,128,0,0,16,12,10,10,9,4,4,132,68,36,24,8,140,82,173,173,178,124,228,90,90,37,89,129,129,1,1,2,4,8,16,32,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,2,2,0,0,0,0,0,0,128,64,160,32,112,216,172,86,171,85,255,0,0,0,0,1,226,21,13,53,194,1,0,0,0,0,1,6,253,1,2,4,8,16,32,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,12,12,12,12,12,12,12,12,4,4,1,129,65,113,105,87,171,213,106,213,170,84,168,211,126,3,1,6,24,48,64,254,1,1,1,1,1,1,6,248,0,0,128,120,7,1,1,1,1,1,133,133,129,129,1,1,1,1,1,17,17,17,33,33,33,1,113,137,137,137,113,1,129,129,65,65,33,33,81,225,65,1,174,85,170,85,170,84,170,84,170,84,169,85,169,255,0,0,0,0,4,4,132,130,130,130,130,130,128,128,128,143,132,131,128,128,64,64,33,33,33,33,16,16,16,16,17,17,16,32,32,32,32,32,0,16,8,8,20,20,255,34,45,49,0,8,8,4,4,4,4,4,4,4,6,5,2,3,2,5,10,13,26,21,26,13,10,15,13,9,9,1,1,1,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,96,112,240,64,0,0,0,0,2,0,0,0,0,32,0,0,0,0,0,128,254,1,142,240,0,0,0,0,0,0,64,1,0,0,0,192,192,192,192,192,192,128,0,0,16,12,10,10,9,4,4,132,68,36,24,8,140,82,173,173,178,124,228,90,90,37,89,129,129,1,1,2,4,8,16,32,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,2,2,0,0,0,0,0,0,128,64,160,32,112,216,172,86,171,85,255,0,0,0,0,1,226,21,13,53,194,1,0,0,0,0,1,6,253,1,2,4,8,16,32,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,12,12,12,12,12,12,12,12,4,4,1,129,65,113,105,87,171,213,106,213,170,84,168,211,126,3,1,6,24,48,64,254,1,1,1,1,1,1,6,248,0,0,128,120,7,1,1,1,5,5,9,9,9,1,1,1,1,1,1,33,33,33,65,65,65,1,113,137,137,137,113,1,129,129,65,65,33,33,81,225,65,1,174,85,170,85,170,84,170,84,170,84,169,85,169,255,0,0,0,0,8,8,8,4,4,4,4,4,0,0,0,15,4,3,0,0,0,128,130,66,66,66,65,33,33,33,34,34,34,32,64,64,64,64,64,80,72,72,84,20,255,34,45,49,0,32,16,16,8,8,8,8,8,8,6,5,2,3,2,5,10,13,26,21,26,13,10,15,14,10,10,2,2,2,2,1,1,1,1,1,1,17,1,1,1,1,1,1,1,0,0,96,112,240,64,0,0,0,0,2,0,0,0,0,32,0,0,0,0,0,128,254,1,142,240,0,0,0,0,0,0,64,1,0,0,0]),ocean_bg_1.x,ocean_bg_1.y,ocean_bg_1.key,ocean_bg_1.mirrorX,ocean_bg_1.mirrorY)
  ocean_bg_2 = Sprite(72,40,bytearray([192,192,192,192,192,192,128,0,0,16,12,10,10,9,4,4,132,68,36,24,8,140,82,173,173,178,124,228,90,90,37,89,129,129,1,1,2,4,8,16,32,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,2,2,0,0,0,0,0,0,128,64,160,32,112,216,172,86,171,85,255,0,0,0,0,1,226,21,13,53,194,1,0,0,0,0,1,6,253,1,2,4,8,16,32,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,12,12,12,12,12,12,12,12,4,4,1,129,65,113,105,87,171,213,106,213,170,84,168,211,126,3,1,6,24,48,64,254,1,1,1,1,1,1,6,248,0,0,128,120,7,1,1,9,9,9,17,17,17,17,9,9,1,1,1,65,65,65,129,129,129,1,113,137,137,137,113,1,129,129,65,65,33,33,81,225,65,1,174,85,170,85,170,84,170,84,170,84,169,85,169,255,0,0,0,0,16,16,16,8,8,8,8,8,0,0,0,15,4,3,0,0,0,0,0,4,4,4,4,2,2,130,130,132,132,132,132,128,128,128,128,144,136,136,148,20,255,34,173,177,128,128,64,64,64,64,64,64,64,64,6,5,2,3,2,5,10,13,26,21,26,13,10,15,12,12,12,4,4,4,4,4,4,4,4,4,4,20,4,4,4,4,2,2,2,2,2,98,114,242,66,1,1,0,0,2,0,0,0,0,32,0,0,0,0,0,128,254,1,142,240,0,0,0,0,0,0,64,1,0,0,0,192,192,192,192,192,192,128,0,0,16,12,10,10,9,4,4,132,68,36,24,8,140,82,173,173,178,124,228,90,90,37,89,129,129,1,1,2,4,8,16,32,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,2,2,0,0,0,0,0,0,128,64,160,32,112,216,172,86,171,85,255,0,0,0,0,1,226,21,13,53,194,1,0,0,0,0,1,6,253,1,2,4,8,16,32,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,12,12,12,12,12,12,12,12,4,4,1,129,65,113,105,87,171,213,106,213,170,84,168,211,126,3,1,6,24,48,64,254,1,1,1,1,1,1,6,248,0,0,128,120,7,1,1,17,17,17,33,33,33,33,17,17,1,1,1,129,129,129,1,1,1,1,113,137,137,137,113,1,129,129,65,65,33,33,81,225,65,1,174,85,170,85,170,84,170,84,170,84,169,85,169,255,0,0,0,0,0,32,32,32,16,16,16,16,16,0,0,15,4,3,0,0,0,0,0,8,8,8,8,4,4,4,4,8,8,8,8,8,8,0,1,17,9,8,20,20,255,34,45,49,0,0,0,0,128,128,128,128,128,128,6,5,2,3,2,5,10,13,26,21,26,29,26,63,60,60,56,56,112,112,96,96,96,96,96,96,96,96,96,96,96,96,48,48,48,48,48,112,112,240,112,48,48,48,48,24,24,24,24,12,44,12,12,12,12,4,128,254,1,142,240,2,6,6,3,3,1,65,1,1,1,1]),ocean_bg_2.x,ocean_bg_2.y,ocean_bg_2.key,ocean_bg_2.mirrorX,ocean_bg_2.mirrorY)
  ocean_sun.x = 47
  ocean_sun.key = 0
  counter = 1
  for count in range(int(display.frameRate * 5)):
    counter = (counter if isinstance(counter, Number) else 0) + 1
    if counter > display.frameRate * 0 and counter <= display.frameRate * 0.75:
      ocean_bg_1.setFrame(0)
      display.drawSprite(ocean_bg_1)
    elif counter > display.frameRate * 0.75 and counter <= display.frameRate * 1.5:
      ocean_bg_1.setFrame(1)
      display.drawSprite(ocean_bg_1)
    elif counter > display.frameRate * 1.5 and counter <= display.frameRate * 2.25:
      ocean_bg_2.setFrame(0)
      display.drawSprite(ocean_bg_2)
    elif counter > display.frameRate * 2.25 and counter <= display.frameRate * 3:
      ocean_bg_2.setFrame(1)
      display.drawSprite(ocean_bg_2)
    elif counter > display.frameRate * 3 and counter <= display.frameRate * 3.75:
      ocean_bg_2.setFrame(0)
      display.drawSprite(ocean_bg_2)
    elif counter > display.frameRate * 3.75 and counter <= display.frameRate * 4.5:
      ocean_bg_1.setFrame(1)
      display.drawSprite(ocean_bg_1)
    elif counter > display.frameRate * 4.5:
      ocean_bg_1.setFrame(0)
      display.drawSprite(ocean_bg_1)
    if counter % 8 == 0:
      ocean_sun.setFrame(ocean_sun.getFrame() + 1)
    display.drawSprite(ocean_sun)
    display.update()
    display.fill(0)
    if buttons.inputJustPressed():
      display.fill(0)
      display.update()
      break
  time.sleep(0.2)
  display.fill(0)
  display.update()
  gc.collect()

river_bg = Sprite(1,1,bytearray([1]))

birds_sprite = Sprite(1,1,bytearray([1]))

def river_screen():
  global river_bg, birds_sprite, counter
  gc.collect()
  river_bg = Sprite(72,40,bytearray([255,255,255,255,255,254,252,252,56,112,96,232,212,170,85,170,87,172,216,112,80,96,64,0,4,136,72,80,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,128,128,64,64,64,32,32,32,32,32,16,16,16,24,136,136,72,64,255,255,255,255,255,254,253,253,248,242,229,202,213,170,85,170,85,170,117,235,86,108,88,40,48,1,1,130,196,40,48,32,0,17,18,52,88,128,2,52,8,192,32,16,72,132,196,98,34,17,9,9,8,8,136,132,132,4,2,2,2,2,1,129,65,33,1,1,128,64,32,16,255,255,255,255,255,251,243,231,207,207,159,43,87,47,79,172,73,170,85,170,85,186,110,172,68,196,128,128,8,11,4,132,128,128,64,65,33,97,145,144,16,59,36,200,80,80,49,18,12,0,0,0,32,25,0,0,192,48,0,0,1,129,65,32,16,8,4,3,0,0,0,0,255,255,255,223,191,31,63,31,63,191,127,63,127,127,254,124,249,242,69,27,31,10,14,5,5,5,154,226,66,33,49,17,17,10,12,12,4,4,2,2,3,1,1,32,32,16,16,16,136,4,0,0,64,64,56,6,1,0,128,112,15,0,56,68,196,68,56,128,128,64,64,32,255,255,255,127,127,127,255,255,255,255,62,126,126,252,252,56,56,120,112,98,98,2,2,2,1,1,0,128,64,0,0,0,16,8,4,2,2,0,16,8,4,4,4,130,130,65,65,33,32,16,8,0,0,224,24,4,2,1,0,0,8,4,4,202,63,201,11,12,0,0,0,0,255,255,255,255,255,254,252,252,56,112,96,232,212,170,85,170,87,172,216,112,80,96,64,0,4,136,72,80,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,128,128,64,64,64,32,32,32,32,32,16,16,16,24,136,136,72,64,255,255,255,255,255,254,253,253,248,242,229,202,213,170,85,170,85,170,117,235,86,108,88,40,48,1,1,130,196,40,48,32,0,17,18,52,88,128,2,52,8,192,32,16,72,132,196,98,34,17,9,9,8,8,8,4,132,4,2,2,2,130,65,33,33,33,1,1,128,64,32,16,255,255,255,255,255,251,243,231,207,207,159,43,87,47,79,172,73,170,85,170,85,186,110,172,68,196,128,128,8,11,4,132,128,128,64,65,33,97,145,144,16,59,36,200,80,80,49,18,12,0,0,0,48,9,1,225,16,16,0,0,1,128,64,32,16,8,4,3,0,0,0,0,255,255,255,223,191,31,63,31,63,191,127,63,127,127,254,124,249,242,69,27,31,10,14,5,5,5,154,226,66,33,49,17,17,10,12,12,4,4,2,2,3,1,1,32,16,8,8,8,4,132,0,0,96,28,3,0,0,0,128,112,15,0,56,68,196,68,56,128,128,64,64,32,255,255,255,127,127,127,255,255,255,255,62,126,126,252,252,56,56,120,112,98,98,2,2,2,1,1,128,64,0,0,0,16,16,8,4,2,0,0,0,16,8,8,8,132,68,34,34,18,17,8,8,0,0,224,24,4,2,1,0,0,8,4,4,202,63,201,11,12,0,0,0,0]),river_bg.x,river_bg.y,river_bg.key,river_bg.mirrorX,river_bg.mirrorY)
  birds_sprite = Sprite(12,6,bytearray([8,16,32,16,8,0,0,4,2,4,2,4,32,16,32,16,32,0,0,1,2,4,2,1]),birds_sprite.x,birds_sprite.y,birds_sprite.key,birds_sprite.mirrorX,birds_sprite.mirrorY)
  birds_sprite.x = 37
  birds_sprite.key = 0
  for count2 in range(int(display.frameRate * 4)):
    counter = (counter if isinstance(counter, Number) else 0) + 1
    display.drawSprite(river_bg)
    display.drawSprite(birds_sprite)
    if counter % 10 == 0:
      river_bg.setFrame(river_bg.getFrame() + 1)
    if counter % 20 == 0:
      birds_sprite.x += -1
      birds_sprite.setFrame(birds_sprite.getFrame() + 1)
    display.update()
    display.fill(0)
    if buttons.inputJustPressed():
      display.fill(0)
      display.update()
      break
  time.sleep(0.2)
  gc.collect()

lake_bg = Sprite(1,1,bytearray([1]))

lake_clouds = Sprite(1,1,bytearray([1]))

def lake_screen():
  global lake_bg, lake_clouds, counter
  gc.collect()
  lake_bg = Sprite(72,40,bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,64,32,16,8,24,56,108,212,172,88,176,96,192,128,0,0,0,0,0,0,0,0,128,128,64,64,64,64,32,144,8,4,4,2,1,1,3,7,13,123,215,170,86,172,84,172,88,176,96,192,16,16,16,16,16,8,8,8,8,4,4,2,2,2,2,2,1,1,1,1,240,12,0,0,0,0,0,0,0,3,30,53,234,85,170,213,107,54,44,20,12,4,2,1,192,32,32,32,192,0,0,0,1,6,136,128,64,128,0,0,0,0,0,7,13,58,213,170,85,170,85,170,128,128,128,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,38,33,32,32,32,32,32,32,16,16,16,16,8,12,11,9,9,8,8,8,8,8,8,72,40,32,81,82,254,138,181,196,18,18,17,17,16,16,17,19,33,32,32,32,32,32,32,32,35,62,53,42,53,42,0,0,0,0,0,32,32,32,64,64,64,64,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,8,8,16,8,136,0,0,0,128,64,112,40,176,0,248,7,56,192,32,64,64,64,64,128,128,128,128,0,0,0,0,0,0,32,32,64,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,32,0,16,16,16,16,32,32,32,16,16,16,16,0,0,255,0,255,18,21,20,36,42,41,40,74,211,80,82,83,144,168,164,162,33,80,72,68,66,161,145,137,133,66,34,18,10,132,68,36,20,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,64,32,16,8,24,56,108,212,172,88,176,96,192,128,0,0,0,0,0,0,0,0,128,128,64,64,64,64,32,144,8,4,4,2,1,1,3,7,13,123,215,170,86,172,84,172,88,176,96,192,16,16,16,16,16,8,8,8,8,4,4,2,2,2,2,2,1,1,1,1,240,12,0,0,0,0,0,0,0,3,30,53,234,85,170,213,107,54,44,20,12,4,2,1,192,32,32,32,192,0,0,0,1,6,136,128,64,128,0,0,0,0,0,7,13,58,213,170,85,170,85,170,128,128,128,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,38,33,32,32,32,32,32,32,16,16,16,16,8,12,11,9,9,8,8,8,8,8,8,72,40,32,81,82,254,138,181,196,18,18,17,17,16,16,17,19,33,32,32,32,32,32,32,32,35,62,53,42,53,42,0,0,0,0,0,64,64,64,32,32,32,32,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,16,16,16,8,136,0,0,0,128,64,112,40,176,0,248,7,56,192,32,64,64,64,64,128,128,128,128,0,0,0,0,0,0,64,64,32,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,32,32,32,32,16,16,16,32,32,32,32,0,0,255,0,255,18,21,20,36,42,41,40,74,211,80,82,83,144,168,164,162,33,80,72,68,66,161,145,137,133,66,34,18,10,132,68,36,20,8,8]),lake_bg.x,lake_bg.y,lake_bg.key,lake_bg.mirrorX,lake_bg.mirrorY)
  lake_clouds = Sprite(45,7,bytearray([127,127,127,127,127,127,63,63,63,62,62,58,56,56,56,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,12,12,12,4,4]), lake_clouds.x,lake_clouds.y,lake_clouds.key,lake_clouds.mirrorX,lake_clouds.mirrorY)
  lake_clouds.x = -5
  lake_clouds.key = 0
  for count3 in range(int(display.frameRate * 4)):
    counter = (counter if isinstance(counter, Number) else 0) + 1
    display.drawSprite(lake_bg)
    display.drawSprite(lake_clouds)
    if counter % 15 == 0:
      lake_bg.setFrame(lake_bg.getFrame() + 1)
    if counter % 26 == 0:
      lake_clouds.x += 1
      birds_sprite.setFrame(birds_sprite.getFrame() + 1)
    display.update()
    display.fill(0)
    if buttons.inputJustPressed():
      display.fill(0)
      display.update()
      break
  time.sleep(0.2)
  gc.collect()

pond_bg = Sprite(1,1,bytearray([1]))

def pond_screen():
  global pond_bg, birds_sprite, counter
  gc.collect()
  pond_bg = Sprite(72,40,bytearray([4,4,4,4,6,6,6,6,6,6,6,6,6,2,2,130,130,128,128,128,128,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,12,236,204,12,12,4,4,4,4,4,128,192,192,64,0,0,0,0,0,0,0,80,176,80,176,80,176,216,168,216,168,84,106,86,107,85,106,85,106,85,106,85,106,85,170,214,172,216,172,220,180,116,108,86,106,54,42,54,42,54,42,85,107,213,170,212,160,71,142,28,96,138,0,255,195,112,216,100,16,136,68,162,81,169,84,172,88,168,88,176,80,160,64,1,65,225,81,33,33,65,64,128,128,0,112,136,136,136,112,0,128,128,128,128,128,128,128,128,192,64,64,68,68,88,113,62,56,44,32,32,32,32,32,32,32,32,32,32,33,33,33,33,32,39,28,31,31,19,17,32,33,33,33,33,33,33,33,33,33,33,65,65,65,65,65,0,0,224,24,4,2,2,0,0,0,49,45,34,255,20,20,8,8,16,0,64,64,32,32,0,0,96,144,144,8,8,200,104,136,8,8,8,144,144,96,0,2,2,2,1,1,1,2,2,2,0,0,0,8,20,18,18,73,105,89,73,65,65,65,65,34,34,20,8,0,0,0,0,0,0,1,1,2,2,2,2,2,0,240,142,1,254,128,4,4,4,4,4,4,8,8,8,8,8,8,8,9,9,9,8,13,25,41,125,18,16,16,16,16,16,16,17,49,33,33,33,34,34,34,32,42,40,48,66,252,64,32,48,40,40,36,32,32,34,16,18,18,16,16,4,4,4,4,6,6,6,6,6,6,6,6,6,2,2,130,130,128,128,128,128,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,12,236,204,12,12,4,4,4,4,4,128,192,192,64,0,0,0,0,0,0,0,80,176,80,176,80,176,216,168,216,168,84,106,86,107,85,106,85,106,85,106,85,106,85,170,214,172,216,172,220,180,116,108,86,106,54,42,54,42,54,42,85,107,213,170,212,160,71,142,28,96,138,0,255,195,112,216,100,16,136,68,162,81,169,84,172,88,168,88,176,80,160,64,1,65,225,81,33,33,65,64,128,128,0,112,136,136,136,112,0,128,128,128,128,128,128,128,128,192,64,64,68,68,88,113,62,56,44,32,32,32,32,32,32,32,32,32,32,33,33,33,33,32,39,28,31,31,19,17,32,33,33,33,33,33,33,33,33,33,33,65,65,65,65,65,0,0,224,24,4,2,2,0,0,0,49,45,34,255,20,20,8,8,16,0,32,32,64,64,0,0,96,144,144,8,8,200,104,136,8,8,8,144,144,96,0,1,1,1,2,2,2,1,1,129,128,128,0,136,20,18,18,73,105,89,73,65,65,65,65,34,34,20,8,0,0,0,0,0,0,1,1,2,2,2,2,2,0,240,142,1,254,128,4,4,4,4,4,4,8,8,8,8,8,8,8,9,9,9,8,13,25,41,125,18,16,16,16,16,16,16,17,49,33,33,33,32,32,32,32,40,40,48,66,252,64,32,48,40,40,36,32,32,33,16,17,17,16,16]),pond_bg.x,pond_bg.y,pond_bg.key,pond_bg.mirrorX,pond_bg.mirrorY)
  birds_sprite = Sprite(12,6,bytearray([8,16,32,16,8,0,0,4,2,4,2,4,32,16,32,16,32,0,0,1,2,4,2,1]),birds_sprite.x,birds_sprite.y,birds_sprite.key,birds_sprite.mirrorX,birds_sprite.mirrorY)
  birds_sprite.x = 30
  birds_sprite.key = 0
  for count4 in range(int(display.frameRate * 4)):
    counter = (counter if isinstance(counter, Number) else 0) + 1
    display.drawSprite(pond_bg)
    display.drawSprite(birds_sprite)
    if counter % 10 == 0:
      pond_bg.setFrame(pond_bg.getFrame() + 1)
    if counter % 20 == 0:
      birds_sprite.x += -1
      birds_sprite.setFrame(birds_sprite.getFrame() + 1)
    display.update()
    display.fill(0)
    if buttons.inputJustPressed():
      display.fill(0)
      display.update()
      break
  time.sleep(0.2)
  gc.collect()
  
secret_bg = Sprite(1,1,bytearray([1]))

def secret_screen():
  global secret_bg, counter
  secret_bg = Sprite(72,40,bytearray([0,0,0,0,0,0,0,0,128,128,0,0,0,128,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,64,224,32,16,8,248,4,4,244,138,242,2,2,250,2,2,242,138,244,4,244,136,248,16,224,160,192,128,0,0,0,0,0,0,0,0,0,0,0,0,1,0,44,3,0,1,0,44,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,224,24,188,3,0,60,162,60,0,0,190,0,0,60,162,60,0,0,190,0,0,60,162,60,0,0,190,0,0,0,190,0,0,63,164,56,224,0,0,0,16,56,20,8,8,16,16,32,32,64,92,162,226,34,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,207,40,207,0,192,47,192,0,15,232,15,0,15,232,15,0,192,47,192,0,0,239,0,0,192,47,192,0,192,47,192,0,15,232,15,0,255,0,0,0,0,0,0,0,0,0,0,0,12,11,136,127,133,5,2,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,14,51,74,243,0,3,250,3,0,240,139,240,0,240,139,240,0,243,138,243,0,240,139,240,0,243,138,243,0,243,138,243,0,128,123,48,14,1,0,0,0,0,0,0,0,0,0,0,0,0,60,35,0,63,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,4,14,8,16,32,62,64,64,64,190,128,128,128,190,128,128,188,162,124,64,64,62,32,16,8,14,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,128,128,0,0,0,128,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,192,160,224,16,248,136,244,4,244,138,242,2,2,250,2,2,2,250,4,4,244,136,248,16,32,224,64,128,0,0,0,0,0,0,0,0,0,0,0,0,1,0,44,3,0,1,0,44,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,224,24,188,3,0,60,162,60,0,0,190,0,0,0,190,0,0,60,162,60,0,0,190,0,0,0,190,0,0,60,162,60,0,3,188,24,224,0,0,0,16,56,20,8,8,16,16,32,32,64,92,162,226,34,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,192,47,192,0,0,239,0,0,192,47,192,0,192,47,192,0,15,232,15,0,207,40,207,0,0,239,0,0,15,232,15,0,15,232,15,0,255,0,0,0,0,0,0,0,0,0,0,0,12,11,136,127,133,5,2,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,14,51,74,243,0,240,139,240,0,243,138,243,0,243,138,243,0,0,251,0,0,3,250,3,0,240,139,240,0,240,139,240,0,240,75,48,14,1,0,0,0,0,0,0,0,0,0,0,0,0,60,35,0,63,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,4,10,12,16,32,62,64,64,64,190,128,128,188,162,188,128,128,190,64,64,64,62,32,16,8,14,4,2,1,0,0,0,0]),secret_bg.x,secret_bg.y,secret_bg.key,secret_bg.mirrorX,secret_bg.mirrorY)
  counter = 1
  for count in range(int(display.frameRate * 4)):
    counter = (counter if isinstance(counter, Number) else 0) + 1
    if counter % 10 == 0:
      secret_bg.setFrame(secret_bg.getFrame() + 1)
    display.drawSprite(secret_bg)
    display.update()
    display.fill(0)
    if buttons.inputJustPressed():
      display.fill(0)
      display.update()
      break