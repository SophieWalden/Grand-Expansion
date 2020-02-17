# This is the file for all the code used in displaying values in the menu
from custom_source_modules import *
def TextMove(Str):
    return -1 * (5 * len(str(Str)))


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


def menu(board, selection, pygame, gameDisplay, Fonts, ResourceCount, MaterialProduction, Cooldown, UnUpgradable,
         UpgradeInfo, MaterialsEarned, Count, Achviements, Mult, PrestigeCount, AscendCount):
    import time
    # Drawing Menu
    pygame.draw.line(gameDisplay, (50, 50, 50), (0, 160), (1000, 160), 5)
    pygame.draw.line(gameDisplay, (50, 50, 50), (250, 160), (250, 0), 5)
    pygame.draw.line(gameDisplay, (50, 50, 50), (500, 160), (500, 0), 5)
    pygame.draw.line(gameDisplay, (50, 50, 50), (750, 160), (750, 0), 5)
    pygame.draw.line(gameDisplay, (50, 50, 50), (0, 80), (1000, 80), 5)

    pos = pygame.mouse.get_pos()

    # Displaying Values for each Item

    # Wood
    pygame.draw.rect(gameDisplay, (165, 42, 42), (5, 15, 50, 50), 0)
    text_surface, rect = Fonts[5].render(("Wood: "), (0, 0, 0))
    gameDisplay.blit(text_surface, (60, 20))
    text_surface, rect = Fonts[3].render((shorten(ResourceCount["Wood"])), (0, 0, 0))
    gameDisplay.blit(text_surface, (160, 30))

    # Stones
    if MaterialsEarned["Stones"] >= 1:
        pygame.draw.rect(gameDisplay, (50, 50, 50), (5, 95, 50, 50), 0)
        text_surface, rect = Fonts[5].render(("Stones: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (60, 100))
        text_surface, rect = Fonts[2].render((shorten(ResourceCount["Stones"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (182, 113))

    # Food:
    if MaterialsEarned["Food"] >= 1:
        pygame.draw.rect(gameDisplay, (228, 217, 111), (255, 15, 50, 50), 0)
        text_surface, rect = Fonts[5].render(("Food: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (310, 20))
        text_surface, rect = Fonts[3].render((shorten(ResourceCount["Food"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (400, 30))

    # Metal
    if MaterialsEarned["Metal"] >= 1:
        pygame.draw.rect(gameDisplay, (125, 125, 125), (255, 95, 50, 50), 0)
        text_surface, rect = Fonts[5].render(("Metal: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (310, 100))
        text_surface, rect = Fonts[3].render((shorten(ResourceCount["Metal"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (420, 110))

    # Electricity
    if MaterialsEarned["Electricity"] >= 1:
        pygame.draw.rect(gameDisplay, (255, 255, 0), (505, 15, 50, 50), 0)
        text_surface, rect = Fonts[2].render(("Electricity: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (560, 30))
        text_surface, rect = Fonts[3].render((shorten(ResourceCount["Electricity"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (680, 27))

    # Prestige
    if MaterialsEarned["Prestige"] >= 1:
        pygame.draw.rect(gameDisplay, (150, 0, 150), (505, 95, 50, 50), 0)
        text_surface, rect = Fonts[4].render(("Prestige: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (560, 105))
        text_surface, rect = Fonts[1].render((shorten(ResourceCount["Prestige"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (685, 113))

    # Mandorium
    if PrestigeCount >= 3:
        pygame.draw.rect(gameDisplay, (3, 63, 99), (755, 15, 50, 50), 0)
        text_surface, rect = Fonts[3].render(("Mandorium: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (810, 30))
        text_surface, rect = Fonts[1].render((shorten(ResourceCount["Mandorium"])), (0, 0, 0))
        gameDisplay.blit(text_surface, (945, 37))

    # Ascension
    if AscendCount >= 1:
        pygame.draw.rect(gameDisplay, (0, 150, 99), (755, 95, 50, 50), 0)
        text_surface, rect = Fonts[3].render(("Ascends: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (810, 105))
        text_surface, rect = Fonts[1].render((str(AscendCount)), (0, 0, 0))
        gameDisplay.blit(text_surface, (915, 110))

    # Displays User's Mouse Selection
    if selection != [-1, -1]:
        if board[selection[1]][selection[0]] == "Dam":
            text_surface, rect = Fonts[6].render(("Dam"), (0, 0, 0))
            gameDisplay.blit(text_surface, (665, 175))

        if board[selection[1]][selection[0]] == "Grass":
            text_surface, rect = Fonts[6].render(("Grass"), (0, 0, 0))
            gameDisplay.blit(text_surface, (750, 175))

        if board[selection[1]][selection[0]].find("Water") != -1:
            text_surface, rect = Fonts[6].render(("Water"), (0, 0, 0))
            gameDisplay.blit(text_surface, (750, 175))

        if board[selection[1]][selection[0]] == "Forest Lv1" or board[selection[1]][selection[0]] == "Forest Lv2" or \
                board[selection[1]][selection[0]] == "Forest Lv3":
            text_surface, rect = Fonts[6].render(("Forest"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))

        if board[selection[1]][selection[0]] == "Quarry Lv1" or board[selection[1]][selection[0]] == "Quarry Lv2" or \
                board[selection[1]][selection[0]] == "Quarry Lv3":
            text_surface, rect = Fonts[6].render(("Quarry"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))


        if board[selection[1]][selection[0]] == "City":
            text_surface, rect = Fonts[6].render(("Upgrade Path"), (0, 0, 0))
            gameDisplay.blit(text_surface, (660, 175))

        if board[selection[1]][selection[0]] == "CityFac" or board[selection[1]][selection[0]] == "CityFar":
            text_surface, rect = Fonts[6].render(("City"), (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))

        if board[selection[1]][selection[0]].find("Factory ") != -1:
            text_surface, rect = Fonts[6].render("Factory", (0, 0, 0))
            gameDisplay.blit(text_surface, (730, 175))

        if board[selection[1]][selection[0]] == "Solar_Power":
            text_surface, rect = Fonts[6].render("Solar_Power", (0, 0, 0))
            gameDisplay.blit(text_surface, (670, 175))

        if board[selection[1]][selection[0]] == "Super_Factory":
            text_surface, rect = Fonts[6].render("Super_Factory", (0, 0, 0))
            gameDisplay.blit(text_surface, (642, 175))

        # Button for upgrading
        UpgradePaths = ["City", "Water", "Factory"]
        stop = False
        for item in UpgradePaths:
            if board[selection[1]][selection[0]] == item:
                stop = True

        # Displays Upgrading Info
        if stop == False:
            stop = False
            for item in UnUpgradable:
                if item == board[selection[1]][selection[0]]:
                    stop = True
            if stop == False:
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                    pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 550, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 550, 200, 100), 0)

                text_surface, rect = Fonts[5].render(("Upgrade"), (0, 0, 0))
                gameDisplay.blit(text_surface, (760, 575))
# Upgrade Info on production
                text_surface, rect = Fonts[5].render(("Current Production: "), (0, 0, 0))
                gameDisplay.blit(text_surface, (650, 250))
                if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                    text_surface, rect = Fonts[5].render((str(UpgradeInfo[board[selection[1]][selection[0]]][1])),
                                                         (0, 0, 0))
                else:
                    text_surface, rect = Fonts[5].render((str(UpgradeInfo[board[selection[1]][selection[0]]][2])),
                                                         (0, 0, 0))

                if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                    if len(UpgradeInfo[board[selection[1]][selection[0]]][1]) >= 10:
                        gameDisplay.blit(text_surface, (710, 325))
                    else:
                        gameDisplay.blit(text_surface, (730, 325))
                else:
                    if len(UpgradeInfo[board[selection[1]][selection[0]]][2]) >= 10:
                        gameDisplay.blit(text_surface, (710, 325))
                    else:
                        gameDisplay.blit(text_surface, (730, 325))

                pygame.draw.line(gameDisplay, (50, 50, 50), (640, 400), (1000, 400), 5)
                if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                    text_surface, rect = Fonts[5].render(
                        ("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][2])), (0, 0, 0))
                    gameDisplay.blit(text_surface, (670, 450))
                else:

                    if board[selection[1]][selection[0]] != "Water":
                        text_surface, rect = Fonts[3].render(
                            ("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][3])), (0, 0, 0))
                    else:
                        text_surface, rect = Fonts[3].render(
                            ("Next Level: " + str(UpgradeInfo[board[selection[1]][selection[0]]][3])), (0, 0, 0))

                    gameDisplay.blit(text_surface, (670, 410))

                if len(UpgradeInfo[board[selection[1]][selection[0]]]) == 3:
                    text_surface, rect = Fonts[5].render(
                        ("Cost: " + str(UpgradeInfo[board[selection[1]][selection[0]]][0])), (0, 0, 0))
                    gameDisplay.blit(text_surface, (710, 500))
                else:
                    if len(str(UpgradeInfo[board[selection[1]][selection[0]]][0])) >= 10:
                        text_surface, rect = Fonts[3].render(
                            ("Cost: " + str(UpgradeInfo[board[selection[1]][selection[0]]][0])), (0, 0, 0))
                    else:
                        text_surface, rect = Fonts[5].render(
                            ("Cost: " + str(UpgradeInfo[board[selection[1]][selection[0]]][0])), (0, 0, 0))
                    gameDisplay.blit(text_surface, (700, 450))
                    if len(str(UpgradeInfo[board[selection[1]][selection[0]]][1])) >= 10:
                        text_surface, rect = Fonts[3].render((str(UpgradeInfo[board[selection[1]][selection[0]]][1])),
                                                             (0, 0, 0))
                    else:
                        text_surface, rect = Fonts[5].render((str(UpgradeInfo[board[selection[1]][selection[0]]][1])),
                                                             (0, 0, 0))
                    if len(str(UpgradeInfo[board[selection[1]][selection[0]]][1])) >= 10:
                        gameDisplay.blit(text_surface, (660, 500))
                    else:
                        gameDisplay.blit(text_surface, (720, 500))
        else:
            # City Upgrade path
            # Template
            # if pos[0] >= ### -> Mouse Selection X Layer
            # and pos[0] <= ### -> Mouse Selection Y Layer
            # and pos[1] >= ### -> Mouse X Layer Disengage Cutoff
            # and pos[1] <= ### -> Mouse Y Layer Disengage Cutoff
            if board[selection[1]][selection[0]] == "City":
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                    pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 550, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 550, 200, 100), 0)

                text_surface, rect = Fonts[5].render("Factory", (0, 0, 0))
                gameDisplay.blit(text_surface, (760, 575))

                # Farm Button
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 250 and pos[1] <= 350:
                    # non mouse hover
                    pygame.draw.rect(gameDisplay, (51,51,0), (725, 250, 200, 100), 0)
                else:
                    # Shaded once mouse hover
                    pygame.draw.rect(gameDisplay, (102, 102, 0), (725, 250, 200, 100), 0)
                # Text Location & Color
                text_surface, rect = Fonts[5].render(("Farm"), (0, 250, 0))
                gameDisplay.blit(text_surface, (780, 275))

            '''
                            # Power Button
                            if pos[0] >= 425 and pos[0] <= 925 and pos[1] >= 450 and pos[1] <= 550:
                                pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 400, 200, 100), 0)
                            else:
                                pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 400, 200, 100), 0)

                            text_surface, rect = Fonts[5].render("Power", (0, 0, 0))
                            gameDisplay.blit(text_surface, (770, 420))
            '''
            # Water Upgrade Paths
            if board[selection[1]][selection[0]] == "Water":
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                    pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 550, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 550, 200, 100), 0)

                text_surface, rect = Fonts[5].render(("Fishing Boat"), (0, 0, 0))
                gameDisplay.blit(text_surface, (740, 575))

                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 350 and pos[1] <= 450:
                    pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 350, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 350, 200, 100), 0)

                text_surface, rect = Fonts[5].render("Dam", (0, 0, 0))
                gameDisplay.blit(text_surface, (780, 375))

            # Factory Paths/ Text Info
            if board[selection[1]][selection[0]] == "Factory":
                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
                    pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 550, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 550, 200, 100), 0)

                text_surface, rect = Fonts[3].render("Super Factory", (0, 0, 0))
                gameDisplay.blit(text_surface, (740, 575))

                if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 350 and pos[1] <= 450:
                    pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 350, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 350, 200, 100), 0)

                text_surface, rect = Fonts[4].render("Solar Power", (0, 0, 0))
                gameDisplay.blit(text_surface, (740, 375))

    # Adding all the things produced
    #  Line 300 Speed for Resource Gather
    if time.process_time() - Cooldown >= 0:
        for Item in ResourceCount:
            if Item != "Metal":
                ResourceCount[Item] += MaterialProduction[Item] * Mult[Item]
                MaterialsEarned[Item] += MaterialProduction[Item] * Mult[Item]
            else:
                for i in range(Count["Super_Factory"]):
                    ResourceCount["Food"] += 3 * Mult["Food"]
                if ResourceCount["Food"] * Mult["Food"] >= MaterialProduction[Item] * Mult[Item]:
                    ResourceCount[Item] += MaterialProduction[Item] * Mult[Item]
                    MaterialsEarned[Item] += MaterialProduction[Item] * Mult[Item]
                    ResourceCount["Food"] -= MaterialProduction[Item] * Mult[Item]
                else:
                    ResourceCount[Item] += ResourceCount["Food"] * Mult["Food"]
                    MaterialsEarned[Item] += ResourceCount["Food"] * Mult["Food"]
                    ResourceCount["Food"] -= ResourceCount["Food"] * Mult["Food"]

        if Count["Forest Lv4"] >= 1 and ResourceCount["Electricity"] > 0:
            if ResourceCount["Electricity"] * Mult["Electricity"] >= Count["Forest Lv4"]:
                ResourceCount["Electricity"] -= int(Count["Forest Lv4"] / Mult["Electricity"])
            else:
                num = Count["Forest Lv4"] - (ResourceCount["Electricity"] * Mult["Electricity"])
                ResourceCount["Wood"] -= 15 * num * Mult["Wood"]
                ResourceCount["Electricity"] = 0

        if Count["Quarry Lv4"] >= 1 and ResourceCount["Electricity"] > 0:
            if ResourceCount["Electricity"] * Mult["Electricity"] >= Count["Quarry Lv4"]:
                ResourceCount["Electricity"] -= int(Count["Quarry Lv4"] / Mult["Electricity"])
            else:
                num = Count["Quarry Lv4"] - (ResourceCount["Electricity"] * Mult["Electricity"])
                ResourceCount["Stones"] -= 15 * num * Mult["Stones"]
                ResourceCount["Electricity"] = 0

        Cooldown = time.process_time()

    # Drawing Menu options
    pygame.draw.line(gameDisplay, (50, 50, 50), (640, 675), (1000, 675), 5)

    # Restart
    if pos[0] >= 650 and pos[0] <= 800 and pos[1] >= 685 and pos[1] <= 735:
        pygame.draw.rect(gameDisplay, (100, 100, 100), (650, 685, 150, 50), 0)
    else:
        pygame.draw.rect(gameDisplay, (150, 150, 150), (650, 685, 150, 50), 0)
    pygame.draw.rect(gameDisplay, (50, 50, 50), (650, 685, 150, 50), 3)
    text_surface, rect = Fonts[3].render("Restart", (0, 0, 0))
    gameDisplay.blit(text_surface, (680, 700))

    # Options

    if pos[0] >= 650 and pos[0] <= 800 and pos[1] >= 740 and pos[1] <= 840:
        pygame.draw.rect(gameDisplay, (100, 100, 100), (650, 740, 150, 50), 0)
    else:
        pygame.draw.rect(gameDisplay, (150, 150, 150), (650, 740, 150, 50), 0)
    pygame.draw.rect(gameDisplay, (50, 50, 50), (650, 740, 150, 50), 3)
    text_surface, rect = Fonts[3].render("Options", (0, 0, 0))
    gameDisplay.blit(text_surface, (680, 755))

    # Prestige Shops

    if pos[0] >= 825 and pos[0] <= 975 and pos[1] >= 740 and pos[1] <= 840:
        pygame.draw.rect(gameDisplay, (100, 100, 100), (825, 740, 150, 50), 0)
    else:
        pygame.draw.rect(gameDisplay, (150, 150, 150), (825, 740, 150, 50), 0)
    pygame.draw.rect(gameDisplay, (50, 50, 50), (825, 740, 150, 50), 3)
    text_surface, rect = Fonts[2].render("Prestige Shop", (0, 0, 0))
    gameDisplay.blit(text_surface, (832.5, 755))

    # Demolish Building
    if pos[0] >= 825 and pos[0] <= 975 and pos[1] >= 685 and pos[1] <= 735:
        pygame.draw.rect(gameDisplay, (100, 100, 100), (825, 685, 150, 50), 0)
    else:
        pygame.draw.rect(gameDisplay, (150, 150, 150), (825, 685, 150, 50), 0)
    pygame.draw.rect(gameDisplay, (50, 50, 50), (825, 685, 150, 50), 3)
    text_surface, rect = Fonts[0].render("Demolish Building", (0, 0, 0))
    gameDisplay.blit(text_surface, (832.5, 705))

    # Menu Upgrades(Finishing the game)

    if selection == [-1, -1]:
        Earned = 0
        Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar_Power", "Super_Factory", "Forest Lv1",
                 "Forest Lv2", "Forest Lv3"
            , "Forest Lv4", "Quarry Lv1", "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam", "Water Fish",
                 "Fisherman", "Dam"
            , "CityFar", "CityFac", "Farm"]
        Value = [0, 1, 2, 2, 2, 3, 3, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 2, 1, 1, 2]
        for tileRow in board:
            for tile in tileRow:
                Earned += Value[Tiles.index(tile)]
        Earned += int(ResourceCount["Wood"] / 1000) + int(ResourceCount["Stones"] / 500) + int(
            ResourceCount["Food"] / 200) + \
                  int(ResourceCount["Metal"] / 100) + int(ResourceCount["Electricity"] / 50)

        text_surface, rect = Fonts[5].render(("Rebirth (+" + str(Earned) + ")"), (0, 0, 0))
        gameDisplay.blit(text_surface, (690, 180))
        text_surface, rect = Fonts[5].render(("Cost: "), (0, 0, 0))
        gameDisplay.blit(text_surface, (770, 240))
        text_surface, rect = Fonts[5].render(("1k wood"), (0, 0, 0))
        gameDisplay.blit(text_surface, (750, 280))
        text_surface, rect = Fonts[5].render(("500 stones"), (0, 0, 0))
        gameDisplay.blit(text_surface, (730, 320))
        text_surface, rect = Fonts[5].render(("200 Food"), (0, 0, 0))
        gameDisplay.blit(text_surface, (740, 360))
        text_surface, rect = Fonts[5].render(("100 metal"), (0, 0, 0))
        gameDisplay.blit(text_surface, (740, 400))
        text_surface, rect = Fonts[5].render(("50 electricity"), (0, 0, 0))
        gameDisplay.blit(text_surface, (710, 440))

        if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 550 and pos[1] <= 650:
            pygame.draw.rect(gameDisplay, (150, 0, 0), (725, 550, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (725, 550, 200, 100), 0)

        text_surface, rect = Fonts[5].render(("Unlock"), (0, 0, 0))
        gameDisplay.blit(text_surface, (760, 567))

    return board, ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, Count, Achviements, Mult
