# Importing all the modules
from pygame import freetype

# time delay & random
import random
import time
from time import sleep
import os




# Try import time
try:
    import time,sys
except ImportError:
    print("Make sure you have imported time & sys module")
    sys.exit()


# Try import random
try:
    import random,sys
except ImportError:
    print("Make sure you have imported random & & sys module")
    sys.exit()

# Try Import Sys
try:
    import sys
except ImportError:
    print("Make sure you have imported the sys module")
    sys.exit()

# Try Import os
try:
    import os
except ImportError:
    print("Make sure you have imported the os module")
    sys.exit()

# Try import pygame
try:
    import pygame
except ImportError:
    print("Make sure you have imported pygame.")
    sys.exit()

# Try import menu
try:
    import menu
except ImportError:
    print("Cant import menu @ this time")
    sys.exit()

# Try import mainMenu
try:
    import mainMenu
except ImportError:
    print("Cant import mainMenu @ this time")
    sys.exit()
