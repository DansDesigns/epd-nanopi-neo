# /*****************************************************************************
# * | File        :	  EPD_1in54.py
# * | Author      :   Waveshare team
# * | Function    :   Hardware underlying interface
# * | Info        :
# *----------------
# * |	This version:   V2.0
# * | Date        :   2018-11-01
# * | Info        :   
# * 1.Remove:
#   digital_write(self, pin, value)
#   digital_read(self, pin)
#   delay_ms(self, delaytime)
# ******************************************************************************/
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


import spidev
#from smbus2 import SMBus
import time
import OPi.GPIO as GPIO #replaces RPi.GPIO
from OPi.pin_mappings import sunxi

# assert sunxi("PA06") == 6    # SPI-0 OLED RST
# assert sunxi("PC00") == 64   # SPI-0 OLED MOSI
# assert sunxi("PC01") == 65   # SPI-0 OLED MISO
# assert sunxi("PC02") == 66   # SPI-0 OLED CLK
# assert sunxi("PC03") == 67   # SPI-0 OLED CS
assert sunxi("PG08") == 200  # GPIO-G8 - E-Ink BUSY
# assert sunxi("PG09") == 201  # GPIO-G9 - OLED-DC

# bus = SMBus(0) # use with SMBus instead of spidev
# RST_PIN         = "PA06"
# DC_PIN          = "PG09"
# BUSY_PIN        = "PG08"

# Pin definition - CHANGED FOR NANOPI NEO
RST_PIN         = 6 # RX1
DC_PIN          = 201 # SDA
BUSY_PIN        = 200 # TX1

# SPI device, bus = 0, device = 0
SPI = spidev.SpiDev(0, 0) # use with spidev instead of SMBus


def digital_write(pin, value):
    GPIO.output(pin, value)

def digital_read(pin):
    return GPIO.input(pin)

def delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_writebyte(data):
    SPI.writebytes(data)

def module_init():
    GPIO.setmode(GPIO.RAW)    # spidev
    #GPIO.setmode(GPIO.SUNXI) # SMBus
    GPIO.setwarnings(False)
    GPIO.setup(RST_PIN, GPIO.OUT)
    GPIO.setup(DC_PIN, GPIO.OUT)
    GPIO.setup(BUSY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    SPI.max_speed_hz = 500000
    SPI.mode = 0b00
    return 0;

### END OF FILE ###
