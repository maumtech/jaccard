#!/bin/sh
cd /mnt/hgfs/E/images/14887-firefox/win7x32
cd 30
md5deep -p 512 win7x32.img > md5hash.txt

cd /mnt/hgfs/E/images/14887-firefox/win7x64
cd 10
md5deep -p 512 Windows_7_x64.img > md5hash.txt

cd /mnt/hgfs/E/images/14887-firefox/win7x64
cd 20
md5deep -p 512 Windows_7_x64.img > md5hash.txt

cd /mnt/hgfs/E/images/14887-firefox/win7x64
cd 30
md5deep -p 512 Windows_7_x64.img > md5hash.txt

cd /mnt/hgfs/E/images/14887-firefox/win7x64
cd 40
md5deep -p 512 Windows_7_x64.img > md5hash.txt

cd /mnt/hgfs/E/images/14887-firefox/win7x64
cd 50
md5deep -p 512 Windows_7_x64.img > md5hash.txt
