from gc_source_modules import *


# Load the images
def load_images(path_to_directory, height, width):
    import os
    import pygame
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                img = pygame.image.load(os.path.join(dirpath, name)).convert()
                img = pygame.transform.scale(img, (int(640 / width), int(640 / height)))
                images[key] = img
    return images


# Main Menu Looping Background
def gen_Board(board, height, width):
    import random
    for j in range(height):
        for i in range(width):
            percent = random.randint(1, 200)
            if percent <= 20:
                board[j][i] = "Grass"
            else:
                if percent <= 55:
                    board[j][i] = "barracks"
                if percent <= 60:
                    board[j][i] = "Water"
                elif percent <= 105:
                    board[j][i] = "Forest Lv1"
                elif percent <= 115:
                    board[j][i] = "Forest Lv3"

                elif percent <= 135:
                    board[j][i] = "town_01"
                elif percent <= 140:
                    board[j][i] = "town_02"
                elif percent <= 143:
                    board[j][i] = "town_03"
                elif percent <= 155:
                    board[j][i] = "town_04"

                elif percent <= 156:
                    board[j][i] = "City_00"
                elif percent <= 159:
                    board[j][i] = "Quarry Lv2"
                elif percent <= 162:
                    board[j][i] = "Quarry Lv3"
                elif percent <= 165:
                    board[j][i] = "Factory"
                elif percent <= 170:
                    board[j][i] = "Solar_Power"
                elif percent <= 175:
                    board[j][i] = "Super_Factory"
                elif percent <= 180:
                    board[j][i] = "FishingBoat"

                else:
                    board[j][i] = "Dam"
    return board


# Main Menu
def HomeScreen(pygame, gameDisplay, Fonts, clock, MusicPaused):
    global AnimationStage, Count, Images
    import main
    run = True
    screen = "Main"
    height = 20
    width = 20
    Images = []
    Images = load_images("Images", 8, 8)
    MenuBoard = gen_Board([[0] * height for _ in range(width)], height, width)
    AnimationStage = {"Water": [1, 0.5], "FishingBoat": [1, 0.5], "Dam": [1, 0.5]}
    x = 0
    y = 0

    while run:
        gameDisplay.fill((0, 100, 255))

        Count = {"Water": 0, "FishingBoat": 0, "Dam": 0, "Forest Lv4": 0, "Quarry Lv4": 0, "Super Factory": 0}
        for j in range(height):
            for i in range(width):
                if MenuBoard[j][i] == "Water" or MenuBoard[j][i] == "FishingBoat" or MenuBoard[j][i] == "Dam":
                    Count["Water"] += 1
                if MenuBoard[j][i] == "FishingBoat":
                    Count["FishingBoat"] += 1
                if MenuBoard[j][i] == "Dam":
                    Count["Dam"] += 1
                if MenuBoard[j][i] == "Forest Lv4":
                    Count["Forest Lv4"] += 1
                if MenuBoard[j][i] == "Quarry Lv4":
                    Count["Quarry Lv4"] += 1
                if MenuBoard[j][i] == "Super Factory":
                    Count["Super Factory"] += 1

        # Drawing all the tiles plus some extra to make it loop seemlessly
        for j in range(height):
            for i in range(width):
                main.draw(i * 80 + x, j * 80 + y, "Tile", MenuBoard[j][i], 8, 8, Images, AnimationStage, Count)
                main.draw(i * 80 + x + 1600, j * 80 + y, "Tile", MenuBoard[j][i], 8, 8, Images, AnimationStage, Count)
                main.draw(i * 80 + x, j * 80 + y + 1600, "Tile", MenuBoard[j][i], 8, 8, Images, AnimationStage, Count)
                main.draw(i * 80 + x + 1600, j * 80 + y + 1600, "Tile", MenuBoard[j][i], 8, 8, Images, AnimationStage,
                          Count)

        # Moving around tiles on screen by -x & -y
        x -= 2
        y -= 2

        if y < -1600:
            y = 0
            x = 0

        pos = pygame.mouse.get_pos()
        # Event checking mainly for clicking on the buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= pos[0] <= 600 and 600 <= pos[1] <= 700 and screen == "Main":
                    main.game_loop(8, 8, 0, False)
                if 825 <= pos[0] <= 925 and 800 <= pos[1] <= 900 and screen == "Main":
                    screen = "Options"
                if 625 <= pos[0] <= 925 and 500 <= pos[1] <= 900 and screen == "Main":
                    screen = "New Game"
                if 775 <= pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775 and screen == "Options":
                    screen = "Main"
                if 175 <= pos[0] <= 375 and 600 <= pos[1] <= 700 and screen == "Main":
                    main.game_loop(8, 8, 0, True)
                # Give user option to mute the background music
                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 50 and pos[1] <= 150 and screen == "Options":
                    if MusicPaused == False:
                        MusicPaused = True
                        pygame.mixer.music.pause()
                    else:
                        MusicPaused = False
                        pygame.mixer.music.unpause()

        # Shows Main screen text and buttons
        if screen == "Main":
            text_surface, rect = Fonts[2].render("Grand Command", (242, 43, 35))
            gameDisplay.blit(text_surface, (220, 50))
            # mouse hover & un-hover location
            if 600 <= pos[0] <= 830 and 620 <= pos[1] <= 840:
                # box location not-hover
                pygame.draw.rect(gameDisplay, (150, 0, 0), (580, 800, 200, 100), 0)
            else:
                # box location on-hover
                pygame.draw.rect(gameDisplay, (255, 0, 0), (580, 800, 200, 100), 0)

            text_surface, rect = Fonts[1].render("New Game", (0, 0, 0))
            gameDisplay.blit(text_surface, (600, 830))

            # mouse clickable to options -> menu for mute sound atm
            if 825 <= pos[0] <= 925 and 850 <= pos[1] <= 900:
                # box location not-hover
                pygame.draw.rect(gameDisplay, (150, 0, 0), (840, 800, 200, 100), 0)
            else:
                # box location on-hover
                pygame.draw.rect(gameDisplay, (255, 0, 0), (840, 800, 200, 100), 0)

            text_surface, rect = Fonts[1].render("Options", (0, 0, 0))
            gameDisplay.blit(text_surface, (880, 830))

            # Shows the options menu
        if screen == "Options":
            if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775:
                pygame.draw.rect(gameDisplay, (150, 0, 0), (775, 675, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (775, 675, 200, 100), 0)

            text_surface, rect = Fonts[1].render("Back", (0, 0, 0))
            gameDisplay.blit(text_surface, (835, 705))

            if 200 <= pos[0] <= 400 and 50 <= pos[1] <= 150:
                pygame.draw.rect(gameDisplay, (150, 0, 0), (200, 50, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (200, 50, 200, 100), 0)

            if MusicPaused == False:
                text_surface, rect = Fonts[1].render("Mute Music", (0, 0, 0))
                gameDisplay.blit(text_surface, (210, 80))
            else:
                text_surface, rect = Fonts[0].render("Unmute Music", (0, 0, 0))
                gameDisplay.blit(text_surface, (210, 86))

        pygame.display.flip()
        clock.tick(120)
