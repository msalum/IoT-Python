# IoT-Python

 README for homework 5.

Prerequisites

* A WeMos Lolin32 microcontroller with at least one color led
* picocom sudo apt-get install picocom. On OS X you need Homebrew to install picocom by: brew install picocom)
* wget sudo apt-get install wget. On OS X brew install wget
* Silabs VCP driver for OS X
* esptool pip install esptool
* Adafruit-ampy pip install adafruit-ampy

How to use

Flashing MicroPython

Install MicroPython:

wget http://micropython.org/resources/firmware/esp32-20171017-v1.9.2-279-g090b6b80.bin
esptool.py -p /dev/ttyUSB0 -b 460800 erase_flash
esptool.py -p /dev/ttyUSB0 -b 460800 write_flash --flash_mode dio 0x1000 esp32-*.bin
Note that in OS X the ttyUSB0 is replaced with tty.SLAB_USBtoUART. This applies for entire project!

Get the microcontroller ready

Upload files to ESP32:

ampy -p /dev/ttyUSB0 put boot.py
ampy -p /dev/ttyUSB0 put main.py
Run it

Connect through picocom:

picocom -b115200 /dev/ttyUSB0
Run the code:

main()
Enter the shown ip into the browser and start blinking.


