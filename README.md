# GC9A01 Display Driver for lv_micropython

Modify the original project to remove tjpgd in order to avoid conflicts with the version integrated in LVGL.

To build the firmware(RP2040 platform):

```
mkdir build-lvmicropython
cd build-lvmicropython

git clone https://github.com/lvgl/lv_micropython.git
git clone https://github.com/calico-cat-3333/gc9a01_mpy_lv.git

echo 'include(${CMAKE_CURRENT_LIST_DIR}/lv_micropython/user_modules/lv_binding_micropython/bindings.cmake)' >> bind.cmake
echo 'include(${CMAKE_CURRENT_LIST_DIR}/gc9a01_mpy_lv/src/micropython.cmake)' >> bind.cmake

echo 'module("lv_utils.py", base_path="../../../user_modules/lv_binding_micropython/lib")' >> lv_micropython/ports/rp2/boards/manifest.py
echo 'module("fs_driver.py", base_path="../../../user_modules/lv_binding_micropython/lib")' >> lv_micropython/ports/rp2/boards/manifest.py

cd lv_micropython
git submodule update --init --recursive user_modules/lv_binding_micropython
make -C ports/rp2 BOARD=PICO submodules
make -j -C mpy-cross
make -j -C ports/rp2 BOARD=PICO USER_C_MODULES=../../../bind.cmake
```

Note: The files in the firmware folder are not prebuilt binaries. Please do not use them.

Note: Tested only on the RP2040 platform.

## Example Useage

see [examples/lvgl_calendar](examples/lvgl_calendar)

You need to copy the lv_utils.py file from [https://github.com/lvgl/lv_binding_micropython/blob/master/lib/lv_utils.py](https://github.com/lvgl/lv_binding_micropython/blob/master/lib/lv_utils.py) to your RP2040 development board.

# Original project README

# GC9A01 Display Driver for MicroPython

<p align="center">
  <img src="https://raw.githubusercontent.com/russhughes/gc9a01_mpy/master/docs/GC9A01.jpg" alt="GC9A01 display photo"/>
</p>

This driver is based on [devbis' st7789_mpy driver.](https://github.com/devbis/st7789_mpy)
I modified the original driver for one of my projects to add:

- Display Rotation.
- Scrolling
- Writing text using bitmaps converted from True Type fonts
- Drawing text using 8 and 16 bit wide bitmap fonts
- Drawing text using Hershey vector fonts
- ~~Drawing JPG's, including a SLOW mode to draw jpg's larger than available ram
  using the TJpgDec - Tiny JPEG Decompressor R0.01d. from
  http://elm-chan.org/fsw/tjpgd/00index.html~~

Included are 12 bitmap fonts derived from classic pc text mode fonts, 26 Hershey vector fonts and several example programs for different devices. The driver supports 240x240 displays.

## Documentation

Documentation can be found in the docs directory and at https://russhughes.github.io/gc9a01_mpy/

## Pre-compiled firmware files

The firmware directory contains pre-compiled firmware for various devices with the gc9a01 C driver and frozen python font files. See the README.md file in the fonts folder for more information on the font files.

### ESP32 BOARDS firmware

  - ARDUINO_NANO_ESP32
  - ESP32_GENERIC with 4, 8, 16, or 32MB flash
  - ESP32_GENERIC_C3 with 4, 8, 16, or 32MB flash
  - ESP32_GENERIC_S2 with 4, 8, 16, or 32MB flash
  - ESP32_GENERIC_S3 with 4, 8, 16, or 32MB flash
  - LILYGO_TTGO_LORA32
  - LOLIN_C3_MINI
  - LOLIN_S2_MINI
  - LOLIN_S2_PICO
  - M5STACK_ATOM
  - OLIMEX_ESP32_POE
  - SIL_WESP32
  - UM_FEATHERS2
  - UM_FEATHERS2NEO
  - UM_FEATHERS3
  - UM_NANOS3
  - UM_PROS3
  - UM_TINYPICO
  - UM_TINYS2
  - UM_TINYS3
  - UM_TINYWATCHS3

### RP2040 BOARDS firmware

  - ADAFRUIT_ITSYBITSY_RP2040
  - ADAFRUIT_QTPY_RP2040
  - ARDUINO_NANO_RP2040_CONNECT
  - ADAFRUIT_FEATHER_RP2040
  - GARATRONIC_PYBSTICK26_RP2040
  - NULLBITS_BIT_C_PRO
  - PIMORONI_PICOLIPO_16MB
  - PIMORONI_PICOLIPO_4MB
  - PIMORONI_TINY2040
  - RPI_PICO
  - RPI_PICO_W
  - SPARKFUN_PROMICRO
  - SPARKFUN_THINGPLUS
  - W5100S_EVB_PICO
  - W5500_EVB_PICO
  - WAVESHARE_RP2040_LCD_1.28
  - WEACTSTUDIO

This is a work in progress.

-- Russ
