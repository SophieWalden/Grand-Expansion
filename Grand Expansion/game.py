try:
    import time, random, sys, os
except:
    print("Make sure to have the time module")
    sys.exit()
try:
    import pygame
except ImportError:
    print("Make sure you have python 3 and pygame.")
    sys.exit()
from pygame import freetype

#To do list:
#Add things that are made with magic

# Initialize the game engine
pygame.init()


DisplayWidth,DisplayHeight = 1000, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Grand Expansion")
font_23 = pygame.freetype.Font("Font.ttf", 23)
font_25 = pygame.freetype.Font("Font.ttf", 25)
font_30 = pygame.freetype.Font("Font.ttf", 30)
font_35 = pygame.freetype.Font("Font.ttf", 35)
font_40 = pygame.freetype.Font("Font.ttf", 40)
font_50 = pygame.freetype.Font("Font.ttf", 50)
font_75 = pygame.freetype.Font("Font.ttf", 75)
font_150 = pygame.freetype.Font("Font.ttf", 150)

#Loading the images

def load_images(path_to_directory):
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                img = pygame.image.load(os.path.join(dirpath, name)).convert()
                images[key] = img
    return images

global Images

Images = load_images("Images")

pygame.mixer.music.load('Sounds/Soundtrack.wav')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
global MusicPaused
MusicPaused = False

def shorten(Num):
    count = 0
    let = ""

    while Num >= 1000:
        Num /= 1000
        count += 1

    Num = str(Num)

    Num2 = ""

    if count >= 1:
        for i in range(Num.index(".")+2):
            Num2 += Num[i]

        Num = Num2

    if count == 1:
        Num += "K"
    if count == 2:
        Num += "M"
    if count == 3:
        Num += "B"
    if count == 4:
        Num += "T"

    

    return Num


