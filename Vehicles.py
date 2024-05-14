import pandas as pd
import numpy as np
import random
df = pd.DataFrame(columns=["Vechicle_ID", "Vechicle_Name", "Vechicle_Type", "Production_Year", "Made_In", "STATUS"])
air = ['Fighter Jet', 'Helicopter', 'Cargo Plane', 'Drone', 'Blimp', 'Stealth Bomber']
navi = ['Aircraft Carrier', 'Submarine', 'Destroyer', 'Frigate', 'Patrol Boat', 'Hovercraft']
land = ['Tank', 'Armored Personnel Carrier', 'Jeep', 'Humvee', 'APC (Armored Fighting Vehicle)', 'Rocket Launcher Truck', 'Motorcycle', 'ATV (All-Terrain Vehicle)']
country = ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia']
for i in range(1, 51):
    df.loc[len(df)] = [i, random.choice(air), "AIR", random.randint(1980, 2020), random.choice(country), "FREE"]
for i in range(51, 121):
    df.loc[len(df)] = [i, random.choice(navi), "NAVI", random.randint(1980, 2020), random.choice(country), "FREE"]
for i in range(121, 351):
    df.loc[len(df)] = [i, random.choice(land), "LAND", random.randint(1980, 2020), random.choice(country), "FREE"]
print(df)
a = []
for i in range(30):
    h = random.randint(0, 350)
    a.append(h)
    df.loc[h, "Mission_ID"] = "ON MISSION"
df.to_csv("C:\\Users\\Rakon\\Desktop\\SQL\\Vechicles.csv")
print(a)