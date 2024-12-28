import random

# Create a pool of units
pool = []

cost1 = []
cost1_units = ["Amumu", "Darius", "Draven", "Irelia", "Lux", "Maddie", "Morgana", "Powder", "Singed", "Steb", "Trundle", "Vex", "Violet", "Zyra"]
for unit in cost1_units:
    for i in range(30):
        cost1.append(unit)

cost2 = []
cost2_units = ["Akali", "Camille", "Leona", "Nocturne", "Rell", "Renata", "Sett", "Tristana", "Urgot", "Vander", "Vladimir", "Zeri", "Ziggs"]
for unit in cost2_units:
    for i in range(25):
        cost2.append(unit)

cost3 = []
cost3_units = ["Blitzcrank", "Cassiopeia", "Ezreal", "Gangplank", "Kogmaw", "Loris", "Nami", "Nunu", "Renni", "Scar", "Smeech", "Swain", "Twisted Fate"]
for unit in cost3_units:
    for i in range(18):
        cost3.append(unit)

cost4 = []
cost4_units = ["Ambessa", "Corki", "Dr Mundo", "Ekko", "Elise", "Garen", "Heimerdinger", "Illaoi", "Silco", "Twitch", "Vi", "Zoe"]
for unit in cost4_units:
    for i in range(10):
        cost4.append(unit)

cost5 = []
cost5_units = ["Caitlyn", "Jayce", "Jinx", "Leblanc", "Malzahar", "Mordekaiser", "Rumble", "Sevika"]
for unit in cost5_units:
    for i in range(9):
        cost5.append(unit)

pool.append(cost1)
pool.append(cost2)
pool.append(cost3)
pool.append(cost4)
pool.append(cost5)



# Chance at Level 1
# 1-cost : 100%
# 2-cost : 0%
# 3-cost : 0%
# 4-cost : 0%
# 5-cost : 0%

# Chance at Level 2
# 1-cost : 100%
# 2-cost : 0%
# 3-cost : 0%
# 4-cost : 0%
# 5-cost : 0%

# Chance at Level 3
# 1-cost : 75%
# 2-cost : 25%
# 3-cost : 0%
# 4-cost : 0%
# 5-cost : 0%

# Chance at Level 4
# 1-cost : 55%
# 2-cost : 30%
# 3-cost : 15%
# 4-cost : 0%
# 5-cost : 0%

# Chance at Level 5
# 1-cost : 45%
# 2-cost : 33%
# 3-cost : 20%
# 4-cost : 2%
# 5-cost : 0%

# Chance at Level 6
# 1-cost : 30%
# 2-cost : 40%
# 3-cost : 25%
# 4-cost : 5%
# 5-cost : 0%

# Chance at Level 7
# 1-cost : 19%
# 2-cost : 30%
# 3-cost : 35%
# 4-cost : 10%
# 5-cost : 1%

# Chance at Level 8
# 1-cost : 18%
# 2-cost : 25%
# 3-cost : 32%
# 4-cost : 22%
# 5-cost : 3%

# Chance at Level 9
# 1-cost : 10%
# 2-cost : 20%
# 3-cost : 25%
# 4-cost : 35%
# 5-cost : 10%

# Chance at Level 10
# 1-cost : 5%
# 2-cost : 10%
# 3-cost : 20%
# 4-cost : 40%
# 5-cost : 25%


level_chance = [[100,0,0,0,0], [100,0,0,0,0], [75,25,0,0,0], [55,30,15,0,0], [45,33,20,2,0], [30,40,25,5,0], [19,30,35,10,1], [18,25,32,22,3], [10,20,25,35,10], [5,10,20,40,25]]


def chance_to_get_cost(level):
    num = random.randint(0, 100)
    if num < level_chance[level-1][0]:
        return 1
    elif num < level_chance[level-1][0] + level_chance[level-1][1]:
        return 2
    elif num < level_chance[level-1][0] + level_chance[level-1][1] + level_chance[level-1][2]:
        return 3
    elif num < level_chance[level-1][0] + level_chance[level-1][1] + level_chance[level-1][2] + level_chance[level-1][3]:
        return 4
    elif num < level_chance[level-1][0] + level_chance[level-1][1] + level_chance[level-1][2] + level_chance[level-1][3] + level_chance[level-1][4]:
        return 5
    else:
        return chance_to_get_cost(level)


def get_unit(level):
    cost = chance_to_get_cost(level)  
    return f"{cost} {random.choice(pool[cost-1])}"



# Manual Test
print()
level = int(input("Enter your level : "))  
print()

if level < 1 or level > 10:
    print("Invalid level")
    print()
    exit()
else:
    while True:
        reroll = input("Do you want to reroll? (y/n): ")
        if reroll.lower() == "y":
            for i in range(5):
                print(get_unit(level))  
            print()
        else:
            break