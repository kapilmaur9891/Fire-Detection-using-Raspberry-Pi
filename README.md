# Fire-Detection-using-Raspberry-Pi
In this project, we will go over how to build a smoke sensor circuit with a Raspberry Pi.

The smoke sensor we will use is the MQ-2. This is a sensor that is not only sensitive to smoke, but also to flammable gas.

The MQ-2 smoke sensor reports smoke by the voltage level that it outputs. The more smoke there is, the greater the voltage that it outputs. Conversely, the less smoke that it is exposed to, the less voltage it outputs.

The MQ-2 also has a built-in potentiometer to adjust the sensitivity to smoke. By adjusting the potentiometer, you can change how sensitive it is to smoke, so it's a form of calibrating it to adjust how much voltage it will put out in relation to the smoke it is exposed to.

We will wire the MQ-2 to a raspberry pi so that the raspberry pi can read the amount of voltage output by the sensor and output to us if smoke has been detected if sensor outputs a voltage above a certain threshold. This way, we will know that the sensor has, in fact, detected smoke.


Components Needed

Raspberry Pi board
MQ-2 Smoke Sensor
MCP3002 Analog-to-digital Converter Chip

The Raspberry Pi is our microcontroller of choice for this circuit. You can really use any Raspberry Pi board, the Model A or the Model B. In our circuit, the Model B Raspberry Pi board will be used. This can be obtained from a number of different suppliers online. We recommend Farnell Element 14, whose Raspberry Pi Model B board can be found at the following link: Raspberry Pi Model B.



Important, it is recommended that you do not obtain the standalone sensor but the whole MQ-2 board. This is because if you buy the standalone sensor, you will have to finish building the whole schematic before you can connect it to the raspberry pi. So that less work is required for integrating this with the raspberry pi, it is recommended that you buy the complete MQ-2 sensor circuit. This you can see below.

If you buy the complete board, there are 3 leads which need to be connected.

Being that the Raspberry Pi cannot process analog signals by itself (it can only process and interpret digital signals), we need an analog-to-digital converter to convert the analog signals to digital signals, so that the Raspberry Pi can manage it. This is why we need an ADC chip and the one we will use is a MCP3002. Using this chip, the Raspberry Pi can interpret analog signals.

MQ-2-smoke-sensor-pinout

The 3 leads are Output, VCC, and GND.

It's very basic.

The gas sensor needs about 5 volts of power in order to operate. This is done by connecting 5 volts to Vcc and GND.

The Output pin gives out the voltage reading, which is proportional to the amount of smoke that the sensor is exposed to. Again, a high voltage output means the sensor is exposed to a lot of smoke. A low or 0 voltage output means the sensor is exposed to either little or no smoke.


