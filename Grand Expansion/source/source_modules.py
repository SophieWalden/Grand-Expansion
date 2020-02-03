# Importing all the modules
try:
    import time, random, sys, os
except ImportError:
    print("Make sure to have the time module")
    sys.exit()
try:
    import pygame
except ImportError:
    print("Make sure you have python 3 and pygame.")
    sys.exit()
from pygame import freetype

try:
    import Menu
    import MainMenu
except ImportError:
    print("You don't have the extra files")
    sys.exit()