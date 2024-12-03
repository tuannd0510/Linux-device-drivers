# Step
## 1. Precondition Kernel version < 6.1
### Install linux kernel 5.15
- Download .deb file here [v5.15](https://kernel.ubuntu.com/mainline/v5.15/)
```
  arm64/linux-headers-5.15.0-051500-generic-64k_5.15.0-051500.202110312130_arm64.deb
  arm64/linux-headers-5.15.0-051500-generic_5.15.0-051500.202110312130_arm64.deb
  arm64/linux-image-unsigned-5.15.0-051500-generic-64k_5.15.0-051500.202110312130_arm64.deb
  arm64/linux-image-unsigned-5.15.0-051500-generic_5.15.0-051500.202110312130_arm64.deb
  arm64/linux-modules-5.15.0-051500-generic-64k_5.15.0-051500.202110312130_arm64.deb
  arm64/linux-modules-5.15.0-051500-generic_5.15.0-051500.202110312130_arm64.deb
```
```bash
sudo dpkg -i *.deb
sudo reboot

# check
uname -a
```

refer 
https://www.youtube.com/watch?v=EN2p3Xc8rTc