def Achviement(Achviements):
    global ResourceCount, MaterialProduction, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked, Count

    count = 0
    for Quest in Achviements:
        if count == 0:
            if Quest["wood"] <= MaterialsEarned["Wood"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                UnUpgradable.pop(UnUpgradable.index("Grass"))
                UnUpgradable.append("CityFac")
                UnUpgradable.append("City")
                UnUpgradable.append("CityFar")
                UpgradeInfo["Grass"] = ["50 Wood","20 Stones","0 Food","1 Food"]
        if count == 1:
            if Quest["food"] <= MaterialsEarned["Food"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                UnUpgradable.pop(UnUpgradable.index("CityFac"))
                UnUpgradable.pop(UnUpgradable.index("CityFar"))

                UnUpgradable.append("Factory")
                UnUpgradable.append("Farm")
                UpgradeInfo["CityFar"] = ["100 Wood","50 food","1 Food","3 Food"]
                UpgradeInfo["CityFac"] = ["50 stones","1 food per second","1 Food","1 Metal"]
        if count == 2:
            if Quest["metal"] <= MaterialsEarned["Metal"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                UnUpgradable.pop(UnUpgradable.index("Water"))
                UnUpgradable.append("Dam")
                UpgradeInfo["Water"] = ["200 Wood","50 metal","0 Electricity","1 Electricity"]
        if count == 3:
            if Quest["Electricity"] <= MaterialsEarned["Electricity"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                UnUpgradable.pop(UnUpgradable.index("Forest Lv3"))
                UnUpgradable.append("Forest Lv4")
                UnUpgradable.pop(UnUpgradable.index("Quarry Lv3"))
                UnUpgradable.append("Quarry Lv4")
                UpgradeInfo["Forest Lv3"] = ["100 Metal","1 Electricity per second","5 wood","15 wood"]
                UpgradeInfo["Quarry Lv3"] = ["150 Metal","1 Electricity per second","5 stones","15 stones"]
        if count == 4:
            if Count["Forest Lv4"] > 0 or Count["Quarry Lv4"] > 0:
                if Quest["Finished"] == False:
                    Quest["Finished"] = True
                    Quest["Show Cooldown"] = 10
                    UnUpgradable.pop(UnUpgradable.index("Factory"))
                    UnUpgradable.append("Super Factories")
                    UpgradeInfo["Super Factories"] = ["100 Metal", "2 Electricity per second", "1 metal","5 Metal"]
        count += 1


    return Achviements


def menu(board,selection):
    global ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked, Count

    #Drawing Menu
    pygame.draw.line(gameDisplay,(50,50,50),(0,160),(1000,160),5)
    pygame.draw.line(gameDisplay,(50,50,50),(250,160),(250,0),5)
    pygame.draw.line(gameDisplay,(50,50,50),(500,160),(500,0),5)
    pygame.draw.line(gameDisplay,(50,50,50),(750,160),(750,0),5)
    pygame.draw.line(gameDisplay,(50,50,50),(0,80),(1000,80),5)

    pos = pygame.mouse.get_pos()
                    

    #Displaying Values for each Item

    #Wood
    pygame.draw.rect(gameDisplay,(165,42,42),(5,15,50,50),0)
    text_surface, rect = font_50.render(("Wood: "), (0, 0, 0))
    gameDisplay.blit(text_surface, (60, 20))
    text_surface, rect = font_35.render((shorten(ResourceCount["Wood"])), (0, 0, 0))
    gameDisplay.blit(text_surface, (160, 30))

    #Stones
    if MaterialsEarned["Stones"] >= 1:
        pygame.draw.rect(gameDisplay,(50,50,50),(5,95,50,50),0)
        text_surface, rect = font_50.render(("Stones: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (60, 100))
        text_surface, rect = font_30.render((shorten(ResourceCount["Stones"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (182, 113))

    #Food:
    if MaterialsEarned["Food"] >= 1:
        pygame.draw.rect(gameDisplay,(228,217,111),(255,15,50,50),0)
        text_surface, rect = font_50.render(("Food: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (310, 20))
        text_surface, rect = font_35.render((shorten(ResourceCount["Food"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (400, 30))

    #Metal
    if MaterialsEarned["Metal"] >= 1:
        pygame.draw.rect(gameDisplay,(125,125,125),(255,95,50,50),0)
        text_surface, rect = font_50.render(("Metal: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (310, 100))
        text_surface, rect = font_35.render((shorten(ResourceCount["Metal"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (420, 110))

    #Electricity
    if UnUpgradable[0] != "Water":
        pygame.draw.rect(gameDisplay,(255,255,0),(505,15,50,50),0)
        text_surface, rect = font_30.render(("Electricity: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (560, 30))
        text_surface, rect = font_35.render((shorten(ResourceCount["Electricity"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (680, 27))
        
    if selection != [-1,-1]:
        if board[selection[1]][selection[0]] == "Dam":
            text_surface, rect = font_75.render(("Waterwheel"), (0, 0, 0))
            gameDisplay.blit(text_surface, (665, 175))
        if board[selection[1]][selection[0]] == "Grass":
            text_surface, rect = font_75.render(("Grass"), (0, 0, 0))
            gameDisplay.blit(text_surface, (750, 175))
        if board[selection[1]][selection[0]] == "Water":
            text_surface, rect = font_75.render(("Water"), (0, 0, 0))
            gameDisplay.blit(text_surface, (750, 175))
        if board[selection[1]][selection[0]] == "Forest Lv1" or board[selection[1]][selection[0]] == "Forest Lv2" or board[selection[1]][selection[0]] == "Forest Lv3":
            text_surface, rect = font_75.render(("Forest"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))
        if board[selection[1]][selection[0]] == "Quarry Lv1" or board[selection[1]][selection[0]] == "Quarry Lv2" or board[selection[1]][selection[0]] == "Quarry Lv3":
            text_surface, rect = font_75.render(("Quarry"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))
        if board[selection[1]][selection[0]] == "City":
            text_surface, rect = font_75.render(("Upgrade Path"), (0, 0, 0))
            gameDisplay.blit(text_surface, (660, 175))
        if board[selection[1]][selection[0]] == "CityFac" or board[selection[1]][selection[0]] == "CityFar":
            text_surface, rect = font_75.render(("City"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))
        if board[selection[1]][selection[0]] == "Factory":
            text_surface, rect = font_75.render(("Factory"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))


        #Button for upgrading
        if board[selection[1]][selection[0]] != "City":
            stop = False
            for item in UnUpgradable:
                if item == board[selection[1]][selection[0]]:
                    stop = True
            if stop == False:
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                    pygame.draw.rect(gameDisplay,(150,0,0),(725,550,200,100),0)
                else:
                    pygame.draw.rect(gameDisplay,(255,0,0),(725,550,200,100),0)
                
                text_surface, rect = font_50.render(("Upgrade"), (0, 0, 0))
                gameDisplay.blit(text_surface, (760, 575))

            
                text_surface, rect = font_50.render(("Current Production: "), (0, 0, 0))
                gameDisplay.blit(text_surface, (650, 250))
                if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                    text_surface, rect = font_50.render((str(UpgradeInfo[board[selection[1]][selection[0]]][1])), (0, 0, 0))
                else:
                    text_surface, rect = font_50.render((str(UpgradeInfo[board[selection[1]][selection[0]]][2])), (0, 0, 0))
                if board[selection[1]][selection[0]] != "Water":
                    gameDisplay.blit(text_surface, (750, 325))
                else:
                    gameDisplay.blit(text_surface, (730, 325))

                pygame.draw.line(gameDisplay,(50,50,50),(640,400),(1000,400),5)
                if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                    text_surface, rect = font_50.render(("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][2])), (0, 0, 0))
                    gameDisplay.blit(text_surface, (670, 450))
                else:
                    if board[selection[1]][selection[0]] != "Water":
                        text_surface, rect = font_50.render(("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][3])), (0, 0, 0))
                    else:
                        text_surface, rect = font_40.render(("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][3])), (0, 0, 0))

                    if board[selection[1]][selection[0]] != "CityFac":
                        gameDisplay.blit(text_surface, (660, 410))
                    else:
                        gameDisplay.blit(text_surface, (670, 410))

                       
                if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                    text_surface, rect = font_50.render(("Cost: " + str(UpgradeInfo[board[selection[1]][selection[0]]][0])), (0, 0, 0))
                    gameDisplay.blit(text_surface, (710, 500))
                else:
                    text_surface, rect = font_50.render(("Cost: " + str(UpgradeInfo[board[selection[1]][selection[0]]][0])), (0, 0, 0))
                    if board[selection[1]][selection[0]] != "CityFac":
                        gameDisplay.blit(text_surface, (710, 450))
                    else:
                        gameDisplay.blit(text_surface, (700, 450))
                    text_surface, rect = font_50.render((str(UpgradeInfo[board[selection[1]][selection[0]]][1])), (0, 0, 0))
                    if board[selection[1]][selection[0]] != "CityFac":
                        gameDisplay.blit(text_surface, (740, 500))
                    else:
                        gameDisplay.blit(text_surface, (680, 500))
        else:
            if board[selection[1]][selection[0]] == "City":
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                    pygame.draw.rect(gameDisplay,(150,0,0),(725,550,200,100),0)
                else:
                    pygame.draw.rect(gameDisplay,(255,0,0),(725,550,200,100),0)
                
                text_surface, rect = font_50.render(("Factory"), (0, 0, 0))
                gameDisplay.blit(text_surface, (760, 575))

                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 350 and pos[1] <= 450:
                    pygame.draw.rect(gameDisplay,(150,0,0),(725,350,200,100),0)
                else:
                    pygame.draw.rect(gameDisplay,(255,0,0),(725,350,200,100),0)
                
                text_surface, rect = font_50.render(("Farm"), (0, 0, 0))
                gameDisplay.blit(text_surface, (780, 375))
            

        


    #Adding all the things produced
    if time.process_time() - Cooldown >= 1:
        for Item in ResourceCount:
            if Item != "Metal":
                ResourceCount[Item] += MaterialProduction[Item]
                MaterialsEarned[Item] += MaterialProduction[Item]
            else:
                if ResourceCount["Food"] >= MaterialProduction[Item]:
                    ResourceCount[Item] += MaterialProduction[Item]
                    MaterialsEarned[Item] += MaterialProduction[Item]
                    ResourceCount["Food"] -= MaterialProduction[Item]
                else:
                    ResourceCount[Item] += ResourceCount["Food"]
                    MaterialsEarned[Item] += ResourceCount["Food"]
                    ResourceCount["Food"] -= ResourceCount["Food"]
        if Count["Forest Lv4"] >= 1 and ResourceCount["Electricity"] > 0:
            if ResourceCount["Electricity"] >= Count["Forest Lv4"]:
                ResourceCount["Electricity"] -= Count["Forest Lv4"]
            else:
                num = Count["Forest Lv4"] - ResourceCount["Electricity"]
                ResourceCount["Wood"] -= 15 * num
                ResourceCount["Electricity"] = 0 
        if Count["Quarry Lv4"] >= 1 and ResourceCount["Electricity"] > 0:
            if ResourceCount["Electricity"] >= Count["Quarry Lv4"]:
                ResourceCount["Electricity"] -= Count["Quarry Lv4"]
            else:
                num = Count["Quarry Lv4"] - ResourceCount["Electricity"]
                ResourceCount["Stones"] -= 15 * num
                ResourceCount["Electricity"] = 0 
                
        Cooldown = time.process_time()
        

    #Drawing Menu options
    pygame.draw.line(gameDisplay,(50,50,50),(640,675),(1000,675),5)

    #Restart
    if pos[0] >= 650 and pos[0] <= 800 and pos[1] >= 685 and pos[1] <= 735:
        pygame.draw.rect(gameDisplay,(100,100,100),(650,685,150,50),0)
    else:
        pygame.draw.rect(gameDisplay,(150,150,150),(650,685,150,50),0)
    pygame.draw.rect(gameDisplay,(50,50,50),(650,685,150,50),3)
    text_surface, rect = font_35.render(("Restart"), (0, 0, 0))
    gameDisplay.blit(text_surface, (680, 700))

    #Demolish Building
    if pos[0] >= 825 and pos[0] <= 975 and pos[1] >= 685 and pos[1] <= 735:
        pygame.draw.rect(gameDisplay,(100,100,100),(825,685,150,50),0)
    else:
        pygame.draw.rect(gameDisplay,(150,150,150),(825,685,150,50),0)
    pygame.draw.rect(gameDisplay,(50,50,50),(825,685,150,50),3)
    text_surface, rect = font_23.render(("Demolish Building"), (0, 0, 0))
    gameDisplay.blit(text_surface, (832.5, 705))


    #Menu Upgrades(Finishing the game)

    if selection == [-1,-1]:
        text_surface, rect = font_75.render(("Finish Game"), (0, 0, 0))
        gameDisplay.blit(text_surface, (670, 180))
        text_surface, rect = font_50.render(("Cost: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (770, 240))
        text_surface, rect = font_50.render(("1k wood"), (0, 0, 0))
        gameDisplay.blit(text_surface, (750, 280))
        text_surface, rect = font_50.render(("500 stones"), (0, 0, 0))
        gameDisplay.blit(text_surface, (730, 320))
        text_surface, rect = font_50.render(("200 Food"), (0, 0, 0))
        gameDisplay.blit(text_surface, (740, 360))
        text_surface, rect = font_50.render(("100 metal"), (0, 0, 0))
        gameDisplay.blit(text_surface, (740, 400))
        text_surface, rect = font_50.render(("50 electricity"), (0, 0, 0))
        gameDisplay.blit(text_surface, (710, 440))

        if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
            pygame.draw.rect(gameDisplay,(150,0,0),(725,550,200,100),0)
        else:
            pygame.draw.rect(gameDisplay,(255,0,0),(725,550,200,100),0)

        text_surface, rect = font_50.render(("Unlock"), (0, 0, 0))
        gameDisplay.blit(text_surface, (760, 567))





    return board
    

def draw(x,y,Obj,Type,height,width):
    global AnimationStage, MaterialProduction, Count, Images
    if Obj == "Tile":
        if Type == "Grass":
            pygame.draw.rect(gameDisplay,(0,128,0),(x,y,(640/width),(640/height)),0)
        if Type == "Water":
            if AnimationStage["Water"][0] == 1:
                gameDisplay.blit(Images["Water1"],(x,y))
            if AnimationStage["Water"][0] == 2:
                gameDisplay.blit(Images["Water2"],(x,y))
            if AnimationStage["Water"][0] == 3:
                gameDisplay.blit(Images["Water3"],(x,y))

            if AnimationStage["Water"][1] <= 0:
                AnimationStage["Water"][0] += 1
                AnimationStage["Water"][1] = 0.5
                if AnimationStage["Water"][0] == 4:
                    AnimationStage["Water"][0] = 1
            else:
                AnimationStage["Water"][1] -= 0.025/Count["Water"]

        if Type == "Dam":
            if AnimationStage["Dam"][0] == 1:
                gameDisplay.blit(Images["Dam1"],(x,y))
            if AnimationStage["Dam"][0] == 2:
                gameDisplay.blit(Images["Dam2"],(x,y))
            if AnimationStage["Dam"][1] <= 0:
                AnimationStage["Dam"][0] += 1
                AnimationStage["Dam"][1] = 0.5
                if AnimationStage["Dam"][0] == 3:
                    AnimationStage["Dam"][0] = 1
            else:
                AnimationStage["Dam"][1] -= 0.05/Count["Dam"]
            
        if Type == "Quarry Lv1":
            gameDisplay.blit(Images["Quarry1"],(x,y))
        if Type == "Quarry Lv2":
            gameDisplay.blit(Images["Quarry2"],(x,y))
        if Type == "Quarry Lv3":
            gameDisplay.blit(Images["Quarry3"],(x,y))
        if Type == "Quarry Lv4":
            gameDisplay.blit(Images["Quarry4"],(x,y))
        if Type == "Forest Lv4":
            gameDisplay.blit(Images["Forest4"],(x,y))
        if Type == "Forest Lv3":
            gameDisplay.blit(Images["Forest3"],(x,y))
        if Type == "Forest Lv1":
            gameDisplay.blit(Images["Forest1"],(x,y))
        if Type == "Forest Lv2":
            gameDisplay.blit(Images["Forest2"],(x,y))
        if Type.find("City") != -1:
            gameDisplay.blit(Images["City"],(x,y))
        if Type == "Factory":
            gameDisplay.blit(Images["Factory"],(x,y))
        if Type == "Farm":
            gameDisplay.blit(Images["Farm"],(x,y))

        pygame.draw.rect(gameDisplay,(50,50,50),(x,y,(640/width),(640/height)),1)

        
            
            
            
    if Obj == "Selection":
        pygame.draw.rect(gameDisplay,(50,205,50),(x,y,(640/width),(640/height)),5)
    

def gen_Board(board,height,width):
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

def MainMenu(time):
    global MusicPaused
    run = True
    screen = "Main"

    while run == True:

        gameDisplay.fill((0,100,255))
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 400 and pos[0] <= 600 and pos[1] >= 600 and pos[1] <= 700 and screen == "Main":
                    game_loop()
                if pos[0] >= 625 and pos[0] <= 825 and pos[1] >= 600 and pos[1] <= 700 and screen == "Main":
                    screen = "Options"
                if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775 and screen == "Options":
                    screen = "Main"
                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 50 and pos[1] <= 150 and screen == "Options":
                    if MusicPaused == False:
                        MusicPaused = True
                        pygame.mixer.music.pause()
                    else:
                        MusicPaused = False
                        pygame.mixer.music.unpause()

        if screen == "Main":
            text_surface, rect = font_150.render(("Grand Expansion"), (0, 0, 0))
            gameDisplay.blit(text_surface, (85, 50))

            if time != 0:
                text_surface, rect = font_75.render(("Time: " + str(time)), (0, 0, 0))
                gameDisplay.blit(text_surface, (380, 300))


            if pos[0] >= 400 and pos[0] <= 600 and pos[1] >= 600 and pos[1] <= 700:
                pygame.draw.rect(gameDisplay,(150,0,0),(400,600,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(400,600,200,100),0)

            text_surface, rect = font_50.render(("Play"), (0, 0, 0))
            gameDisplay.blit(text_surface, (460, 630))

            if pos[0] >= 625 and pos[0] <= 825 and pos[1] >= 600 and pos[1] <= 700:
                pygame.draw.rect(gameDisplay,(150,0,0),(625,600,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(625,600,200,100),0)

            text_surface, rect = font_50.render(("Options"), (0, 0, 0))
            gameDisplay.blit(text_surface, (670, 630))
        if screen == "Options":
            if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775:
                pygame.draw.rect(gameDisplay,(150,0,0),(775,675,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(775,675,200,100),0)

            text_surface, rect = font_50.render(("Exit"), (0, 0, 0))
            gameDisplay.blit(text_surface, (835, 705))

            if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 50 and pos[1] <= 150:
                pygame.draw.rect(gameDisplay,(150,0,0),(200,50,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(200,50,200,100),0)

            if MusicPaused == False:
                text_surface, rect = font_50.render(("Mute Music"), (0, 0, 0))
                gameDisplay.blit(text_surface, (210, 80))
            else:
                text_surface, rect = font_40.render(("Unmute Music"), (0, 0, 0))
                gameDisplay.blit(text_surface, (210, 86))
        

        pygame.display.flip()
        clock.tick(60)
        

def game_loop():
    global ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, AnimationStage, Count
    
    game_run = True
    height = 8
    width = 8
    board = gen_Board([[0] * height for _ in range(width)],height,width)
    CurSelection = [-1,-1]
    ResourceCount = {"Wood": 10, "Stones": 0,"Food": 0,"Metal": 0,"Electricity": 0}
    MaterialProduction = {"Wood": 200, "Stones": 200,"Food": 200,"Metal": 100,"Electricity": 200}
    MaterialsEarned = {"Wood": 0, "Stones": 0,"Food": 0,"Metal": 0,"Electricity": 0}
    Cooldown = time.process_time()
    UnUpgradable = ["Water","Grass","Quarry Lv3","Forest Lv3"]
    UpgradeInfo = {"Map Upgrades": [],"Forest Lv1":["10 wood","0 wood","1 wood"],"Quarry Lv1":["15 wood","0 stones", "1 stones"],"Forest Lv2":["40 wood","1 wood","5 wood"],"Quarry Lv2":["45 wood","20 stones","1 stones", "5 stones"]}
    Achievments = [{"Name": "Beginner","Description":"You gathered 100 wood","Reward":"Unlocked cities","wood": 100,"Finished": False,"Show Cooldown": 0}
                   ,{"Name": "Food Man","Description":"You gathered 50 food","Reward":"Unlocked Factories","wood": 300,"stones":100,"food":50,"Finished": False,"Show Cooldown": 0}
                   ,{"Name": "Heavy Metal","Description":"You made 100 metal","Reward":"Unlocked Electricity","metal": 100,"Finished": False,"Show Cooldown": 0}
                   ,{"Name": "Shocking","Description":"You produced 100 Electricity","Reward": "Unlocked Electric Upgrades","Electricity": 100,"Finished": False,"Show Cooldown": 0}
                   ,{"Name": "Fast Materials","Description":"You got a Lvl4 Upgrade","Reward": "Unlocked Upgraded Factories","Finished": False,"Show Cooldown": 0}]
    ConfirmMessage = ""
    Confirming = False
    PreviousPos = [0,0]
    MenuClicking = False
    AnimationStage = {"Water": [1,0.5],"Dam": [1,0.5]}
    Count = {"Water": 0,"Dam": 0}
    StartTime = time.process_time()
    hour = 0
    seconds = 0
    minutes = 0


    while game_run == True:

        gameDisplay.fill((150,150,150))
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Confirming == False:
                    xPos = int(pos[0]/(10 * width))
                    yPos = int(pos[1]/(10 * height)) - 2
                if xPos >= 8:
                    xPos = PreviousPos[0]
                    yPos = PreviousPos[1]
                    MenuClicking = True
                if yPos < 0:
                    xPos = PreviousPos[0]
                    yPos = PreviousPos[1]
                    MenuClicking = True
                PreviousPos = [xPos,yPos]
                

                #Yes or no for Demolishing Buildings
                if pos[0] >= 570 and pos[0] <= 670 and pos[1] >= 400 and pos[1] <= 450 and Confirming == True:
                    Confirming = False

                if pos[0] >= 320 and pos[0] <= 420 and pos[1] >= 400 and pos[1] <= 450 and Confirming == True:
                    if board[yPos][xPos].find("Forest") != -1:
                        if board[yPos][xPos].find("2") != -1:
                            MaterialProduction["Wood"] -= 1
                        if board[yPos][xPos].find("3") != -1:
                            MaterialProduction["Wood"] -= 5
                        if board[yPos][xPos].find("4") != -1:
                            MaterialProduction["Wood"] -= 15
                        board[yPos][xPos] = "Forest Lv1"
                    if board[yPos][xPos].find("Quarry") != -1:
                        if board[yPos][xPos].find("2") != -1:
                            MaterialProduction["Stones"] -= 1
                        if board[yPos][xPos].find("3") != -1:
                            MaterialProduction["Stones"] -= 5
                        if board[yPos][xPos].find("4") != -1:
                            MaterialProduction["Stones"] -= 15
                        board[yPos][xPos] = "Quarry Lv1"
                    if board[yPos][xPos].find("City") != -1 or board[yPos][xPos].find("Factory") != -1:
                        if board[yPos][xPos].find("City") != -1:
                            MaterialProduction["Food"] -= 1
                        if board[yPos][xPos].find("Factory") != -1:
                            MaterialProduction["Metal"] -= 1
                        board[yPos][xPos] = "Grass"
                    Confirming = False

                if xPos <= 7 and yPos >= 0 and MenuClicking == False:
                    if CurSelection == [-1,-1] or CurSelection != [xPos,yPos]:
                        CurSelection = [xPos,yPos]
                    else:
                        CurSelection = [-1,-1]
                else:
                    MenuClicking = False

                #Restarts the game
                if pos[0] >= 650 and pos[0] <= 800 and pos[1] >= 685 and pos[1] <= 735:
                    game_loop()

                #Demolishes Selected Building
                if pos[0] >= 825 and pos[0] <= 975 and pos[1] >= 685 and pos[1] <= 735 and CurSelection != [-1,-1]:
                    Confirming = True
                    ConfirmMessage = "Are you sure you want to demolish the building?"
                        
                #Upgrading
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650 and CurSelection != [-1,-1]:
                    if board[CurSelection[1]][CurSelection[0]] == "Forest Lv3" and ResourceCount["Metal"] >= 100 and ResourceCount["Electricity"] >= 1:
                       ResourceCount["Metal"] -= 100
                       MaterialProduction["Wood"] += 10
                       board[CurSelection[1]][CurSelection[0]] = "Forest Lv4"

                    if board[CurSelection[1]][CurSelection[0]] == "Forest Lv2" and ResourceCount["Wood"] >= 40:
                        ResourceCount["Wood"] -= 40
                        MaterialProduction["Wood"] += 4
                        board[CurSelection[1]][CurSelection[0]] = "Forest Lv3"
                    if board[CurSelection[1]][CurSelection[0]] == "Forest Lv1" and ResourceCount["Wood"] >= 10:
                        ResourceCount["Wood"] -= 10
                        MaterialProduction["Wood"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "Forest Lv2"
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv3" and ResourceCount["Metal"] >= 150 and ResourceCount["Electricity"] >= 1:
                       ResourceCount["Metal"] -= 150
                       MaterialProduction["Stones"] += 10
                       board[CurSelection[1]][CurSelection[0]] = "Quarry Lv4"
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv2" and ResourceCount["Wood"] >= 45 and ResourceCount["Stones"] >= 20:
                       ResourceCount["Wood"] -= 45
                       ResourceCount["Stones"] -= 20
                       MaterialProduction["Stones"] += 3
                       board[CurSelection[1]][CurSelection[0]] = "Quarry Lv3"
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv1" and ResourceCount["Wood"] >= 15:
                        ResourceCount["Wood"] -= 15
                        MaterialProduction["Stones"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "Quarry Lv2"
                    if board[CurSelection[1]][CurSelection[0]] == "CityFac" and ResourceCount["Food"] >= 1 and ResourceCount["Stones"] >= 50 and Achievments[1]["Finished"] == True:
                        ResourceCount["Stones"] -= 50
                        MaterialProduction["Metal"] += 1
                        MaterialProduction["Food"] -= 1
                        board[CurSelection[1]][CurSelection[0]] = "Factory"
                    if board[CurSelection[1]][CurSelection[0]] == "City" and pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650: 
                        board[CurSelection[1]][CurSelection[0]] = "CityFac"
                    if board[CurSelection[1]][CurSelection[0]] == "CityFar" and ResourceCount["Wood"] >= 100 and ResourceCount["Food"] >= 50 and Achievments[1]["Finished"] == True:
                        ResourceCount["Wood"] -= 100
                        ResourceCount["Food"] -= 50
                        MaterialProduction["Food"] += 2
                        board[CurSelection[1]][CurSelection[0]] = "Farm"
                    if board[CurSelection[1]][CurSelection[0]] == "Grass" and ResourceCount["Wood"] >= 50 and ResourceCount["Stones"] >= 20 and UnUpgradable[1] != "Grass":
                        ResourceCount["Wood"] -= 50
                        ResourceCount["Stones"] -= 20
                        MaterialProduction["Food"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "City"
                    if board[CurSelection[1]][CurSelection[0]] == "Water" and ResourceCount["Wood"] >= 200 and ResourceCount["Metal"] >= 50 and Achievments[2]["Finished"] == True:
                        ResourceCount["Wood"] -= 200
                        ResourceCount["Metal"] -= 50
                        MaterialProduction["Electricity"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "Dam"

                #Path Choices
                if board[CurSelection[1]][CurSelection[0]] == "City" and pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 350 and pos[1] <= 450:
                    board[CurSelection[1]][CurSelection[0]] = "CityFar"
                        

                if CurSelection == [-1,-1] and pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650 and ResourceCount["Wood"] >= 1000 and ResourceCount["Stones"] >= 500 and ResourceCount["Food"] >= 200 and ResourceCount["Metal"] >= 100 and ResourceCount["Electricity"] >= 50:
                    time2 = int((time.process_time() - StartTime))
                    hours = 0
                    minutes = 0
                    seconds = 0
                    while time2 >= 3600:
                        time2 -= 3600
                        hours += 1
                    while time2 >= 60:
                        time2 -= 60
                        minutes += 1
                    while time2 >= 1:
                        time2 -= 1
                        seconds += 1
                    if minutes < 10 and hours > 0:
                        minutes = "0" + str(minutes)
                    if seconds < 10 and minutes > 0:
                        seconds = "0" + str(seconds)
                    if hours != 0:
                        MainMenu(str(hours) + ":" + str(minutes) + ":" + str(seconds))
                    if minutes != 0:
                        MainMenu(str(minutes) + ":" + str(seconds))
                    else:
                        MainMenu(str(seconds))
    
        #Counting Tiles for certain animations
        Count = {"Water": 0,"Dam": 0,"Forest Lv4": 0,"Quarry Lv4": 0}
        for j in range(height):
            for i in range(width):
                if board[j][i] == "Water":
                    Count["Water"] += 1
                if board[j][i] == "Dam":
                    Count["Dam"] += 1
                if board[j][i] == "Forest Lv4":
                    Count["Forest Lv4"] += 1
                if board[j][i] == "Quarry Lv4":
                    Count["Quarry Lv4"] += 1

        #Drawing all Tiles
        for j in range(height):
            for i in range(width):
                draw(i * (640/width),j * (640/height) + 160,"Tile",board[j][i],height,width)

        #Drawing Selection
        if CurSelection != [-1,-1]:
            draw(CurSelection[0] * (640/width),CurSelection[1] * (640/height) + 160,"Selection","Green",height,width)


        #Drawing the menu w/ cost and prices
        board = menu(board,CurSelection)

        #Achvievment Check
        Achviement(Achievments)

        #Display the Achievement
        for quest in Achievments:
            if quest["Show Cooldown"] > 0:
                quest["Show Cooldown"] -= 0.1
                pygame.draw.rect(gameDisplay,(200,200,200),(300,700,400,100),0)
                pygame.draw.rect(gameDisplay,(25,25,25),(300,700,400,100),5)
                text_surface, rect = font_50.render((quest["Name"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 710))
                text_surface, rect = font_25.render((quest["Description"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 750))
                text_surface, rect = font_25.render((quest["Reward"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 775))


        #Shows a confirm message
        if Confirming == True:
            pygame.draw.rect(gameDisplay,(150,150,150),(300,300,400,200),0)
            pygame.draw.rect(gameDisplay,(50,50,50),(300,300,400,200),5)
            text_surface, rect = font_23.render((ConfirmMessage), (0, 0, 0))
            gameDisplay.blit(text_surface, (315, 350))

            if pos[0] >= 320 and pos[0] <= 420 and pos[1] >= 400 and pos[1] <= 450:
                pygame.draw.rect(gameDisplay,(0,100,0),(320,400,100,50),0)
            else:
                pygame.draw.rect(gameDisplay,(0,150,0),(320,400,100,50),0)

            pygame.draw.rect(gameDisplay,(0,200,0),(320,400,100,50),3)

            if pos[0] >= 570 and pos[0] <= 670 and pos[1] >= 400 and pos[1] <= 450:
                pygame.draw.rect(gameDisplay,(100,0,0),(570,400,100,50),0)
            else:
                pygame.draw.rect(gameDisplay,(150,0,0),(570,400,100,50),0)

            text_surface, rect = font_23.render(("Yes"), (0, 0, 0))
            gameDisplay.blit(text_surface, (355, 415))
            text_surface, rect = font_23.render(("No"), (0, 0, 0))
            gameDisplay.blit(text_surface, (610, 415))

            pygame.draw.rect(gameDisplay,(200,0,0),(570,400,100,50),3)
                
                

        pygame.display.flip()
        clock.tick(60)



MainMenu(0)
