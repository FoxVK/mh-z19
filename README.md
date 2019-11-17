# mh-z19.py
Python3 readout of mh-z19 CO2 concentration sensor

Just call it with serial line as argument and you will get back	CO2 concentration in PPM
```
NTB:~$ python3 mh-z19.py /dev/ttyUSB0 
2746
```
(Datasheet of sensor)[https://www.winsen-sensor.com/d/files/infrared-gas-sensor/mh-z19b-co2-ver1_0.pdf]
## Note:
 - Outdoor concentration is 300-400 PPM
 - Recomended limit for human beings is 1500PPM
 
Sensor needs to be powered with 5V 150mA but it's logic is 3.3V
