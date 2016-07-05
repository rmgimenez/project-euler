'''from yahoo_finance import Share

fesa = Share('FESA4.SA')
valor_compra = 7.5
print('FESA4')
print('Valor compra:',valor_compra)
print('Valor atual',fesa.get_price())
print('Diferença',(float(fesa.get_price()) - valor_compra)*200)

itsa = Share('ITSA4.SA')
print('Valor atual ITSA4',itsa.get_price())


import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()'''
from urllib.request import urlopen
import xml.etree.ElementTree as ET

link_xml = 'http://imgur.com/r/cosplay/top/day.xml';
arq_xml = urlopen(link_xml)
xml = ET.parse(arq_xml)

items = []
for item_xml in xml.findall('item'):
	lista = {
		'id': item_xml.find('id').text,
		'hash': item_xml.find('hash').text,
		'author': item_xml.find('author').text,
		'title': item_xml.find('title').text,
		'score': item_xml.find('score').text,
		'size': item_xml.find('size').text,
		'views': item_xml.find('views').text,
		'is_album': item_xml.find('is_album').text,
		'mimetype': item_xml.find('mimetype').text,
		'ext': item_xml.find('ext').text
	}
	items.append(lista)

for item in items:
	print('====')
	for k, i in item.items():
		print(k, i)
	print('====')


