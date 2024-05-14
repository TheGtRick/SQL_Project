import pandas as pd
import numpy as np
import random
df1 = pd.read_csv("C:\\Users\\Rakon\\Desktop\\SQL\\Medics.csv")
df = pd.DataFrame(columns=["IIN", "NAME", "SURNAME", "FATHER_NAME", "BIRTHDATE", "GENDER", "FAMILY", "ADDRESS", "RANK", "STATUS", "COMMANDER_IIN", "HIRE_DATE", "CONTRACT_TYPE", "REBUKES", "SALARY"])
for i in range(56):
    iin = str(df1["IIN"][i])
    if len(iin) == 11: iin = "0" + iin
    elif len(iin) == 10: iin = "00" + iin
    elif len(iin) == 9: iin = "000" + iin
    if i != 37:
        com_iin = str(int(df1["COMMANDER_IIN"][i]))
        if len(com_iin) == 11: com_iin = "0" + com_iin
        elif len(com_iin) == 10: com_iin = "00" + com_iin
        elif len(com_iin) == 9: com_iin = "000" + com_iin
    name = df1["NAME"][i]
    surname = df1["SURNAME"][i]
    faher_name = df1["FATHERNAME"][i]
    birth = df1["BIRTHDATE"][i]
    gender = df1["GENDER"][i]
    family = df1["FAMILY"][i]
    address = df1["ADDRESS"][i]
    rank = df1["RANK"][i]
    status = df1["STATUS"][i]
    hire = df1["HIRE_DATE"][i]
    con_type = df1["CONTRACT_TYPE"][i]
    rebukes = df1["REBUKES"][i]
    salary = df1["SALARY"][i]
    df.loc[len(df)] = [iin, name, surname, faher_name, birth, gender, family, address, rank, status, com_iin, hire, con_type, rebukes, salary]
print(df)
df.to_csv("C:\\Users\\Rakon\\Desktop\\SQL\\Medics.csv")