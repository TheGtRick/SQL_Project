import pandas as pd
import numpy as np
import random
a = [133, 286, 181, 294, 93, 153, 239, 161, 134, 175, 50, 298, 242, 89, 18, 137, 99, 107, 229, 153, 28, 114, 180, 292, 245, 24, 144, 324, 41, 13]
df = pd.DataFrame(columns=["VECHICLE_ID", "MISSION_ID"])
for i in range(len(a)):
    df.loc[len(df)] = [a[i], random.randint(1,10)]
print(df)
df.to_csv("C:\\Users\\Rakon\\Desktop\\SQL\\VechiclesM.csv")
