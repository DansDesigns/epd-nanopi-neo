# epd-nanopi
Waveshare E-Paper Display on a NanoPi Duo2

This code controls the Waveshare 1.54 inch E-Paper display (variant B, three-color) on a NanoPi Duo2.

## Prerequisites

- apt: python-pip, python-pil
- pip: spidev
- npi-config: enable SPI1, disable UART1, disable I2C1

## Pin Mapping

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


