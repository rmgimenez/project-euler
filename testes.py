# teste
import math

from time import time
start = time()

import funcoes

import requests
import xml.etree.ElementTree as ET


r = requests.get('http://imgur.com/r/wallpapers/top/day.xml', 
                 headers={'Cache-Control': 'no-cache'})
print('Variável', r.text)


print("Time: {0} secs".format(time()-start))