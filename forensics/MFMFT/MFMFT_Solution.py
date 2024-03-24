import os

indices = [0, 10, 17, 18, 5, 6, 15, 13, 9, 16, 12, 5, 11, 1, 14, 5, 7, 6, 7, 3, 2, 2, 10, 8, 4, 7]

mft = open("TheMFT", "rb")
flag = ""

for index in indices:
    position = index*0x400+0xda
    mft.seek(position, 0)
    byteRead = mft.read(1)
    flag += byteRead.decode()

print(flag)