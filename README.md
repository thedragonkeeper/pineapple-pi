# pineapple-pi
adds a rpi0 to mk7 pineapple

# Optional hardware modification
1. on the top side of the mk7, remove the pins of the usb port from the motherboard
2. pull the middle pins out of the usb connector
3. cut the usb cable from a usb hub and solder the wires to the bottom side of the mk7s usb; making the hub permanent part of the mk7
4. remove the connector for the hubs power cable and attach the positive and negative wires to the correct pins remaining within the mk7s usb port
5. 3d print a new case to hold the new parts, an stl is provided in this repo which allows enough clearance for my hub (without extra clearance, will cause mk7 to feel alot warmer than normal)

# Manual setup

## mk7
Check that the kernel is 4.14.180 otherwise the ipk wont work.
1. ssh into mk7
2. wget https://github.com/TheDragonkeeper/pineapple-pi/blob/main/kmod-usb-net-cdc-ether_4.14.180-1_mipsel_24kc.ipk
4. opkg update ; opkg --force-depends kmod-usb-net-cdc-ether_4.14.180-1_mipsel_24kc.ipk
5. opkg install sshfs
6. connect rpi0 via usb port
7. setup ssh a ssh key and send it to the rpi
8. create file .ssh/config add:
```
    Host rpi
       User       root
       IdentityFile       ~/.ssh/rpiz
```
9. edit /etc/config/network and replace the usb0 section with:
```
    config interface 'usb'
        option ifname 'usb0'
        option proto 'static'
        option netmask '255.255.255.0'
        option ipaddr '172.69.69.1'
 ```
 
 10. edit /etc/hosts and add
 ```
     172.69.69.2 rpi
```


## rpi
packages to install:
```
    apt-get install python3-pycurl
```
1. edit /etc/network/interfaces.d/usb0
```
    allow-hotplug usb0
    iface usb0 inet static
    address 172.69.69.2
    netmask 255.255.255.0
    network 172.69.69.0
    broadcast 172.69.69.255
    gateway 172.69.69.1
```
2. edit /etc/hosts and add
```
    172.69.69.1 mk7
```
