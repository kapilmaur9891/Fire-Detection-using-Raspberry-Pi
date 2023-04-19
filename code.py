#  The code to read the value of a smoke sensor with a Raspberry Pi is shown below.

# The botbook_mcp3002 library which you need to import into your code can be obtained at the following link: botbook_mcp3002.You just have to copy the contents of the page this redirects you to and save it as a .py file (a python file).

# /* MQ-2 Smoke Sensor Circuit with Raspberry Pi */

#*****SimpsonsAlarm.py*****#
from twilio.rest import Client
import PCF8591 as ADC
import LCD1602 as LCD
import RPi.GPIO as GPIO
import time
import math

# Board Setup
GPIO.setmode(GPIO.BCM)

# Pin Setup
gas = 17
buzzer = 18
fire = 27

#*****Initialize Pins*****#
def setup():
    ADC.setup(0x48)
    LCD.init(0x27, 1)
    GPIO.setup(fire, GPIO.IN)
    GPIO.setup(gas, GPIO.IN)
    GPIO.setup(buzzer, GPIO.OUT)
    global Buzz						# Assign a global variable to replace GPIO.PWM
    Buzz = GPIO.PWM(buzzer, 440)

#*****Core Functionality*****#
def loop():
    while True:
        firetmp =  ADC.read(0) # get analog value from flame sensor
        gaslvl = ADC.read(1) # get analog value from gas sensor
        lvls = "Gas: " +str(gaslvl)+", Fire: "+str(firetmp)
        digFire = GPIO.input(fire) # Flame sensor digital output
        digGas = GPIO.input(gas) # Gas sensor digital output

        if digFire == 0 or digGas == 0: # fire or gas levels are too high
            warning = 'DOH! Something is not okay!!\nLevels: '+lvls #Simpson's Reference
            print(warning)
            time_end = time.time() + 30 # setup for 30 second while loop
            while time.time() < time_end: # flash warnings for 30 seconds
                clearLCD()
                LCD.write(0, 0, 'DOH! Something  ') # write warning on LCD
                LCD.write(0, 1, 'is not Okay!    ')
                time.sleep(3)
                clearLCD()
                LCD.write(0, 0, '*****Danger*****')
                LCD.write(0, 1, 'Fire:'+str(firetmp)+' Gas:'+str(gaslvl))
                time.sleep(3)

        else: # otherwise
            print (lvls) # display fire and gas levels in command line
            LCD.write(0, 0, 'Gas: '+str(gaslvl)) # write levels to lcd
            LCD.write(0, 1, 'Fire: '+str(firetmp))
            time.sleep(3)
            LCD.write(0, 0, 'Everything Is Ok')
            LCD.write(0, 1, '****************')
            Buzz.start(50) # make the buzzer make noise
            time.sleep(2)
            Buzz.stop() # stop the buzzer
            time.sleep(1)
            clearLCD()



#*****Clear Contents of LCD*****#
def clearLCD():
        LCD.write(0, 0, '                ')
        LCD.write(0, 1, '                ')
        time.sleep(.1)

#*****Main*****#
if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		pass