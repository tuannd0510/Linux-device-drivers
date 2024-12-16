# SG90-servo driver Raspberry Pi 3


## 
```
sudo nano /boot/config.txt
# add new lines
dtoverlay=pwm,pin=12,func=2
```


## pins configuration
Brown   - GND
Red     - VCC 5V
Orange  - PWM

duty = [1ms:2ms]
duty    |   deg
1ms     |   0
1.5ms   |   -90
2ms     |   90

## 

When the signal is high, we call this "on time". 
To describe the amount of "on time" , we use the concept of duty cycle. 

- pwm on time = signal high
- Duty cycle là tỷ lệ signal high trong 1 khoảng thời gian
- Period là chu kỳ xung.
- Pulse width là giá trị mức cao so với period.