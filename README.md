# epd-nanopi-neo
Waveshare E-Paper Display modified for NanoPi Neo/Air/Core

This code controls the Waveshare 1.54 inch E-Paper display (variant B, BW/three-color) on a NanoPi Neo.

## Prerequisites

- apt: python3-pip, python3-pil python3-spidev
- npi-config/armbian-config: enable SPI0
- Github: OPi-GPIO

## Pin Mapping can be changed in epdconfig.py

|Display | NanoPi |
VCC----3.3V-----17
GND----GND------20
CS--------------13 (PA13)
RESET----------- 6 (PA06)
DC/RS--------- 201 (PG09)
MOSI----------- 64 (PC00)
SCK------------ 66 (PC02)
BUSY---------- 200 (PG08)

