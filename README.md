# epd-nanopi-neo
Waveshare E-Paper Display modified for NanoPi Neo/Air/Core

This code controls the Waveshare 1.54 inch E-Paper display (variant B, BW/three-color) on a NanoPi Neo.

## Prerequisites

- apt: python-pip, python-pil
- pip: spidev
- npi-config: enable SPI1, disable UART1, disable I2C1
- Github: OPi-GPIO

## Pin Mapping can be changed in 

| Display | NanoPi |
|---------|--------|
| BUSY    | TX1    |
| RST     | RX1    |
| DC      | SDA    |
| CS      | CS     |
| CLK     | CLK    |
| DIN     | MOSI   |
| GND     | GND    |
| VCC     | 3V3    |


