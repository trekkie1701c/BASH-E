import time

from PIL import Image
from picharsso import new_drawer

def convert(image):
	drawer = new_drawer("braille", height=64, colorize=True)
	print(drawer(image))
