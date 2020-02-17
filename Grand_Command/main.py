from gc_game_data import *


# Making the window
gameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))
pygame.display.set_caption("Grand Command")

# Fonts
from gc_fonts import *


#Loading the images


#Multipliers for Prestige


#Map Level
global MapLevel
MapLevel = 1

# Music
pygame.mixer.music.load('Sounds/Background_SoundTrack.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)
global MusicPaused
MusicPaused = False

#Shorten is a function that takes a number and shortens it while still keeping the value because of the use of letters


#Generates a board using a height and a width



# Checks for all the achievments







# Tile Information
from tile_information import *

    # Draws the green selection thing



# Generates a board using a height and a width



# Main Info for GC


    # Declaring a ton of variables


    # Saves data(Useful for Prestiges)


            # Moving your selection with the keys


            # Triggers when you press the mouse


                # Yes or no for Demolishing Buildings


                # Demolishing Buildings


                # Making the selection


                # Restarts the game


                # Prestige shop


                        # Adds things to cost


                        # Wood Upgrade


                        # Stones Upgrade


                        # Food Upgrade


                        # Metal Upgrade


                        # Electricity Upgrade


                        # Mandorium Miner


                # Showing Options


                    # Runs the options window


                        # Handles Events


                                # Saves your data to a save file


                                    # Exports save data


                                # Import save Data:


                        # Displays all the buttons



                # Demolishes Selected Building


                # All of the upgrades


                # Path Choices


                # Taking you back to mainscreen when you finish and calculates time


        # Counting Tiles for certain animations


        # Drawing all Tiles


        # Drawing Selection


        # This is my try at making multiple files. It looks very ineffecient and probably bad to use.

        # Achvievment Check


        # Display the Achievement


        # Shows a confirm message


        # Auto Save



MusicPaused = mainMenu.HomeScreen(pygame, gameDisplay,[font_40,font_50,font_150], clock, MusicPaused)





