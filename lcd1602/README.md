## enable SPI Interface:
```
sudo raspi-config
```
->Interface Options -> I2C -> Enable -> Finish

## 
```
echo '1' > /sys/devices/virtual/alphalcd/lcdi2c/clear 
echo '11' > /sys/devices/virtual/alphalcd/lcdi2c/position 
echo "abc" > /dev/lcdi2c 
```
