#!/usr/bin/python

from images2gif import writeGif
from PIL import Image
import os

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.gif')))

images = [Image.open(fn) for fn in file_names]

filename = 'my.gif'

writeGif(filename, images, duration=0.5)


