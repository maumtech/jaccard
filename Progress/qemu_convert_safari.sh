#!/bin/sh
cd /mnt/hgfs/E/images/15151-safari/win7x32
cd 30
qemu-img convert -f vmdk win7x32.vmdk win7x32.img 

cd /mnt/hgfs/E/images/15151-safari/win7x64
cd 10
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
cd /mnt/hgfs/E/images/15151-safari/win7x64
cd 20
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
cd /mnt/hgfs/E/images/15151-safari/win7x64
cd 30
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
cd /mnt/hgfs/E/images/15151-safari/win7x64
cd 40
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
cd /mnt/hgfs/E/images/15151-safari/win7x64
cd 50
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
cd /mnt/hgfs/E/images/15151-safari/winXP
cd 30
qemu-img convert -f vmdk winxp-flat.vmdk winxp-flat.img 
