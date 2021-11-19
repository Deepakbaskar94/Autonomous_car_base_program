from Adafruit_SSD1306 import SSD1306_128_64
from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


SHUNT_OHMS = 0.1
RST = None
disp = SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
#draw.rectangle((0,0,disp.width,disp.height), outline=0, fill=0)

padding = -2
top = padding
bottom = disp.height - padding
x = 0
displaydata = "a"
displaydata1 = "b"
displaydata2 = "c"
#font = ImageFont.load_default()

ina = INA219(SHUNT_OHMS)
ina.configure()

print("Press Ctrl+C to quit.")
sleep(1)

def oled_data(displaydata, displaydata1, displaydata2):
                draw.rectangle((0,0,disp.width,disp.height), outline=0, fill=0)
                bus_V = round(ina.voltage(), 2)
                bus_I = round(ina.current(), 2)
                power = round(ina.power(), 2)
                shunt_V = round(ina.shunt_voltage(), 2)
                load_V  = round((bus_V + (shunt_V/1000)), 2)

                draw.text((x, top), "Probe Plus Bot", font=font, fill=255)
                draw.text((x, top+16), "Bus V: " + str(bus_V) + " V", font=font, fill=255)
                draw.text((x, top+24), "Bus Curr: " + str(bus_I) + " mA", font=font, fill=255)
                #draw.text((x, top+32), "Power: " + str(power) + " mW", font=font, fill=255)
                #draw.text((x, top+40), "Shunt V: " + str(shunt_V) + " mV" , font=font, fill=255)
                #draw.text((x, top+48), "Load V: " + str(load_V) + " V", font=font, fill=255)
                draw.text((x, top+32), "distance: " + displaydata + " mm", font=font, fill=255)
                draw.text((x, top+40), "distanceL: " + displaydata1 + " mm", font=font, fill=255)
                draw.text((x, top+48), "distanceR: " + displaydata2 + " mm", font=font, fill=255)

                disp.image(image)
                disp.display()
                sleep(.1)

for x in range(1):
           oled_data(displaydata, displaydata1, displaydata2)

'''except DeviceRangeError as e:
        print (e)

except KeyboardInterrupt as e:
        print("\nProgram closed")

finally:
        draw.rectangle((0,0,disp.width,disp.height), outline=0, fill=0)
        disp.image(image)
        disp.display()'''

