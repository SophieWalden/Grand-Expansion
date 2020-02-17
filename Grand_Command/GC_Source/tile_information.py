from gc_game_data import *

def draw(x, y, Obj, Type, height, width, Images, AnimationStage, Count):
    global MaterialProduction
    if Obj == "Tile":
        if Type == "Grass":
            pygame.draw.rect(gameDisplay, (0, 128, 0), (x, y, (640 / width), (640 / height)), 0)
        if Type.find("Water") != -1:

            # Animation 4 water
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
            # Animation 4 Dam
            if AnimationStage["Dam"][0] == 1:
                gameDisplay.blit(Images["Dam1"], (x, y))
            if AnimationStage["Dam"][0] == 2:
                gameDisplay.blit(Images["Dam2"], (x, y))
            if AnimationStage["Dam"][1] <= 0:
                AnimationStage["Dam"][0] += 1
                AnimationStage["Dam"][1] = 0.5
                if AnimationStage["Dam"][0] == 3:
                    AnimationStage["Dam"][0] = 1
            else:
                AnimationStage["Dam"][1] -= 0.05 / Count["Dam"]

        # Tile Texture
        if Type == "Quarry Lv1":
            gameDisplay.blit(Images["Quarry1"], (x, y))
        if Type == "Quarry Lv2":
            gameDisplay.blit(Images["Quarry2"], (x, y))
        if Type == "Quarry Lv3":
            gameDisplay.blit(Images["Quarry3"], (x, y))
        if Type == "Quarry Lv4":
            gameDisplay.blit(Images["Quarry4"], (x, y))


        if Type == "Forest Lv1":
            gameDisplay.blit(Images["Forest1"], (x, y))
        if Type == "Forest Lv2":
            gameDisplay.blit(Images["Forest2"], (x, y))
        if Type == "Forest Lv3":
            gameDisplay.blit(Images["Forest3"], (x, y))
        if Type == "Forest Lv4":
            gameDisplay.blit(Images["Forest4"], (x, y))


       # Farm -> Town
        if Type == "Farm":
            gameDisplay.blit(Images["Farm"], (x, y))
        if Type == "town_00":
            gameDisplay.blit(Images["town_00"], (x, y))
        if Type == "town_01":
            gameDisplay.blit(Images["town_01"], (x, y))
        if Type == "town_02":
            gameDisplay.blit(Images["town_02"], (x, y))
        if Type == "town_03":
            gameDisplay.blit(Images["town_03"], (x, y))
        if Type == "town_04":
            gameDisplay.blit(Images["town_04"], (x, y))
        if Type == "town_05":
            gameDisplay.blit(Images["town_05"], (x, y))
        if Type == "City_00":
            gameDisplay.blit(Images["City_00"], (x, y))


        if Type.find("Factory ") != -1 or Type == "Factory":
            gameDisplay.blit(Images["Factory"], (x, y))

        # Military
        if Type == "barracks":
            gameDisplay.blit(Images["barracks"], (x, y))

        # Military Units
        if Type == "squad_trail_fireteam":
            gameDisplay.blit(Images["squad_trail_fireteam"], (x, y))


        if Type == "Fisherman":
            gameDisplay.blit(Images["Fisherman"], (x, y))

        if Type == "Solar Power":
            gameDisplay.blit(Images["Solar power"], (x, y))
        if Type == "Super Factory":
            gameDisplay.blit(Images["Super Factory"], (x, y))

        # Tile Border
        pygame.draw.rect(gameDisplay, (50, 50, 50), (x, y, (640 / width), (640 / height)), 1)