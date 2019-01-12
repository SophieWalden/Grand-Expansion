try:
    import pygame
except ImportError:
    print("Make sure you have python 3 and pygame.")
    sys.exit()
try:
    import time, random, sys
except:
    print("Make sure to have the time module")
    sys.exit()
from pygame import freetype

#game_font = pygame.freetype.Font("Font.ttf", 75)
#text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
#gameDisplay.blit(text_surface, (150, 300))

#To do list:
#Add things that are made with magic

# Initialize the game engine
pygame.init()



DisplayWidth,DisplayHeight = 1000, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Grand Expansion")


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
    global ResourceCount, MaterialProduction, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked

    count = 0
    for Quest in Achviements:
        if count == 0:
            if Quest["wood"] <= MaterialsEarned["Wood"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                UnUpgradable.pop(UnUpgradable.index("Grass"))
                UnUpgradable.append("City")
                UpgradeInfo["Grass"] = ["50 Wood","20 Stones","0 Food","1 Food"]
        if count == 1:
            if Quest["wood"] <= MaterialsEarned["Wood"] and Quest["stones"] <= MaterialsEarned["Stones"] and Quest["food"] <= MaterialsEarned["Food"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                UnUpgradable.pop(UnUpgradable.index("City"))
                UnUpgradable.append("Factories")
                UpgradeInfo["Factory"] = ["200 Wood","75 Stones","25 Food","1 Metal"]
        count += 1


    return Achviements


def menu(board,selection):
    global ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked

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
    game_font = pygame.freetype.Font("Font.ttf", 50)
    text_surface, rect = game_font.render(("Wood: "), (0, 0, 0))
    gameDisplay.blit(text_surface, (60, 20))
    game_font = pygame.freetype.Font("Font.ttf", 35)
    text_surface, rect = game_font.render((shorten(ResourceCount["Wood"])), (0, 0, 0))
    gameDisplay.blit(text_surface, (160, 30))

    #Stones
    if MaterialsEarned["Stones"] >= 1:
        pygame.draw.rect(gameDisplay,(50,50,50),(5,95,50,50),0)
        game_font = pygame.freetype.Font("Font.ttf", 50)
        text_surface, rect = game_font.render(("Stones: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (60, 100))
        game_font = pygame.freetype.Font("Font.ttf", 35)
        text_surface, rect = game_font.render((shorten(ResourceCount["Stones"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (190, 110))

    #Food:
    if MaterialsEarned["Food"] >= 1:
        pygame.draw.rect(gameDisplay,(228,217,111),(255,15,50,50),0)
        game_font = pygame.freetype.Font("Font.ttf", 50)
        text_surface, rect = game_font.render(("Food: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (310, 20))
        game_font = pygame.freetype.Font("Font.ttf", 35)
        text_surface, rect = game_font.render((shorten(ResourceCount["Food"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (400, 30))

    #Metal
    if MaterialsEarned["Metal"] >= 1:
        pygame.draw.rect(gameDisplay,(125,125,125),(255,95,50,50),0)
        game_font = pygame.freetype.Font("Font.ttf", 50)
        text_surface, rect = game_font.render(("Metal: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (310, 100))
        game_font = pygame.freetype.Font("Font.ttf", 35)
        text_surface, rect = game_font.render((shorten(ResourceCount["Metal"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (420, 110))

    #Magic
    if UpgradeInfo["Map Upgrades"][0][3] == True:
        pygame.draw.rect(gameDisplay,(228,217,111),(255,15,50,50),0)
        game_font = pygame.freetype.Font("Font.ttf", 50)
        text_surface, rect = game_font.render(("Mqtid: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (310, 20))
        game_font = pygame.freetype.Font("Font.ttf", 35)
        text_surface, rect = game_font.render((shorten(ResourceCount["Mqgic"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (400, 30))
        
    if selection != [-1,-1]:
        if board[selection[1]][selection[0]] == "Grass":
            game_font = pygame.freetype.Font("Font.ttf", 75)
            text_surface, rect = game_font.render(("Grass"), (0, 0, 0))
            gameDisplay.blit(text_surface, (750, 175))
        if board[selection[1]][selection[0]] == "Water":
            game_font = pygame.freetype.Font("Font.ttf", 75)
            text_surface, rect = game_font.render(("Water"), (0, 0, 0))
            gameDisplay.blit(text_surface, (750, 175))
        if board[selection[1]][selection[0]] == "Forest Lv1" or board[selection[1]][selection[0]] == "Forest Lv2" or board[selection[1]][selection[0]] == "Forest Lv3":
            game_font = pygame.freetype.Font("Font.ttf", 75)
            text_surface, rect = game_font.render(("Forest"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))
        if board[selection[1]][selection[0]] == "Quarry Lv1" or board[selection[1]][selection[0]] == "Quarry Lv2" or board[selection[1]][selection[0]] == "Quarry Lv3":
            game_font = pygame.freetype.Font("Font.ttf", 75)
            text_surface, rect = game_font.render(("Quarry"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))
        if board[selection[1]][selection[0]] == "City":
            game_font = pygame.freetype.Font("Font.ttf", 75)
            text_surface, rect = game_font.render(("City"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))
        if board[selection[1]][selection[0]] == "Factory":
            game_font = pygame.freetype.Font("Font.ttf", 75)
            text_surface, rect = game_font.render(("Factory"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))

        stop = False

        #Button for upgrading
        for item in UnUpgradable:
            if item == board[selection[1]][selection[0]]:
                stop = True
        if stop == False:
            if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                pygame.draw.rect(gameDisplay,(150,0,0),(725,550,200,100),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(725,550,200,100),0)
            
            game_font = pygame.freetype.Font("Font.ttf", 50)
            text_surface, rect = game_font.render(("Upgrade"), (0, 0, 0))
            gameDisplay.blit(text_surface, (760, 575))

            game_font = pygame.freetype.Font("Font.ttf", 50)
            text_surface, rect = game_font.render(("Current Production: "), (0, 0, 0))
            gameDisplay.blit(text_surface, (650, 250))
            if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                text_surface, rect = game_font.render((str(UpgradeInfo[board[selection[1]][selection[0]]][1])), (0, 0, 0))
            else:
                text_surface, rect = game_font.render((str(UpgradeInfo[board[selection[1]][selection[0]]][2])), (0, 0, 0))   
            gameDisplay.blit(text_surface, (750, 325))

            pygame.draw.line(gameDisplay,(50,50,50),(640,400),(1000,400),5)
            game_font = pygame.freetype.Font("Font.ttf", 50)
            if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                text_surface, rect = game_font.render(("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][2])), (0, 0, 0))
                gameDisplay.blit(text_surface, (670, 450))
            else:
                text_surface, rect = game_font.render(("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][3])), (0, 0, 0))
                if board[selection[1]][selection[0]] != "City":
                    gameDisplay.blit(text_surface, (660, 410))
                else:
                    gameDisplay.blit(text_surface, (670, 410))
                   
            if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                text_surface, rect = game_font.render(("Cost: " + str(UpgradeInfo[board[selection[1]][selection[0]]][0])), (0, 0, 0))
                gameDisplay.blit(text_surface, (710, 500))
            else:
                text_surface, rect = game_font.render(("Cost: " + str(UpgradeInfo[board[selection[1]][selection[0]]][0])), (0, 0, 0))
                if board[selection[1]][selection[0]] != "City":
                    gameDisplay.blit(text_surface, (710, 450))
                else:
                    gameDisplay.blit(text_surface, (700, 450))
                text_surface, rect = game_font.render((str(UpgradeInfo[board[selection[1]][selection[0]]][1])), (0, 0, 0))
                if board[selection[1]][selection[0]] != "City":
                    gameDisplay.blit(text_surface, (740, 500))
                else:
                    gameDisplay.blit(text_surface, (680, 500))

    else:

        pygame.draw.line(gameDisplay,(50,50,50),(640,425),(1000,425),5)

        #Unlocking Magic

        if UpgradeInfo["Map Upgrades"][0][3] == False:

            game_font = pygame.freetype.Font("Font.ttf", 35)
            text_surface, rect = game_font.render(("Unlock Electricity(Not ready)"), (0, 0, 0))
            gameDisplay.blit(text_surface, (645, 180))

            game_font = pygame.freetype.Font("Font.ttf", 35)
            text_surface, rect = game_font.render(("Cost: "), (0, 0, 0))
            gameDisplay.blit(text_surface, (785, 210))

            game_font = pygame.freetype.Font("Font.ttf", 35)
            text_surface, rect = game_font.render((UpgradeInfo["Map Upgrades"][0][0]), (0, 0, 0))
            gameDisplay.blit(text_surface, (760, 240))

            game_font = pygame.freetype.Font("Font.ttf", 35)
            text_surface, rect = game_font.render((UpgradeInfo["Map Upgrades"][0][1]), (0, 0, 0))
            gameDisplay.blit(text_surface, (755, 270))

            game_font = pygame.freetype.Font("Font.ttf", 35)
            text_surface, rect = game_font.render((UpgradeInfo["Map Upgrades"][0][2]), (0, 0, 0))
            gameDisplay.blit(text_surface, (770, 300))

            if pos[0] >= 745 and pos[0] <= 895 and pos[1] >= 345 and pos[1] <= 420:
                pygame.draw.rect(gameDisplay,(150,0,0),(745,345,150,75),0)
            else:
                pygame.draw.rect(gameDisplay,(255,0,0),(745,345,150,75),0)

            game_font = pygame.freetype.Font("Font.ttf", 35)
            text_surface, rect = game_font.render(("Unlock"), (0, 0, 0))
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
                
        Cooldown = time.process_time()
        

    #Drawing Menu options
    pygame.draw.line(gameDisplay,(50,50,50),(640,675),(1000,675),5)

    #Restart
    if pos[0] >= 650 and pos[0] <= 800 and pos[1] >= 685 and pos[1] <= 735:
        pygame.draw.rect(gameDisplay,(100,100,100),(650,685,150,50),0)
    else:
        pygame.draw.rect(gameDisplay,(150,150,150),(650,685,150,50),0)
    pygame.draw.rect(gameDisplay,(50,50,50),(650,685,150,50),3)
    game_font = pygame.freetype.Font("Font.ttf", 35)
    text_surface, rect = game_font.render(("Restart"), (0, 0, 0))
    gameDisplay.blit(text_surface, (680, 700))

    #Demolish Building
    if pos[0] >= 825 and pos[0] <= 975 and pos[1] >= 685 and pos[1] <= 735:
        pygame.draw.rect(gameDisplay,(100,100,100),(825,685,150,50),0)
    else:
        pygame.draw.rect(gameDisplay,(150,150,150),(825,685,150,50),0)
    pygame.draw.rect(gameDisplay,(50,50,50),(825,685,150,50),3)
    game_font = pygame.freetype.Font("Font.ttf", 23)
    text_surface, rect = game_font.render(("Demolish Building"), (0, 0, 0))
    gameDisplay.blit(text_surface, (832.5, 705))


    return board
    

def draw(x,y,Obj,Type,height,width):
    if Obj == "Tile":
        if Type == "Grass":
            pygame.draw.rect(gameDisplay,(0,128,0),(x,y,(640/width),(640/height)),0)
            pygame.draw.rect(gameDisplay,(50,50,50),(x,y,(640/width),(640/height)),1)
        if Type == "Water":
            pygame.draw.rect(gameDisplay,(50,50,250),(x,y,(640/width),(640/height)),0)
            pygame.draw.rect(gameDisplay,(50,50,50),(x,y,(640/width),(640/height)),1)
        if Type == "Quarry Lv1" or Type == "Quarry Lv2" or Type == "Quarry Lv3":
            pygame.draw.rect(gameDisplay,(75,75,75),(x,y,(640/width),(640/height)),0)
            pygame.draw.rect(gameDisplay,(50,50,50),(x,y,(640/width),(640/height)),1)
        if Type == "Forest Lv1" or Type == "Forest Lv2" or Type == "Forest Lv3":
            pygame.draw.rect(gameDisplay,(0,50,0),(x,y,(640/width),(640/height)),0)

            #Trees
            pygame.draw.rect(gameDisplay,(165,42,42),(x+8,y+40,5,10),0)
            pygame.draw.polygon(gameDisplay,(0,150,0),[(x+5,y+40),(x+15,y+40),(x+10,y+35)],0)
            pygame.draw.rect(gameDisplay,(165,42,42),(x+38,y+40,5,10),0)
            pygame.draw.polygon(gameDisplay,(0,150,0),[(x+35,y+40),(x+45,y+40),(x+40,y+35)],0)
            pygame.draw.rect(gameDisplay,(165,42,42),(x+23,y+20,5,10),0)
            pygame.draw.polygon(gameDisplay,(0,150,0),[(x+20,y+20),(x+30,y+20),(x+25,y+15)],0)
            pygame.draw.rect(gameDisplay,(165,42,42),(x+68,y+40,5,10),0)
            pygame.draw.polygon(gameDisplay,(0,150,0),[(x+65,y+40),(x+75,y+40),(x+70,y+35)],0)
            pygame.draw.rect(gameDisplay,(165,42,42),(x+53,y+20,5,10),0)
            pygame.draw.polygon(gameDisplay,(0,150,0),[(x+50,y+20),(x+60,y+20),(x+55,y+15)],0)
            
            pygame.draw.rect(gameDisplay,(50,50,50),(x,y,(640/width),(640/height)),1)
        if Type == "City":
            pygame.draw.rect(gameDisplay,(200,200,200),(x,y,(640/width),(640/height)),0)
            pygame.draw.rect(gameDisplay,(50,50,50),(x,y,(640/width),(640/height)),1)
        if Type == "Factory":
            pygame.draw.rect(gameDisplay,(225,225,225),(x,y,(640/width),(640/height)),0)
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

def Board_SizeUp(board,height,width,UpSize):
    pass

def game_loop():
    global ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned
    
    game_run = True
    height = 8
    width = 8
    board = gen_Board([[0] * height for _ in range(width)],height,width)
    CurSelection = [-1,-1]
    ResourceCount = {"Wood": 10, "Stones": 0,"Food": 0,"Metal": 0,"Electricity": 0}
    MaterialProduction = {"Wood": 0, "Stones": 0,"Food": 0,"Metal": 0,"Electricity": 0}
    MaterialsEarned = {"Wood": 0, "Stones": 0,"Food": 0,"Metal": 0,"Electricity": 0}
    Cooldown = time.process_time()
    UnUpgradable = ["Water","Grass","Quarry Lv3","Forest Lv3"]
    UpgradeInfo = {"Map Upgrades": [["300 wood","100 stones","50 food",False]],"City":["50 stones","1 food per second","1 food","1 metal"],"Forest Lv1":["10 wood","0 wood","1 wood"],"Quarry Lv1":["15 wood","0 stones", "1 stones"],"Forest Lv2":["40 wood","1 wood","5 wood"],"Quarry Lv2":["45 wood","20 stones","1 stones", "5 stones"]}
    Achievments = [{"Name": "Beginner","Description":"You gathered 100 wood","Reward":"Unlocked cities","wood": 100,"Finished": False,"Show Cooldown": 0}
                   ,{"Name": "Food Man","Description":"You gathered 50 food","Reward":"Unlocked Factories","wood": 300,"stones":100,"food":50,"Finished": False,"Show Cooldown": 0}]
    ConfirmMessage = ""
    Confirming = False
    PreviousPos = [0,0]
    MenuClicking = False


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
                        board[yPos][xPos] = "Forest Lv1"
                        if board[yPos][xPos].find("2") != -1:
                            MaterialProduction["Wood"] -= 1
                        if board[yPos][xPos].find("3") != -1:
                            MaterialProduction["Wood"] -= 5
                    if board[yPos][xPos].find("Quarry") != -1:
                        board[yPos][xPos] = "Quarry Lv1"
                        if board[yPos][xPos].find("2") != -1:
                            MaterialProduction["Stones"] -= 1
                        if board[yPos][xPos].find("2") != -1:
                            MaterialProduction["Stones"] -= 5
                    if board[yPos][xPos].find("City") != -1 or board[yPos][xPos].find("Factory") != -1:
                        board[yPos][xPos] = "Grass"
                        if board[yPos][xPos].find("City") != -1:
                            MaterialProduction["Food"] -= 1
                        if board[yPos][xPos].find("Factory") != -1:
                            MaterialProduction["Metal"] -= 1
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
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                    if board[CurSelection[1]][CurSelection[0]] == "Forest Lv2" and ResourceCount["Wood"] >= 40:
                        ResourceCount["Wood"] -= 40
                        MaterialProduction["Wood"] += 4
                        board[CurSelection[1]][CurSelection[0]] = "Forest Lv3"
                    if board[CurSelection[1]][CurSelection[0]] == "Forest Lv1" and ResourceCount["Wood"] >= 10:
                        ResourceCount["Wood"] -= 10
                        MaterialProduction["Wood"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "Forest Lv2"
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv2" and ResourceCount["Wood"] >= 45 and ResourceCount["Stones"] >= 20:
                       ResourceCount["Wood"] -= 45
                       ResourceCount["Stones"] -= 20
                       MaterialProduction["Stones"] += 3
                       board[CurSelection[1]][CurSelection[0]] = "Quarry Lv3"
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv1" and ResourceCount["Wood"] >= 15:
                        ResourceCount["Wood"] -= 15
                        MaterialProduction["Stones"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "Quarry Lv2"
                    if board[CurSelection[1]][CurSelection[0]] == "City" and ResourceCount["Food"] >= 1 and ResourceCount["Stones"] >= 50:
                        ResourceCount["Stones"] -= 50
                        MaterialProduction["Metal"] += 1
                        MaterialProduction["Food"] -= 1
                        board[CurSelection[1]][CurSelection[0]] = "Factory"
                        UnUpgradable.append("Factory")
                    if board[CurSelection[1]][CurSelection[0]] == "Grass" and ResourceCount["Wood"] >= 50 and ResourceCount["Stones"] >= 20 and UnUpgradable[1] != "Grass":
                        ResourceCount["Wood"] -= 50
                        ResourceCount["Stones"] -= 20
                        MaterialProduction["Food"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "City"

    

                #Map Upgrades
                if pos[0] >= 745 and pos[0] <= 895 and pos[1] >= 345 and pos[1] <= 420 and UpgradeInfo["Map Upgrades"][0][3] == False and ResourceCount["Wood"] >= 300 and ResourceCount["Stones"] >= 100 and ResourceCount["Food"] >= 50:
                    ResourceCount["Wood"] -= 300
                    ResourceCount["Stones"] -= 100
                    ResourceCount["Food"] -= 50
                    UpgradeInfo["Map Upgrades"][0][3] = True

        for j in range(height):
            for i in range(width):
                draw(i * (640/width),j * (640/height) + 160,"Tile",board[j][i],height,width)

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
                game_font = pygame.freetype.Font("Font.ttf", 50)
                text_surface, rect = game_font.render((quest["Name"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 710))
                game_font = pygame.freetype.Font("Font.ttf", 25)
                text_surface, rect = game_font.render((quest["Description"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 750))
                text_surface, rect = game_font.render((quest["Reward"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 775))


        #Shows a confirm message
        if Confirming == True:
            pygame.draw.rect(gameDisplay,(150,150,150),(300,300,400,200),0)
            pygame.draw.rect(gameDisplay,(50,50,50),(300,300,400,200),5)
            game_font = pygame.freetype.Font("Font.ttf", 23)
            text_surface, rect = game_font.render((ConfirmMessage), (0, 0, 0))
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

            text_surface, rect = game_font.render(("Yes"), (0, 0, 0))
            gameDisplay.blit(text_surface, (355, 415))
            text_surface, rect = game_font.render(("No"), (0, 0, 0))
            gameDisplay.blit(text_surface, (610, 415))

            pygame.draw.rect(gameDisplay,(200,0,0),(570,400,100,50),3)

            
                
                

        pygame.display.flip()
        clock.tick(60)



game_loop()
