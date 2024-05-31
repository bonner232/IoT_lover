import connect
import mqtt
import ai
from time import sleep
import utime
import machine
import sys
import neopixel
import uasyncio
BROKER_ADDRESS = '192.168.1.93'
CLIENT_ID = 'esp322'

pin_high = machine.Pin(21, machine.Pin.OUT)
pin_high.value(1)

# Define the number of pixels and the pin number for the pixel
num_pixels = 7
pixel_pin = machine.Pin(12)

# Create a NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

connect.connect_to_wifi('****', '*****')

mqtt.connect_mqtt()
print("conncted")
mqtt.publish_to_mqtt()
print("send to melina")
running = True

#while running:
 #   aivar = ai.runall()
  #  print(aivar)
   # print("_______")
    
    #if aivar >100:
     #   running = False
        #mqtt.publish_to_mqtt()
        #for i in range(num_pixels):
            #pixels[i] = (0, 255, 0)
            #pixels.write()
            #sleep(5)
            #for i in range(num_pixels):
                #pixels[i] = (0, 0, 0)
                #pixels.write()
                
        
    


async def func1():
    
    # Run for 1 second (1000 milliseconds)
    #while utime.ticks_diff(utime.ticks_ms(), start_time) < 2000:
        # Your code to run for 1 second goes here
    i = 0
    j = 0
    while j < 200:
    
        aivar = ai.runall()
        print(aivar)
        print("_______")
        j = j + 1
        print(j)
        if aivar > -118:
            for i in range(num_pixels):
                pixels[i] = (0, 0, 255)
                pixels.write()
                sleep(0.2)
                for i in range(num_pixels):
                    pixels[i] = (0, 0, 0)
                    pixels.write()
            
        
        
        if aivar > 100:
            mqtt.publish_to_mqtt()
            print("out")
            for i in range(num_pixels):
                pixels[i] = (0, 255, 0)
                pixels.write()
                sleep(0.2)
                for i in range(num_pixels):
                    pixels[i] = (0, 0, 0)
                    pixels.write()
                    
        
        
        
    await uasyncio.sleep_ms(60)
            
            
        
    # Sleep for 10 milliseconds
    
    #while True:
     #   aivar = ai.runall()
      #  print(aivar)
       # print("_______")
        #await uasyncio.sleep_ms(10)
        #if aivar > 100:
         #   mqtt.publish_to_mqtt()
            
          #  print("out")

async def func2():
    
    read_var = mqtt.read_mqtt()
    print("fun2")
    print(read_var)
    
                
        

        
    await uasyncio.sleep_ms(10)

async def main():
    task1 = uasyncio.create_task(func1())
    task2 = uasyncio.create_task(func2())
    await uasyncio.gather(task1, task2)

while True:
    uasyncio.run(main())
    





















