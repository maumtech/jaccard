#!/bin/sh
cd /mnt/hgfs/E/images/14416-wiresharK/win7x64
cd 30
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
cd /mnt/hgfs/E/images/14416-wireshark/win7x64
cd 40
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
cd /mnt/hgfs/E/images/14416-wireshark/win7x64
cd 50
qemu-img convert -f vmdk Windows_7_x64.vmdk Windows_7_x64.img
