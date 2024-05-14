import pandas as pd
import numpy as np
import random
df = pd.DataFrame(columns=["EQUIPMENT_ID", "EQUIPMENT_NAME", "PRODUCTION_YEAR", "MADE_IN", "STATUS"])
country = ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia']
equipments = ["AK-47", "M4 Carbine", "FN SCAR", "H&K G36", "Steyr AUG", "Tavor X95", "Pistol", "Grenade", "Body Armor (Bronezhilet)", "Helmet", "Night Vision Goggles", "Combat Boots", "Medic Kit", "Tactical Backpack", "Handheld Radio", "Gas Mask", "Ammunition", "Rations", "Canteen"]
for i in range(1000):
    id = i
    name = random.choice(equipments)
    year = random.randint(1980, 2020)
    made = random.choice(country)
    status = "FREE"
    df.loc[len(df)] = [id, name, year, made, status]
a = []
for i in range(200):
    h = random.randint(0, 350)
    a.append(h)
    df.loc[h, "STATUS"] = "ON MISSION"
print(df)
print(a)
df.to_csv("C:\\Users\\Rakon\\Desktop\\SQL\\Equipments.csv")