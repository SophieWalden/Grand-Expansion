from custom_source_modules import *
#This is the file for all the code in the main menu

#Load the images
def load_images(path_to_directory,height,width):
    import os
    import pygame
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                img = pygame.image.load(os.path.join(dirpath, name)).convert()
                img = pygame.transform.scale(img,(int(640/width),int(640/height)))
                images[key] = img
    return images

#Generates a board using a height and a width
def gen_Board(board,height,width):
    import random
    for j in range(height):
        for i in range(width):
            percent = random.randint(1,100)
            if percent <= 50:
                board[j][i] = "Grass"
            else:
                if percent <= 60:
                    board[j][i] = "Water"
                elif percent <= 75:
                    board[j][i] = "Forest Lv1"
                else:
                    board[j][i] = "Quarry Lv1"
    return board

#Main Menu
def HomeScreen(pygame, gameDisplay, Fonts, clock, MusicPaused):
    global AnimationStage, Count, Images
    import Main
    run = True
    screen = "Main"
    height = 20
    width = 20
    Images = []
    Images = load_images("Images",8,8)
    MenuBoard = gen_Board([[0] * height for _ in range(width)],height,width)
    AnimationStage = {"Water": [1,0.5],"Fisherman": [1,0.5],"Dam": [1,0.5]}
    x = 0
    y = 0
    

    while run == True:

        gameDisplay.fill((0,100,255))

        
        
        #Counting for animation speed
        Count = {"Water": 0,"Water Fish": 0,"Dam": 0,"Forest Lv4": 0,"Quarry Lv4": 0,"Super Factory": 0}
        for j in range(height):
            for i in range(width):
                if MenuBoard[j][i] == "Water" or MenuBoard[j][i] == "Water Fish" or MenuBoard[j][i] == "Water Dam":
                    Count["Water"] += 1
                if MenuBoard[j][i] == "Water Fish":
                    Count["Water Fish"] += 1
                if MenuBoard[j][i] == "Dam":
                    Count["Dam"] += 1
                if MenuBoard[j][i] == "Forest Lv4":
                    Count["Forest Lv4"] += 1
                if MenuBoard[j][i] == "Quarry Lv4":
                    Count["Quarry Lv4"] += 1
                if MenuBoard[j][i] == "Super Factory":
                    Count["Super Factory"] += 1


        #Drawing all the tiles plus some extra to make it loop seemlessly
        for j in range(height):
            for i in range(width):
                Main.draw(i * 80 + x,j * 80 + y,"Tile",MenuBoard[j][i],8,8, Images, AnimationStage, Count)
                Main.draw(i * 80 + x,j * 80 + y,"Tile",MenuBoard[j][i],8,8, Images, AnimationStage, Count)
                Main.draw(i * 80 + x + 1600,j * 80 + y,"Tile",MenuBoard[j][i],8,8, Images, AnimationStage, Count)
                Main.draw(i * 80 + x,j * 80 + y + 1600,"Tile",MenuBoard[j][i],8,8, Images, AnimationStage, Count)
                Main.draw(i * 80 + x + 1600,j * 80 + y + 1600,"Tile",MenuBoard[j][i],8,8, Images, AnimationStage, Count)

        #Moving around tiles on screen
        x -= 2
        y -= 2

        if y < -1600:
            y = 0
            x = 0


        pos = pygame.mouse.get_pos()
        #Event checking mainly for clicking on the buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 400 and pos[0] <= 600 and pos[1] >= 600 and pos[1] <= 700 and screen == "Main":
                    Main.game_loop(8,8,0,False)
                if pos[0] >= 625 and pos[0] <= 825 and pos[1] >= 600 and pos[1] <= 700 and screen == "Main":
                    screen = "Options"
                if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775 and screen == "Options":
                    screen = "Main"
                if pos[0] >= 175 and pos[0] <= 375 and pos[1] >= 600 and pos[1] <= 700 and screen == "Main":
                    Main.game_loop(8,8,0,True)
                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 50 and pos[1] <= 150 and screen == "Options":
                    if MusicPaused == False:
                        MusicPaused = True
                        pygame.mixer.music.pause()
                    else:
                        MusicPaused = False
                        pygame.mixer.music.unpause()

                    
        #Shows Main screen text and buttons
        if screen == "Main":
            text_surface, rect = Fonts[2].render(("Grand Expansion"), (0, 0, 0))
            gameDisplay.blit(text_surface, (85, 50))


            if pos[0] >= 175 and pos[0] <= 375 and pos[1] >= 600 and pos[1] <= 700:
                pygame.draw.rect(gameDisplay,(150,0,0),(175,600,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(175,600,200,100),0)


            if pos[0] >= 400 and pos[0] <= 600 and pos[1] >= 600 and pos[1] <= 700:
                pygame.draw.rect(gameDisplay,(150,0,0),(400,600,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(400,600,200,100),0)

            text_surface, rect = Fonts[1].render(("New Game"), (0, 0, 0))
            gameDisplay.blit(text_surface, (420, 630))

            text_surface, rect = Fonts[1].render(("Continue"), (0, 0, 0))
            gameDisplay.blit(text_surface, (200, 630))

            if pos[0] >= 625 and pos[0] <= 825 and pos[1] >= 600 and pos[1] <= 700:
                pygame.draw.rect(gameDisplay,(150,0,0),(625,600,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(625,600,200,100),0)

            text_surface, rect = Fonts[1].render(("Options"), (0, 0, 0))
            gameDisplay.blit(text_surface, (670, 630))

        #Shows the options menu
        if screen == "Options":
            if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775:
                pygame.draw.rect(gameDisplay,(150,0,0),(775,675,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(775,675,200,100),0)

            text_surface, rect = Fonts[1].render(("Back"), (0, 0, 0))
            gameDisplay.blit(text_surface, (835, 705))

            if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 50 and pos[1] <= 150:
                pygame.draw.rect(gameDisplay,(150,0,0),(200,50,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(200,50,200,100),0)

            if MusicPaused == False:
                text_surface, rect = Fonts[1].render(("Mute Music"), (0, 0, 0))
                gameDisplay.blit(text_surface, (210, 80))
            else:
                text_surface, rect = Fonts[0].render(("Unmute Music"), (0, 0, 0))
                gameDisplay.blit(text_surface, (210, 86))


        pygame.display.flip()
        clock.tick(120)
