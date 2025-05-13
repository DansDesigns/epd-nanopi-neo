# epd-nanopi-neo
Waveshare E-Paper Display modified for NanoPi Neo/Air/Core

This code controls the Waveshare 1.54 inch E-Paper display (variant B, BW/three-color) on a NanoPi Neo.

## Prerequisites

- apt: python3-pip, python3-pil python3-spidev
- npi-config/armbian-config: enable SPI0
- or add to /boot/armbianEnv.txt:
    param_spidev_spi_bus=0
    param_spidev_max_freq=4500000
- Github: OPi-GPIO

## Pin Mapping can be changed in epdconfig.py

|  Display |   NanoPi   |
VCC--------3.3V-------17
GND--------GND--------20
CS---------24---------24 (PC3)
RESET------12---------12 (PA6)
DC/RS------18---------18 (PG9)
MOSI-------19---------19 (PC0)
SCK--------23---------23 (PC2)

