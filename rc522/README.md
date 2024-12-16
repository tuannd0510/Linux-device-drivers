# Setup Rpi
Enable SPI interface
```bash
sudo raspi-config
# / Interface Options / SPI / Enable / Finish
```

Connection GPIO
![RPI <-> RC522 module](rfid-rpi.png)

## Insert driver 


```bash
make
dtc spidev_disabler.dts -O dtb >spidev_disabler.dtbo
sudo cp spidev_disabler.dtbo /boot/overlays/
```


```bash
sudo nano /boot/config.txt
# add new line:
dtoverlay=spidev_disabler
```

## Run file test






