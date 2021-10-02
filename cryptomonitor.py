#!/usr/bin/python
#matrice
import re
import time
import datetime
import argparse
contras=1
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


#autrre
import time
import hmac
import urllib
import requests
import hashlib
import base64
import sys
import json

import subprocess


def heure():

    for boubou in range(1):
        for heu in range(5):
            now = datetime.datetime.now()  # recup date  
            timestamp = time.mktime(now.timetuple())  # convertion  
            h=datetime.datetime.fromtimestamp(int(timestamp)).strftime('%H')
            m=datetime.datetime.fromtimestamp(int(timestamp)).strftime('%M')
            s=datetime.datetime.fromtimestamp(int(timestamp)).strftime('%S')
            d=datetime.datetime.fromtimestamp(int(timestamp)).strftime('%d')
            month=datetime.datetime.fromtimestamp(int(timestamp)).strftime('%m')

            with canvas(device) as draw:
                text(draw,(16,0),str(h)+":"+str(m).zfill(2)+":"+str(s).zfill(2), fill="white", font=TINY_FONT)
            time.sleep(0.5)
        with canvas(device) as draw:
            text(draw,(22,0),str(d)+"/"+str(month), fill="white", font=TINY_FONT)
        time.sleep(5)


def affichage():
    for boudeb in range(2):    
        for boucle in range(64):
            with canvas(device) as draw:
                text(draw, (int(boucle)-4, 0), "!", fill="white")
                text(draw, (64-int(boucle), 0), "!", fill="white")
                text(draw, (30, int(boucle)-32), "!", fill="white")
                time.sleep(0.05)
        

    fichier = open("data.txt", "r") 
    contenu = fichier.read()
    fichier.close()  
    print("ecriture")
    show_message(device, str(contenu), fill="white", font=proportional(CP437_FONT), scroll_delay=0.05) ## slide
    time.sleep(1)
 
            



#programme

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=8, block_orientation=-90, rotate=0)
print("Created device")
device.contrast(10)

with canvas(device) as draw:
    text(draw,(21,0),"Miner", fill="white", font=TINY_FONT)
time.sleep(2)
with canvas(device) as draw:
    text(draw,(18,0),"Monitor", fill="white", font=TINY_FONT)    
time.sleep(2)
with canvas(device) as draw:
    text(draw,(21,0),"clock", fill="white", font=TINY_FONT)  
time.sleep(2)
while True:

    heure()
    subprocess.call("python requests.py 1", shell=True)
    affichage()


