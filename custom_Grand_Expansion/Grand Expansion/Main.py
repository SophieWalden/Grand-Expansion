from custom_source_modules import *

# Initialize the game engine
pygame.init()

DisplayWidth, DisplayHeight = 1000, 800
clock = pygame.time.Clock()

# Prestige Count
global PrestigeCount
PrestigeCount = 0
global MinerBought
MinerBought = False
global AscendCount
AscendCount = 0

# Making the window
gameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))
pygame.display.set_caption("Grand Expansion")

# Fonts
from fonts import *


# Loading the images
def load_images(path_to_directory, height, width):
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                img = pygame.image.load(os.path.join(dirpath, name)).convert()
                img = pygame.transform.scale(img, (int(640 / width), int(640 / height)))
                images[key] = img
    return images


# Multipliers for Prestige
global Mult
# Temp Multi
Mult = {"Wood": 6, "Stones": 6, "Food": 6, "Metal": 6, "Electricity": 6, "Prestige": 6, "Mandorium": 6}

# Map Level
global MapLevel
MapLevel = 2

# Plays the music
pygame.mixer.music.load('Sounds/ambient-guitar-x1-loop-mode.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
global MusicPaused
MusicPaused = False


# Shorten is a function that takes a number and shortens it while still keeping the value because of the use of letters
def shorten(Num):
    count = 0
    let = ""

    while Num >= 1000:
        Num /= 1000
        count += 1

    Num = str(Num)

    Num2 = ""

    if count >= 1:
        for i in range(Num.index(".") + 2):
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
    if count == 5:
        Num += "q"
    if count == 6:
        Num += "Q"
    if count == 7:
        Num += "s"
    if count == 8:
        Num += "S"

    return Num


# Checks for all the achviements
def Achviement(Achviements):
    global ResourceCount, MaterialProduction, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked, Count, PrestigeCount

    count = 0
    for Quest in Achviements:
        if count == 0:
            if Quest["wood"] <= MaterialsEarned["Wood"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(0)
        if count == 1:
            if Quest["food"] <= MaterialsEarned["Food"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(1)
        if count == 2:
            if Quest["metal"] <= MaterialsEarned["Metal"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(2)
        if count == 3:
            if Quest["Electricity"] <= MaterialsEarned["Electricity"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(3)
        if count == 4:
            if Count["Forest Lv4"] > 0 or Count["Quarry Lv4"] > 0:
                if Quest["Finished"] == False:
                    Quest["Finished"] = True
                    Quest["Show Cooldown"] = 10
                    AchievmentRewards(4)
        if count == 5:
            if Quest["Finished"] == False and ResourceCount["Food"] >= 200:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(5)
        if count == 6:
            if Quest["Finished"] == False and PrestigeCount >= 3:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
        count += 1

    return Achviements


def AchievmentRewards(Num):
    global ResourceCount, MaterialProduction, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked, Count

    if Num == 0:
        UnUpgradable.pop(UnUpgradable.index("Grass"))
        UnUpgradable.append("CityFac")
        UnUpgradable.append("City")
        UnUpgradable.append("Farm")
        UnUpgradable.append("CityFar")
        UpgradeInfo["Grass"] = ["50 Wood", "20 Stones", "0 Food", "1 Food"]
    if Num == 1:
        UnUpgradable.pop(UnUpgradable.index("CityFac"))
        UnUpgradable.pop(UnUpgradable.index("CityFar"))
        UnUpgradable.append("Farm")
        UnUpgradable.append("Factory Su")
        UnUpgradable.append("Factory")
        UnUpgradable.append("Factory So")
        UpgradeInfo["CityFar"] = ["100 Wood", "50 food", "1 Food", "10 Food"]
        UpgradeInfo["CityFac"] = ["50 stones", "-5 food per second", "-5 Food", "1 Metal"]
    if Num == 2:
        UnUpgradable.pop(UnUpgradable.index("Water Dam"))
        UnUpgradable.append("Dam")
        UpgradeInfo["Water Dam"] = ["200 Wood", "50 metal", "0 Electricity", "1 Electricity"]
    if Num == 3:
        UnUpgradable.pop(UnUpgradable.index("Forest Lv3"))
        UnUpgradable.append("Forest Lv4")
        UnUpgradable.pop(UnUpgradable.index("Quarry Lv3"))
        UnUpgradable.append("Quarry Lv4")
        UpgradeInfo["Forest Lv3"] = ["100 Metal", "1 Electricity per second", "5 wood", "15 wood"]
        UpgradeInfo["Quarry Lv3"] = ["150 Metal", "1 Electricity per second", "5 stones", "15 stones"]
    if Num == 4:
        UnUpgradable.pop(UnUpgradable.index("Factory So"))
        UnUpgradable.pop(UnUpgradable.index("Factory Su"))
        UnUpgradable.append("Super_Factory")
        UnUpgradable.append("Solar_Power")
        UpgradeInfo["Factory Su"] = ["100 Metal", "2 Electricity per second", "1 metal", "5 Metal"]
        UpgradeInfo["Factory So"] = ["100 Metal", "1 Food per second", "1 metal", "3 Electricity"]
    if Num == 5:
        UnUpgradable.pop(UnUpgradable.index("Water Fish"))
        UnUpgradable.append("Fisherman")
        UpgradeInfo["Water Fish"] = ["100 Wood", "25 metal", "0 Food", "2 Food"]


# Draws all the tiles
def draw(x, y, Obj, Type, height, width, Images, AnimationStage, Count):
    global MaterialProduction
    if Obj == "Tile":
        if Type == "Grass":
            pygame.draw.rect(gameDisplay, (0, 128, 0), (x, y, (640 / width), (640 / height)), 0)
        if Type.find("Water") != -1:
            # The Animation for water
            if AnimationStage["Water"][0] == 1:
                gameDisplay.blit(Images["Water1"], (x, y))
            if AnimationStage["Water"][0] == 2:
                gameDisplay.blit(Images["Water2"], (x, y))
            if AnimationStage["Water"][0] == 3:
                gameDisplay.blit(Images["Water3"], (x, y))

            if AnimationStage["Water"][1] <= 0:
                AnimationStage["Water"][0] += 1
                AnimationStage["Water"][1] = 0.5
                if AnimationStage["Water"][0] == 4:
                    AnimationStage["Water"][0] = 1
            else:
                AnimationStage["Water"][1] -= 0.025 / Count["Water"]




        if Type == "Dam":
            # The Animation for Dam
            if AnimationStage["Dam"][0] == 1:
                gameDisplay.blit(Images["Dam1"], (x, y))
            if AnimationStage["Dam"][0] == 2:
                gameDisplay.blit(Images["Dam2"], (x, y))
            if AnimationStage["Dam"][1] <= 0:
                AnimationStage["Dam"][0] += 1
                AnimationStage["Dam"][1] = random.randint(800, 1000)  # random vara for dam to open/close
                if AnimationStage["Dam"][0] == 3:
                    AnimationStage["Dam"][0] = 1
            else:
                AnimationStage["Dam"][1] -= 10 / Count["Dam"]

        if Type == "Fisherman":
            if AnimationStage["Fisherman"][0] == 1:
                gameDisplay.blit(Images["Fisherman1"], (x, y))
            if AnimationStage["Fisherman"][0] == 2:
                gameDisplay.blit(Images["Fisherman2"], (x, y))
            if AnimationStage["Fisherman"][1] <= 0:
                AnimationStage["Fisherman"][0] += 1
                AnimationStage["Fisherman"][1] = random.randint(850, 1200)  # random vara for dam to open/close
                if AnimationStage["Fisherman"][0] == 3:
                    AnimationStage["Fisherman"][0] = 1
            else:
                AnimationStage["Fisherman"][1] -= 5 / Count["Fisherman"]

        # Drawing all the diffrent tiles
        if Type == "Quarry Lv1":
            gameDisplay.blit(Images["Quarry1"], (x, y))
        if Type == "Quarry Lv2":
            gameDisplay.blit(Images["Quarry2"], (x, y))
        if Type == "Quarry Lv3":
            gameDisplay.blit(Images["Quarry3"], (x, y))
        if Type == "Quarry Lv4":
            gameDisplay.blit(Images["Quarry4"], (x, y))
        if Type == "Forest Lv4":
            gameDisplay.blit(Images["Forest4"], (x, y))
        if Type == "Forest Lv3":
            gameDisplay.blit(Images["Forest3"], (x, y))
        if Type == "Forest Lv1":
            gameDisplay.blit(Images["Forest1"], (x, y))
        if Type == "Forest Lv2":
            gameDisplay.blit(Images["Forest2"], (x, y))
        if Type == "Farm":
            gameDisplay.blit(Images["Farm"], (x, y))
        if Type == "Fisherman":
            gameDisplay.blit(Images["Fisherman0"], (x, y))
        if Type == "Solar_Power":
            gameDisplay.blit(Images["Solar_Power"], (x, y))

        if Type.find("City") != -1:
            gameDisplay.blit(Images["City"], (x, y))
        if Type.find("Factory") != -1 or Type == "Factory":
            gameDisplay.blit(Images["Factory"], (x, y))
        if Type.find("Solar_Power") != -1 or Type == "Solar_Power":
            gameDisplay.blit(Images["Solar_Power"], (x, y))
        if Type == "Super_Factory":
            gameDisplay.blit(Images["Super_Factory"], (x, y))

        # Drawing a little line around the tile to make a grid
        pygame.draw.rect(gameDisplay, (50, 50, 50), (x, y, (640 / width), (640 / height)), 1)

    # Draws the green selection thing
    if Obj == "Selection":
        if int(5 / (int(height / 2) - 3)) != 0:
            pygame.draw.rect(gameDisplay, (50, 205, 50), (x, y, (640 / width), (640 / height)),
                             int(5 / (int(height / 2) - 3)))
        else:
            pygame.draw.rect(gameDisplay, (50, 205, 50), (x, y, (640 / width), (640 / height)), 1)


# Generates a board using a height and a width
def gen_Board(board, height, width):
    for j in range(height):
        for i in range(width):
            percent = random.randint(1, 100)
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


# Map Board
def boardUpSize(board, height, width):
    for TileRow in board:
        for i in range(2):
            percent = random.randint(1, 100)
            if percent <= 50:
                TileRow.append("Grass")
            else:
                if percent <= 60:
                    TileRow.append("Water")
                elif percent <= 75:
                    TileRow.append("Forest Lv1")
                else:
                    TileRow.append("Quarry Lv1")
    for i in range(2):
        boardline = []
        for i in range(width):
            percent = random.randint(1, 100)
            if percent <= 50:
                boardline.append("Grass")
            else:
                if percent <= 60:
                    boardline.append("Water")
                elif percent <= 75:
                    boardline.append("Forest Lv1")
                else:
                    boardline.append("Quarry Lv1")
        board.append(boardline)
    return board


# The main part of the game
def game_loop(height, width, prestige, LoadSave):
    global AscendCount, MinerBought, ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, \
        AnimationStage, Count, Achviements, MusicPaused, Images, Mult, MapLevel, PrestigeCount

    # Declaring the values for resources
    game_run = True
    board = gen_Board([[0] * height for _ in range(width)], height, width)
    CurSelection = [-1, -1]
    ResourceCount = {"Wood": 60, "Stones": 60, "Food": 60, "Metal": 60, "Electricity": 60, "Prestige": prestige,
                     "Mandorium": 0}
    MaterialProduction = {"Wood": 0, "Stones": 0, "Food": 0, "Metal": 0, "Electricity": 0, "Prestige": 0,
                          "Mandorium": 0}
    MaterialsEarned = {"Wood": 250, "Stones": 250, "Food": 15, "Metal": 10, "Electricity": 0, "Prestige": prestige,
                       "Mandorium": 0}
    Cooldown = time.process_time()
    UnUpgradable = ["Water", "Grass", "Quarry Lv3", "Forest Lv3", "Water Fish", "Water Dam"]
    UpgradeInfo = {"Map Upgrades": [], "Forest Lv1": ["10 wood", "0 wood", "1 wood"],
                   "Quarry Lv1": ["15 wood", "0 stones", "1 stones"],
                   "Forest Lv2": ["40 wood", "1 wood", "5 wood"],
                   "Quarry Lv2": ["45 wood", "20 stones", "1 stones", "5 stones"]}

    Achievments = [
        {"Name": "Beginner", "Description": "You gathered 100 wood", "Reward": "Unlocked cities", "wood": 100,
         "Finished": False, "Show Cooldown": 0}

        , {"Name": "Food Man", "Description": "You gathered 50 food", "Reward": "Unlocked Factories", "wood": 300,
           "stones": 100, "food": 50, "Finished": False, "Show Cooldown": 0}

        , {"Name": "Heavy Metal", "Description": "You made 100 metal", "Reward": "Unlocked Electricity",
           "metal": 100, "Finished": False, "Show Cooldown": 0}

        , {"Name": "Shocking", "Description": "You produced 100 Electricity", "Reward": "Unlocked Electric Upgrades",
           "Electricity": 100, "Finished": False, "Show Cooldown": 0}

        , {"Name": "Fast Materials", "Description": "You got a Lvl4 Upgrade", "Reward": "Unlocked Upgraded Factories",
           "Finished": False, "Show Cooldown": 0}

        , {"Name": "Stockpile", "Description": "Have 200 food at any time", "Reward": "Unlocked Fishermen",
           "Finished": False, "Show Cooldown": 0}

        , {"Name": "Restarter", "Description": "You rebirthed 3 times", "Reward": "Unlocked Mandorium",
           "Finished": False, "Show Cooldown": 0}]
    # Tile Images
    Images = []
    Images = load_images("Images", height, width)
    ConfirmMessage = ""
    Confirming = False
    PreviousPos = [0, 0]
    MenuClicking = False
    AnimationStage = {"Water": [1, 0.5], "Dam": [1, 0.5]}
    Count = {"Water": 0, "Dam": 0}
    StartTime = time.process_time()
    hour = 0
    seconds = 0
    minutes = 0
    TimeStart = 0
    SaveMesses = 0
    Secret = False
    SaveCooldown = time.process_time() + 30
    cost = [5, 15]
    cost2 = [10]
    for i in range(MapLevel + 1):
        cost2.append(cost2[len(cost2) - 1] * 10)
    HighMult = 0
    for item in Mult:
        if Mult[item] >= HighMult:
            HighMult = Mult[item]
    for i in range(HighMult):
        cost.append(cost[len(cost) - 1] * 3)
    Saving = 0

    if LoadSave == True:
        SaveFile = open("Save File/SaveFile.txt", "r")
        ask = SaveFile.readline()
        DataList = []
        if ask.count("#") >= 90:
            count = 0
            for i in range(ask.count("#")):
                DataBit = ""
                FindBit = True
                while FindBit == True:
                    if ask[count] != "#":
                        DataBit += ask[count]
                    else:
                        FindBit = False
                    count += 1
                DataList.append(DataBit)

            Count = 0
            if DataList[Count] == "Beta1.6":
                Count += 1
                ItemChecker = [ResourceCount, MaterialProduction, MaterialsEarned]
                for Item in ItemChecker:
                    for item in Item:
                        Item[item] = int(DataList[Count])
                        Count += 1

                for item in Mult:
                    Mult[item] = int(DataList[Count])
                    Count += 1

                for quest in Achievments:
                    if Achievments.index(quest) != 6:
                        quest["Finished"] = DataList[Count]
                        if quest["Finished"] == "True":
                            AchievmentRewards(Achievments.index(quest))
                            quest["Finished"] = True
                        else:
                            quest["Finished"] = False
                        quest["Show Cooldown"] = int(DataList[Count + 1])
                    Count += 2

                height = int(DataList[Count])
                width = int(DataList[Count + 1])
                Count += 2
                Images = load_images("Images", height, width)
                board = [[0] * height for _ in range(width)]

                PrestigeCount = int(DataList[Count])
                AscendCount = int(DataList[Count + 1])
                MinerBought = DataList[Count + 2]
                MusicPaused = DataList[Count + 3]
                if MusicPaused == "True":
                    pygame.mixer.music.pause()
                    MusicPaused = True
                else:
                    MusicPaused = False

                Count += 4

                Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar_Power", "Super_Factory",
                         "Forest Lv1", "Forest Lv2", "Forest Lv3"
                    , "Forest Lv4", "Quarry Lv1", "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam",
                         "Water Fish", "Fisherman", "Dam"
                    , "CityFar", "CityFac", "Farm"]
                for j in range(height):
                    for i in range(width):
                        board[j][i] = Tiles[int(DataList[Count])]
                        Count += 1

    # Saves data(Useful for Prestiges)
    Saving = 3
    Data = ""
    Data += "Beta1.6" + "#"
    ItemChecker = [ResourceCount, MaterialProduction, MaterialsEarned]
    for Item in ItemChecker:
        for item in Item:
            Data += str(Item[item]) + "#"

    for item in Mult:
        Data += str(Mult[item]) + "#"

    for quest in Achievments:
        Data += str(quest["Finished"]) + "#"
        Data += str(int(quest["Show Cooldown"])) + "#"

    Data += str(height) + "#"
    Data += str(width) + "#"

    Data += str(PrestigeCount) + "#"
    Data += str(AscendCount) + "#"
    Data += str(MinerBought) + "#"
    Data += str(MusicPaused) + "#"

    Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar_Power", "Super_Factory", "Forest Lv1",
             "Forest Lv2", "Forest Lv3"
        , "Forest Lv4", "Quarry Lv1", "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam", "Water Fish",
             "Fisherman", "Dam"
        , "CityFar", "CityFac", "Farm"]
    for j in range(height):
        for i in range(width):
            Data += str(Tiles.index(board[j][i])) + "#"
    SaveFile = open("Save File/SaveFile.txt", "w")
    SaveFile.write(Data)

    while game_run == True:

        gameDisplay.fill((150, 150, 150))
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Moving your selection with the keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if CurSelection != [-1, -1] and CurSelection[0] != 0:
                        CurSelection[0] -= 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if CurSelection != [-1, -1] and CurSelection[0] != width - 1:
                        CurSelection[0] += 1
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if CurSelection != [-1, -1] and CurSelection[1] != 0:
                        CurSelection[1] -= 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if CurSelection != [-1, -1] and CurSelection[1] != height - 1:
                        CurSelection[1] += 1

            # Triggers when you press the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks for which tile you are selecting
                if Confirming == False:
                    xPos = int(pos[0] / ((640 / width)))
                    yPos = pos[1] / (640 / height) - int(160 / (640 / height))
                    if height % 4 == 2:
                        if yPos - 0.5 < int(yPos):
                            # Less then
                            yPos = int(yPos)
                        else:
                            # Greater then
                            yPos = int(yPos) + 1
                        yPos -= 1
                    else:
                        yPos = int(yPos)

                if xPos >= height:
                    xPos = PreviousPos[0]
                    yPos = PreviousPos[1]
                    MenuClicking = True
                if yPos < 0:
                    xPos = PreviousPos[0]
                    yPos = PreviousPos[1]
                    MenuClicking = True
                PreviousPos = [xPos, yPos]

                if pos[0] >= 445 and pos[0] <= 545 and pos[1] >= 400 and pos[1] <= 450 and Confirming == True and \
                        ConfirmMessage == "You have collected 10k Mandorium":
                    PrestigeCount = 0
                    for item in Mult:
                        Mult[item] *= 10
                    AscendCount += 1
                    MinerBought = False
                    game_loop(8, 8, 0, False)

                # Yes or no for Demolishing Buildings
                if pos[0] >= 570 and pos[0] <= 670 and pos[1] >= 400 and pos[
                    1] <= 450 and Confirming == True and ConfirmMessage \
                        != "You have collected 10k Mandorium":
                    Confirming = False

                    # Demolishing Buildings
                    if pos[0] >= 320 and pos[0] <= 420 and pos[1] >= 400 and pos[
                        1] <= 450 and Confirming == True and ConfirmMessage \
                            != "You have collected 10k Mandorium":
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

                # Making the selection
                if xPos <= height - 1 and yPos >= 0 and MenuClicking == False:
                    if CurSelection == [-1, -1] or CurSelection != [xPos, yPos]:
                        CurSelection = [xPos, yPos]
                    else:
                        CurSelection = [-1, -1]
                else:
                    MenuClicking = False

                # Restarts the game
                if pos[0] >= 650 and pos[0] <= 800 and pos[1] >= 685 and pos[1] <= 735:
                    MapLevel = 0
                    game_loop(8, 8, 0, False)

                # Prestige shop
                if pos[0] >= 825 and pos[0] <= 975 and pos[1] >= 740 and pos[1] <= 840:
                    run = True

                    while run == True:
                        gameDisplay.fill((150, 150, 150))
                        pygame.draw.rect(gameDisplay, (50, 50, 50), (0, 0, 1000, 800), 15)
                        pos = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775:
                                    run = False
                                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 25 and pos[1] <= 125 and ResourceCount[
                                    "Prestige"] >= cost[Mult["Wood"] - 1]:
                                    ResourceCount["Prestige"] -= cost[Mult["Wood"] - 1]
                                    Mult["Wood"] += 1
                                if 600 <= pos[0] <= 800 and pos[1] >= 25 and pos[1] <= 125 and ResourceCount[
                                    "Prestige"] >= cost[Mult["Stones"] - 1]:
                                    ResourceCount["Prestige"] -= cost[Mult["Stones"] - 1]
                                    Mult["Stones"] += 1
                                if 200 <= pos[0] <= 400 and pos[1] >= 150 and pos[1] <= 250 and \
                                        ResourceCount["Prestige"] >= cost[Mult["Food"] - 1]:
                                    ResourceCount["Prestige"] -= cost[Mult["Food"] - 1]
                                    Mult["Food"] += 1
                                if 600 <= pos[0] <= 800 and pos[1] >= 150 and pos[1] <= 250 and \
                                        ResourceCount["Prestige"] >= cost[Mult["Metal"] - 1]:
                                    ResourceCount["Prestige"] -= cost[Mult["Metal"] - 1]
                                    Mult["Metal"] += 1
                                if 200 <= pos[0] <= 400 and pos[1] >= 275 and pos[1] <= 375 and \
                                        ResourceCount["Prestige"] >= cost[Mult["Electricity"] - 1]:
                                    ResourceCount["Prestige"] -= cost[Mult["Electricity"] - 1]
                                    Mult["Electricity"] += 1
                                if 600 <= pos[0] <= 800 and pos[1] >= 275 and pos[1] <= 375 and \
                                        ResourceCount["Prestige"] >= cost2[MapLevel]:
                                    ResourceCount["Prestige"] -= cost2[MapLevel]
                                    height += 2
                                    width += 2
                                    board = boardUpSize(board, height, width)
                                    cost2.append(cost2[MapLevel] * 10)
                                    MapLevel += 1
                                    Images = load_images("Images", height, width)
                                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 400 and pos[
                                    1] <= 500 and PrestigeCount >= 3 and \
                                        ResourceCount["Prestige"] >= 10000 and MinerBought == False:
                                    MinerBought = True
                                    ResourceCount["Prestige"] -= 10000
                                    MaterialProduction["Mandorium"] += 100

                        # Adds things to cost
                        highMult = 0
                        for item in Mult:
                            if Mult[item] > highMult:
                                highMult = Mult[item]
                        if (cost[len(cost) - 1] / 3 ** highMult) == 5 / 3:
                            cost.append(cost[(len(cost) - 1)] * 3)

                        # Displaying amount of prestige
                        text_surface, rect = font_30.render(("Prestige: " + str(shorten(ResourceCount["Prestige"]))),
                                                            (0, 0, 0))
                        gameDisplay.blit(text_surface, (415, 35))

                        # Wood Upgrade
                        if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 25 and pos[1] <= 125:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (200, 25, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (200, 25, 200, 100), 0)
                        pygame.draw.rect(gameDisplay, (200, 0, 0), (200, 25, 200, 100), 3)
                        text_surface, rect = font_45.render(("Wood x" + str(Mult["Wood"] + 1)), (0, 0, 0))
                        gameDisplay.blit(text_surface, (235, 35))
                        text_surface, rect = font_40.render(("Cost: " + str(shorten(cost[Mult["Wood"] - 1]))),
                                                            (0, 0, 0))
                        gameDisplay.blit(text_surface, (235, 75))

                        # Stones Upgrade
                        if pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 25 and pos[1] <= 125:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (600, 25, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (600, 25, 200, 100), 0)
                        pygame.draw.rect(gameDisplay, (200, 0, 0), (600, 25, 200, 100), 3)
                        text_surface, rect = font_45.render(("Stones x" + str(Mult["Stones"] + 5)), (0, 0, 0))
                        gameDisplay.blit(text_surface, (620, 35))
                        text_surface, rect = font_40.render(("Cost: " + str(shorten(cost[Mult["Stones"] - 2]))),
                                                            (0, 0, 0))
                        gameDisplay.blit(text_surface, (635, 75))

                        # Food Upgrade
                        if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 150 and pos[1] <= 250:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (200, 150, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (200, 150, 200, 100), 0)
                        pygame.draw.rect(gameDisplay, (200, 0, 0), (200, 150, 200, 100), 3)
                        text_surface, rect = font_45.render(("Food x" + str(Mult["Food"] + 10)), (0, 0, 0))
                        gameDisplay.blit(text_surface, (235, 160))
                        text_surface, rect = font_40.render(("Cost: " + str(shorten(cost[Mult["Food"] - 1]))),
                                                            (0, 0, 0))
                        gameDisplay.blit(text_surface, (225, 200))

                        # Metal Upgrade
                        if pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 150 and pos[1] <= 250:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (600, 150, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (600, 150, 200, 100), 0)
                        pygame.draw.rect(gameDisplay, (200, 0, 0), (600, 150, 200, 100), 3)
                        text_surface, rect = font_45.render(("Metal x" + str(Mult["Metal"] + 8 + 'Food x'
                                                                             + str(Mult['Food'] - 5))), (0, 0, 0))
                        gameDisplay.blit(text_surface, (620, 160))
                        text_surface, rect = font_40.render(("Cost: " + str(shorten(cost[Mult["Metal"] - 5]))),
                                                            (0, 0, 0))
                        gameDisplay.blit(text_surface, (635, 200))

                        # Electricity Upgrade
                        if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 275 and pos[1] <= 375:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (200, 275, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (200, 275, 200, 100), 0)
                        pygame.draw.rect(gameDisplay, (200, 0, 0), (200, 275, 200, 100), 3)
                        text_surface, rect = font_35.render(("Electricity x" + str(Mult["Electricity"] + 10)), (0, 0, 0))
                        gameDisplay.blit(text_surface, (205, 290))
                        text_surface, rect = font_40.render(("Cost: " + str(shorten(cost[Mult["Electricity"] - 1]))),
                                                            (0, 0, 0))
                        gameDisplay.blit(text_surface, (225, 325))

                        # Map Upgrade
                        if pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 275 and pos[1] <= 375:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (600, 275, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (600, 275, 200, 100), 0)
                        pygame.draw.rect(gameDisplay, (200, 0, 0), (600, 275, 200, 100), 3)
                        text_surface, rect = font_40.render(("Map Upgrade"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (615, 290))
                        text_surface, rect = font_40.render(("Cost: " + str(shorten(cost2[MapLevel]))), (0, 0, 0))
                        gameDisplay.blit(text_surface, (625, 325))

                        # Mandorium Miner
                        if PrestigeCount >= 3:
                            if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 400 and pos[1] <= 500:
                                pygame.draw.rect(gameDisplay, (150, 0, 0), (200, 400, 200, 100), 0)
                            else:
                                pygame.draw.rect(gameDisplay, (255, 0, 0), (200, 400, 200, 100), 0)
                            pygame.draw.rect(gameDisplay, (200, 0, 0), (200, 400, 200, 100), 3)
                            text_surface, rect = font_30.render(("Mandorium Miner"), (0, 0, 0))
                            gameDisplay.blit(text_surface, (215, 425))
                            if MinerBought == False:
                                text_surface, rect = font_40.render(("Cost: 10k"), (0, 0, 0))
                            else:
                                text_surface, rect = font_40.render(("Bought"), (0, 0, 0))
                            gameDisplay.blit(text_surface, (235, 450))

                        # Back button
                        if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (775, 675, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (775, 675, 200, 100), 0)

                        text_surface, rect = font_50.render(("Back"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (835, 705))

                        pygame.display.update()
                        clock.tick(20)

                # Showing Options
                if pos[0] >= 650 and pos[0] <= 800 and pos[1] >= 740 and pos[1] <= 840:
                    run = True

                    # Runs the options window
                    while run == True:
                        gameDisplay.fill((150, 150, 150))
                        pygame.draw.rect(gameDisplay, (50, 50, 50), (0, 0, 1000, 800), 15)

                        # Handles Events
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                # Exit Options menu
                                if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775:
                                    run = False
                                # Pause/UnPause music
                                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 50 and pos[1] <= 150:
                                    if MusicPaused == False:
                                        MusicPaused = True
                                        pygame.mixer.music.pause()
                                    else:
                                        MusicPaused = False
                                        pygame.mixer.music.unpause()

                                # Saves your data to a save file
                                if pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 175 and pos[1] <= 275:
                                    Data = ""
                                    Data += "Beta1.6" + "#"
                                    ItemChecker = [ResourceCount, MaterialProduction, MaterialsEarned]
                                    for Item in ItemChecker:
                                        for item in Item:
                                            Data += str(Item[item]) + "#"

                                    for item in Mult:
                                        Data += str(Mult[item]) + "#"

                                    for quest in Achievments:
                                        Data += str(quest["Finished"]) + "#"
                                        Data += str(int(quest["Show Cooldown"])) + "#"

                                    Data += str(height) + "#"
                                    Data += str(width) + "#"

                                    Data += str(PrestigeCount) + "#"
                                    Data += str(AscendCount) + "#"
                                    Data += str(MinerBought) + "#"

                                    Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar_Power",
                                             "Super_Factory",
                                             "Forest Lv1", "Forest Lv2", "Forest Lv3", "Forest Lv4", "Quarry Lv1",
                                             "Quarry Lv2",
                                             "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam", "Water Fish",
                                             "Fisherman", "Dam"
                                        , "CityFar", "CityFac", "Farm"]

                                    for j in range(height):
                                        for i in range(width):
                                            Data += str(Tiles.index(board[j][i])) + "#"
                                    SaveFile = open("Save File/SaveFile.txt", "w")
                                    SaveFile.write(Data)

                                    # Exports save data
                                if pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 50 and pos[1] <= 150:
                                    Data = ""
                                    Data += "Beta1.6" + "#"
                                    ItemChecker = [ResourceCount, MaterialProduction, MaterialsEarned]
                                    for Item in ItemChecker:
                                        for item in Item:
                                            Data += str(Item[item]) + "#"

                                    for item in Mult:
                                        Data += str(Mult[item]) + "#"

                                    for quest in Achievments:
                                        Data += str(quest["Finished"]) + "#"
                                        Data += str(int(quest["Show Cooldown"])) + "#"

                                    Data += str(height) + "#"
                                    Data += str(width) + "#"

                                    Data += str(PrestigeCount) + "#"
                                    Data += str(AscendCount) + "#"
                                    Data += str(MinerBought) + "#"
                                    Data += str(MusicPaused) + "#"

                                    Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar_Power",
                                             "Super_Factory",
                                             "Forest Lv1", "Forest Lv2", "Forest Lv3", "Forest Lv4", "Quarry Lv1",
                                             "Quarry Lv2",
                                             "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam", "Water Fish",
                                             "Fisherman", "Dam"
                                        , "CityFar", "CityFac", "Farm"]

                                    for j in range(height):
                                        for i in range(width):
                                            Data += str(Tiles.index(board[j][i])) + "#"
                                    print(Data)

                                # Import save Data:
                                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 175 and pos[1] <= 275 and \
                                        Achievments[6]["Finished"] != True:
                                    ask = input("Give me your data")
                                    DataList = []

                                    if ask.count("#") >= 90:
                                        count = 0
                                        for i in range(ask.count("#")):
                                            DataBit = ""
                                            FindBit = True
                                            while FindBit == True:
                                                if ask[count] != "#":
                                                    DataBit += ask[count]
                                                else:
                                                    FindBit = False
                                                count += 1
                                            DataList.append(DataBit)

                                        Count = 0
                                        if DataList[Count] == "Beta1.6":
                                            Count += 1
                                            ItemChecker = [ResourceCount, MaterialProduction, MaterialsEarned]
                                            for Item in ItemChecker:
                                                for item in Item:
                                                    Item[item] = int(DataList[Count])
                                                    Count += 1

                                            for item in Mult:
                                                Mult[item] = int(DataList[Count])
                                                Count += 1

                                            for quest in Achievments:
                                                if Achievments.index(quest) != 6:
                                                    quest["Finished"] = DataList[Count]
                                                    if quest["Finished"] == "True":
                                                        AchievmentRewards(Achievments.index(quest))
                                                        quest["Finished"] = True
                                                    else:
                                                        quest["Finished"] = False
                                                    quest["Show Cooldown"] = int(DataList[Count + 1])
                                                Count += 2

                                            height = int(DataList[Count])
                                            width = int(DataList[Count + 1])
                                            Count += 2
                                            Images = load_images("Images", height, width)
                                            board = [[0] * height for _ in range(width)]

                                            PrestigeCount = int(DataList[Count])
                                            AscendCount = int(DataList[Count + 1])
                                            MinerBought = DataList[Count + 2]
                                            MusicPaused = DataList[Count + 3]
                                            if MusicPaused == "True":
                                                pygame.mixer.music.pause()
                                                MusicPaused = True
                                            else:
                                                MusicPaused = False

                                            Count += 4

                                            Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So",
                                                     "Solar_Power", "Super_Factory",
                                                     "Forest Lv1", "Forest Lv2", "Forest Lv3", "Forest Lv4",
                                                     "Quarry Lv1",
                                                     "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam",
                                                     "Water Fish", "Fisherman", "Dam"
                                                , "CityFar", "CityFac", "Farm"]
                                            for j in range(height):
                                                for i in range(width):
                                                    board[j][i] = Tiles[int(DataList[Count])]
                                                    Count += 1

                        pos = pygame.mouse.get_pos()

                        # Displays all the buttons

                        if pos[0] >= 775 and pos[0] <= 975 and pos[1] >= 675 and pos[1] <= 775:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (775, 675, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (775, 675, 200, 100), 0)

                        text_surface, rect = font_50.render(("Back"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (835, 705))

                        if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 50 and pos[1] <= 150:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (200, 50, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (200, 50, 200, 100), 0)

                        if MusicPaused == False:
                            text_surface, rect = font_50.render(("Mute Music"), (0, 0, 0))
                            gameDisplay.blit(text_surface, (210, 80))
                        else:
                            text_surface, rect = font_40.render(("Unmute Music"), (0, 0, 0))
                            gameDisplay.blit(text_surface, (210, 86))

                        if pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 50 and pos[1] <= 150:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (600, 50, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (600, 50, 200, 100), 0)

                        text_surface, rect = font_40.render(("Export Data"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (620, 80))

                        if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 175 and pos[1] <= 275:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (200, 175, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (200, 175, 200, 100), 0)

                        text_surface, rect = font_40.render(("Import Data"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (220, 205))

                        if pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 175 and pos[1] <= 275:
                            pygame.draw.rect(gameDisplay, (150, 0, 0), (600, 175, 200, 100), 0)
                        else:
                            pygame.draw.rect(gameDisplay, (255, 0, 0), (600, 175, 200, 100), 0)

                        text_surface, rect = font_40.render(("Save Game"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (630, 205))

                        pygame.display.flip()
                        clock.tick(60)

                # Demolishes Selected Building
                if pos[0] >= 825 and pos[0] <= 975 and pos[1] >= 685 and pos[1] <= 735 and CurSelection != [-1, -1]:
                    Confirming = True
                    ConfirmMessage = "Are you sure you want to demolish the building?"

                # Will need to re-check & fix readability
                # All of the upgrades
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650 and CurSelection != [-1, -1]:
                    if board[CurSelection[1]][CurSelection[0]] == "Forest Lv3" and ResourceCount["Metal"] >= 100 and \
                            ResourceCount["Electricity"] >= 1:
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
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv3" and ResourceCount["Metal"] >= 150 and \
                            ResourceCount["Electricity"] >= 1:
                        ResourceCount["Metal"] -= 150
                        MaterialProduction["Stones"] += 10
                        board[CurSelection[1]][CurSelection[0]] = "Quarry Lv4"
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv2" and ResourceCount["Wood"] >= 45 and \
                            ResourceCount["Stones"] >= 20:
                        ResourceCount["Wood"] -= 45
                        ResourceCount["Stones"] -= 20
                        MaterialProduction["Stones"] += 3
                        board[CurSelection[1]][CurSelection[0]] = "Quarry Lv3"
                    if board[CurSelection[1]][CurSelection[0]] == "Quarry Lv1" and ResourceCount["Wood"] >= 15:
                        ResourceCount["Wood"] -= 15
                        MaterialProduction["Stones"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "Quarry Lv2"
                    if board[CurSelection[1]][CurSelection[0]] == "Factory So" and ResourceCount["Metal"] >= 100 and \
                            ResourceCount["Electricity"] >= 2:
                        ResourceCount["Metal"] -= 100
                        MaterialProduction["Metal"] -= 1
                        MaterialProduction["Electricity"] += 3
                        board[CurSelection[1]][CurSelection[0]] = "Solar_Power"
                    if board[CurSelection[1]][CurSelection[0]] == "Factory Su" and ResourceCount["Metal"] >= 100 and \
                            ResourceCount["Electricity"] >= 2:
                        ResourceCount["Metal"] -= 100
                        MaterialProduction["Metal"] += 4
                        board[CurSelection[1]][CurSelection[0]] = "Super_Factory"
                    if board[CurSelection[1]][CurSelection[0]] == "Factory" and pos[0] >= 725 and pos[0] <= 925 and pos[
                        1] >= 550 and pos[1] <= 650:
                        board[CurSelection[1]][CurSelection[0]] = "Factory Su"
                    if board[CurSelection[1]][CurSelection[0]] == "CityFac" and ResourceCount["Food"] >= 1 and \
                            ResourceCount["Stones"] >= 50 \
                            and Achievments[1]["Finished"] == True:
                        ResourceCount["Stones"] -= 50
                        MaterialProduction["Metal"] += 1
                        MaterialProduction["Food"] -= 1
                        board[CurSelection[1]][CurSelection[0]] = "Factory"
                    if board[CurSelection[1]][CurSelection[0]] == "Water Fish" and ResourceCount["Wood"] >= 100 and \
                            ResourceCount["Metal"] >= 25 \
                            and Achievments[5]["Finished"] == True:
                        ResourceCount["Wood"] -= 100
                        ResourceCount["Metal"] -= 25
                        MaterialProduction["Food"] += 2
                        board[CurSelection[1]][CurSelection[0]] = "Fisherman"
                    if board[CurSelection[1]][CurSelection[0]] == "City" and pos[0] >= 725 and pos[0] <= 925 and pos[
                        1] >= 550 and pos[1] <= 650:
                        board[CurSelection[1]][CurSelection[0]] = "CityFac"
                    if board[CurSelection[1]][CurSelection[0]] == "Water" and pos[0] >= 725 and pos[0] <= 925 and pos[
                        1] >= 550 and pos[1] <= 650:
                        board[CurSelection[1]][CurSelection[0]] = "Water Fish"
                    if board[CurSelection[1]][CurSelection[0]] == "CityFar" and ResourceCount["Wood"] >= 100 and \
                            ResourceCount["Food"] >= 50 \
                            and Achievments[1]["Finished"] == True:
                        ResourceCount["Wood"] -= 100
                        ResourceCount["Food"] -= 50
                        MaterialProduction["Food"] += 2
                        board[CurSelection[1]][CurSelection[0]] = "Farm"
                    if board[CurSelection[1]][CurSelection[0]] == "Grass" and ResourceCount["Wood"] >= 50 and \
                            ResourceCount["Stones"] >= 20 \
                            and UnUpgradable[1] != "Grass":
                        ResourceCount["Wood"] -= 50
                        ResourceCount["Stones"] -= 20
                        MaterialProduction["Food"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "City"
                    if board[CurSelection[1]][CurSelection[0]] == "Water Dam" and ResourceCount["Wood"] >= 200 and \
                            ResourceCount["Metal"] >= 50 \
                            and Achievments[2]["Finished"] == True:
                        ResourceCount["Wood"] -= 200
                        ResourceCount["Metal"] -= 50
                        MaterialProduction["Electricity"] += 1
                        board[CurSelection[1]][CurSelection[0]] = "Dam"

                # Path Choices
                if board[CurSelection[1]][CurSelection[0]] == "City" and pos[0] >= 725 and pos[0] <= 925 and pos[
                    1] >= 350 and pos[1] <= 450:
                    board[CurSelection[1]][CurSelection[0]] = "CityFar"
                if board[CurSelection[1]][CurSelection[0]] == "Water" and pos[0] >= 725 and pos[0] <= 925 and pos[
                    1] >= 350 and pos[1] <= 450:
                    board[CurSelection[1]][CurSelection[0]] = "Water Dam"
                if board[CurSelection[1]][CurSelection[0]] == "Factory" and pos[0] >= 725 and pos[0] <= 925 and pos[
                    1] >= 350 and pos[1] <= 450:
                    board[CurSelection[1]][CurSelection[0]] = "Factory So"

                # Taking you back to mainscreen when you finish and calculates time
                if CurSelection == [-1, -1] and pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650 and \
                        ResourceCount["Wood"] >= 1000 \
                        and ResourceCount["Stones"] >= 500 and ResourceCount["Food"] >= 200 and ResourceCount[
                    "Metal"] >= 100 \
                        and ResourceCount["Electricity"] >= 50:
                    Earned = 0
                    Tiles = ["Grass", "City", "Factory Su", "Factory Su", "Factory So", "Solar_Power", "Super_Factory",
                             "Forest Lv1", "Forest Lv2", "Forest Lv3"
                        , "Forest Lv4", "Quarry Lv1", "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam",
                             "Water Fish", "Fisherman", "Dam"
                        , "CityFar", "CityFac", "Farm"]
                    Value = [0, 1, 2, 2, 2, 3, 3, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 2, 1, 1, 2]
                    for tileRow in board:
                        for tile in tileRow:
                            Earned += Value[Tiles.index(tile)]
                    Earned += int(ResourceCount["Wood"] / 1000) + int(ResourceCount["Stones"] / 500) + int(
                        ResourceCount["Food"] / 200) + \
                              int(ResourceCount["Metal"] / 100) + int(ResourceCount["Electricity"] / 50)
                    PrestigeCount += 1
                    game_loop(height, width, prestige + Earned, False)

        # Counting Tiles for certain animations
        Count = {"Water": 0, "Water Fish": 0,"Dam": 0, "Forest Lv4": 0, "Quarry Lv4": 0, "Super_Factory": 0}
        for j in range(height):
            for i in range(width):
                if board[j][i] == "Water" or board[j][i] == "Water Fish" or board[j][i] == "Water Dam":
                    Count["Water"] += 1
                if board[j][i] == "Water Fish":
                    Count["Water Fish"] += 1
                if board[j][i] == "Dam":
                    Count["Dam"] += 1
                if board[j][i] == "Forest Lv4":
                    Count["Forest Lv4"] += 1
                if board[j][i] == "Quarry Lv4":
                    Count["Quarry Lv4"] += 1
                if board[j][i] == "Super_Factory":
                    Count["Super_Factory"] += 1

        # Drawing all Tiles
        for j in range(height):
            for i in range(width):
                draw(i * (640 / width), j * (640 / height) + 160, "Tile", board[j][i], height, width, Images,
                     AnimationStage, Count)

        # Drawing Selection
        if CurSelection != [-1, -1]:
            draw(CurSelection[0] * (640 / width), CurSelection[1] * (640 / height) + 160, "Selection", "Green", height,
                 width, Images, AnimationStage, Count)

        # This is my try at making multiple files. It looks very ineffecient and probably bad to use.
        board, ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, Count, Achviements, \
        Mult = Menu.menu(board, CurSelection, pygame, gameDisplay,
                         [font_23, font_25, font_30, font_35, font_40, font_50, font_75, font_150],
                         ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, Count,
                         Achievments,
                         Mult, PrestigeCount, AscendCount)
        # Achvievment Check
        Achviement(Achievments)

        # Display the Achievement
        for quest in Achievments:
            if quest["Show Cooldown"] > 0:
                quest["Show Cooldown"] -= 0.1
                pygame.draw.rect(gameDisplay, (200, 200, 200), (300, 700, 400, 100), 0)
                pygame.draw.rect(gameDisplay, (25, 25, 25), (300, 700, 400, 100), 5)
                text_surface, rect = font_50.render((quest["Name"]), (0, 0, 0))
                text_surface, rect = font_25.render((quest["Description"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 750))
                text_surface, rect = font_25.render((quest["Reward"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (310, 775))
            else:
                quest["Show Cooldown"] = 0

        # Shows a confirm message
        if Confirming == True:
            pygame.draw.rect(gameDisplay, (150, 150, 150), (300, 300, 400, 200), 0)
            pygame.draw.rect(gameDisplay, (50, 50, 50), (300, 300, 400, 200), 5)
            if ConfirmMessage != "You have collected 10k Mandorium":
                text_surface, rect = font_23.render((ConfirmMessage), (0, 0, 0))
                gameDisplay.blit(text_surface, (315, 350))
            else:
                text_surface, rect = font_23.render((ConfirmMessage), (0, 0, 0))
                gameDisplay.blit(text_surface, (365, 350))
                text_surface, rect = font_23.render(("You will now ascend"), (0, 0, 0))
                gameDisplay.blit(text_surface, (405, 370))

            if ConfirmMessage != "You have collected 10k Mandorium":
                if pos[0] >= 320 and pos[0] <= 420 and pos[1] >= 400 and pos[1] <= 450:
                    pygame.draw.rect(gameDisplay, (0, 100, 0), (320, 400, 100, 50), 0)
                else:
                    pygame.draw.rect(gameDisplay, (0, 150, 0), (320, 400, 100, 50), 0)

                pygame.draw.rect(gameDisplay, (0, 200, 0), (320, 400, 100, 50), 3)

                if pos[0] >= 570 and pos[0] <= 670 and pos[1] >= 400 and pos[1] <= 450:
                    pygame.draw.rect(gameDisplay, (100, 0, 0), (570, 400, 100, 50), 0)
                else:
                    pygame.draw.rect(gameDisplay, (150, 0, 0), (570, 400, 100, 50), 0)

                pygame.draw.rect(gameDisplay, (200, 0, 0), (570, 400, 100, 50), 3)

                text_surface, rect = font_23.render(("Yes"), (0, 0, 0))
                gameDisplay.blit(text_surface, (355, 415))
                text_surface, rect = font_23.render(("No"), (0, 0, 0))
                gameDisplay.blit(text_surface, (610, 415))
            else:
                if pos[0] >= 445 and pos[0] <= 545 and pos[1] >= 400 and pos[1] <= 450:
                    pygame.draw.rect(gameDisplay, (0, 100, 0), (445, 400, 100, 50), 0)
                else:
                    pygame.draw.rect(gameDisplay, (0, 150, 0), (445, 400, 100, 50), 0)

                pygame.draw.rect(gameDisplay, (0, 200, 0), (445, 400, 100, 50), 3)

                text_surface, rect = font_23.render(("Proceed"), (0, 0, 0))
                gameDisplay.blit(text_surface, (465, 415))

            CurSelection = [-1, -1]

        # Auto Save
        if time.process_time() - SaveCooldown >= 0:
            Saving = 3
            Data = ""
            Data += "Beta1.6" + "#"
            ItemChecker = [ResourceCount, MaterialProduction, MaterialsEarned]
            for Item in ItemChecker:
                for item in Item:
                    Data += str(Item[item]) + "#"

            for item in Mult:
                Data += str(Mult[item]) + "#"

            for quest in Achievments:
                Data += str(quest["Finished"]) + "#"
                Data += str(int(quest["Show Cooldown"])) + "#"

            Data += str(height) + "#"
            Data += str(width) + "#"

            Data += str(PrestigeCount) + "#"
            Data += str(AscendCount) + "#"
            Data += str(MinerBought) + "#"
            Data += str(MusicPaused) + "#"

            Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar_Power", "Super_Factory",
                     "Forest Lv1", "Forest Lv2", "Forest Lv3"
                , "Forest Lv4", "Quarry Lv1", "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam",
                     "Water Fish", "Fisherman", "Dam"
                , "CityFar", "CityFac", "Farm"]
            for j in range(height):
                for i in range(width):
                    Data += str(Tiles.index(board[j][i])) + "#"
            SaveFile = open("Save File/SaveFile.txt", "w")
            SaveFile.write(Data)

            SaveCooldown = time.process_time() + 30

        if Saving >= 0:
            text_surface, rect = font_40.render(("Saving"), (0, 0, 0))
            gameDisplay.blit(text_surface, (10, 760))
            Saving -= 0.05

        # A Miner from the prestige shop
        if MinerBought == True:
            MaterialProduction["Mandorium"] = 100
            Mult["Mandoirum"] = 1

        if ResourceCount["Mandorium"] >= 10000:
            Confirming = True
            ConfirmMessage = "You have collected 10k Mandorium"

        pygame.display.flip()
        clock.tick(60)


MusicPaused = MainMenu.HomeScreen(pygame, gameDisplay, [font_40, font_50, font_150], clock, MusicPaused)
