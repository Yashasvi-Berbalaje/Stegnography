import socket
import cv2
import time
from PIL import Image
import io 
def decode(img):
    # img = input("Enter image name(with extension) : ")
    # image = Image.open(img, 'r')
    # f = open('pythonimage123.jpg',"wb")
    # f.write(img)
    image = Image.open(io.BytesIO(img))
    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
        
        # string of binary data
        binstr = ''
        for i in pixels[:8]:
            # print(i)
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        # print(chr(int(binstr, 2)))
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data
c = socket.socket()
q = input("Enter the ip addess from where you want to receive the image")
p = int(input("Enter the port number"))
# r = input("Enter the extension of your received file - jpg , png , bmp")
# s = "pythonimage123." + r
# print(s)
condition = True
c.connect((q,p))
# f = open(s,"wb")
Data=bytes()
while condition:
    image = c.recv(1024)
    if str(image) == "b''":
        text=decode(Data)
        text_file = open("data.txt", "w")
        text_file.write(text)
        text_file.close()
        condition = False
    Data=Data+image


