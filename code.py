import board
import terminalio
import displayio
import math
import time
import rtc
from adafruit_st7789 import ST7789
import network

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.IO13
tft_dc = board.IO14

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.IO15)
display = ST7789(display_bus, width=320, height=240, rotation=90)

mynet = network.Network()
mynet.syncRTC_time()

# Open the files
# Setup the file as the bitmap data source
zero = open("/zero.bmp", "rb")
one = open("/one.bmp", "rb")
two = open("/two.bmp", "rb")
three = open("/three.bmp", "rb")
four = open("/four.bmp", "rb")
five = open("/five.bmp", "rb")
six = open("/six.bmp", "rb")
seven = open("/seven.bmp", "rb")
eight = open("/eight.bmp", "rb")
nine = open("/nine.bmp", "rb")


class numbers:	
    def __init__(self, val, name):
        self.fname = name
        self.width = val
        self.file = displayio.OnDiskBitmap(name)
        
    def get_name(self):
        return self.fname	
    
    def get_width(self):
        return self.width
        
    def get_file(self):
        return self.file
        

def pickSprite(num, dig, width):
    sprite = displayio.TileGrid(num, pixel_shader=displayio.ColorConverter(),
    width = 1,
    height = 1,
    tile_width = width,
    tile_height = 224,
    default_tile = 0,x=dig, y=0)
    return sprite
    

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(int(n * multiplier) / multiplier)
    

    
zero = numbers(157, zero)
one = numbers(150, one)
two = numbers(155, two)
three = numbers(158, three)
four = numbers(152, four)
five = numbers(153, five)
six = numbers(156, six)
seven = numbers(160, seven)
eight = numbers(160, eight)
nine = numbers(148, nine)


boardRTC = rtc.RTC()

#  Main Loop
while True:
    display.refresh()
    clockTime = boardRTC.datetime
    
    fdig = clockTime.tm_min % 10
    sdig = truncate(clockTime.tm_min / 10)


    # Create a Group to hold the TileGrid
    group = displayio.Group()
    
    if fdig == 0:
        group.append(pickSprite(zero.get_file(), 160, zero.get_width()))
        
    if fdig == 1:
        group.append(pickSprite(one.get_file(), 160, one.get_width()))
        
    if fdig == 2:
        group.append(pickSprite(two.get_file(), 160, two.get_width()))
        
    if fdig == 3:
        group.append(pickSprite(three.get_file(), 160, three.get_width()))
        
    if fdig == 4:
        group.append(pickSprite(four.get_file(), 160, four.get_width()))

    if fdig == 5:
        group.append(pickSprite(five.get_file(), 160, five.get_width()))
        
    if fdig == 6:
        group.append(pickSprite(six.get_file(), 160, six.get_width()))
        
    if fdig == 7:
        group.append(pickSprite(seven.get_file(), 160, seven.get_width()))
        
    if fdig == 8:
        group.append(pickSprite(eight.get_file(), 160, eight.get_width()))
        
    if fdig == 9:
        group.append(pickSprite(nine.get_file(), 160, nine.get_width()))
        
        
    if sdig == 0:
        group.append(pickSprite(zero.get_file(), 0, zero.get_width()))
        
    if sdig == 1:
        group.append(pickSprite(one.get_file(), 0, one.get_width()))
        
    if sdig == 2:
        group.append(pickSprite(two.get_file(), 0, two.get_width()))
        
    if sdig == 3:
        group.append(pickSprite(three.get_file(), 0, three.get_width()))
        
    if sdig == 4:
        group.append(pickSprite(four.get_file(), 0, four.get_width()))

    if sdig == 5:
        group.append(pickSprite(five.get_file(), 0, five.get_width()))
        
    if sdig == 6:
        group.append(pickSprite(six.get_file(), 0, six.get_width()))
        
    if sdig == 7:
        group.append(pickSprite(seven.get_file(), 0, seven.get_width()))
        
    if sdig == 8:
        group.append(pickSprite(eight.get_file(), 0, eight.get_width()))
        
    if sdig == 9:
        group.append(pickSprite(nine.get_file(), 0, nine.get_width()))

    # Add the Group to the Display
    display.show(group)

    
   
