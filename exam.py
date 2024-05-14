import pandas as pd
import numpy as np
import random
df1 = pd.read_csv("C:\\Users\\Rakon\\Desktop\\SQL\\ExamResults.csv")
df = pd.DataFrame(columns=["IIN", "NAME", "SURNAME", "WEIGHT", "HEIGHT", "100M", "6KM", "SHOOTING", "PULLUPS", "PSYCHOTEST"])
for i in range(300):
    iin = str(df1["IIN"][i])
    if len(iin) == 11: iin = "0" + iin
    elif len(iin) == 10: iin = "00" + iin
    elif len(iin) == 9: iin = "000" + iin
    name = df1["NAME"][i]
    surname = df1["SURNAME"][i]
    weight = df1["WEIGHT"][i]
    height = df1["HEIGHT"][i]
    hun = df1["100M"][i]
    six = df1["6KM"][i]
    shooting = df1["SHOOTING"][i]
    pull = df1["PULLUPS"][i]
    psychotest = "PASSED"
    df.loc[len(df)] = [iin, name, surname, weight, height, hun, six, shooting, pull, psychotest]
df.to_csv("C:\\Users\\Rakon\\Desktop\\SQL\\ExamResults.csv")
print(df)