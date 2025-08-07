import lvgl as lv
import lv_utils
from gc9a01_lv import GC9A01_lv
from machine import Pin, SPI

if not lv.is_initialized(): lv.init()
if not lv_utils.event_loop.is_running(): event_loop=lv_utils.event_loop()

lcd_spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11))
lcd_dc = Pin(8, Pin.OUT)
lcd_cs = Pin(9, Pin.OUT)
lcd_rst = Pin(13, Pin.OUT)
lcd_bl = Pin(25, Pin.OUT)

disp_drv = GC9A01_lv(lcd_spi, lcd_rst, lcd_cs, lcd_dc, lcd_bl)

scr = lv.obj()

lv.screen_load(scr)

cal = lv.calendar(scr)
cal.align(lv.ALIGN.CENTER,0,0)
cal.set_size(180,180)

d = lv.calendar.add_header_dropdown(cal)