import pandas as pd
import numpy as np
import random
streets = ["Oak St", "Pine St", "Main St", "Cedar Ln", "Maple Ave"]
cities = ["Springfield", "Lexington", "Riverside", "Orlando", "Denver", "Portland", "Baltimore", "Charleston", "Providence", "Madison", "Austin", "Phoenix", "Raleigh", "Manchester", "Honolulu", "Boise", "Lincoln", "Fargo", "Salem", "Harrisburg", "Baton Rouge", "Columbia", "Des Moines", "Little Rock", "Salt Lake City", "Augusta"]
states = ["IL", "KY", "CA", "FL", "CO", "OR", "MD", "WV", "RI", "WI", "TX", "AZ", "NC", "NH", "HI", "ID", "NE", "ND", "OR", "PA", "LA", "SC", "IA", "AR", "UT", "ME"]
zip_codes = ["62701", "40502", "92501", "32801", "80202", "97201", "21201", "25301", "02901", "53703", "78701", "85001", "27601", "03101", "96801", "83702", "68102", "58102", "97301", "17101", "70801", "29201", "50309", "72201", "84101", "04330"]
names = ["John", "Michael", "Robert", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher",
            "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth", "George",
            "Joshua", "Kevin", "Brian", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Gary", "Jacob",
            "Nicholas", "Eric", "Stephen", "Jonathan", "Larry", "Justin", "Scott", "Brandon", "Frank", "Benjamin",
            "Gregory", "Raymond", "Samuel", "Patrick", "Alexander", "Jack", "Dennis", "Jerry", "Tyler", "Aaron",
            "Henry", "Jose", "Douglas", "Peter", "Adam", "Nathan", "Zachary", "Walter", "Kyle", "Harold", "Carl",
            "Jeremy", "Keith", "Roger", "Gerald", "Ethan", "Arthur", "Terry", "Christian", "Sean", "Lawrence",
            "Austin", "Joe", "Noah", "Jesse", "Albert", "Bryan", "Billy", "Bruce", "Willie", "Jordan", "Dylan",
            "Alan", "Ralph", "Gabriel", "Roy", "Juan", "Wayne", "Eugene", "Logan", "Randy", "Louis", "Russell", "Vincent"]
surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
            "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
            "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright",
            "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez",
            "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez",
            "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson",
            "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly",
            "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry",
            "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales"]
df = pd.DataFrame(columns=["IIN", "NAME", "SURNAME", "BIRTHDATE", "GENDER", "ADDRESS", "RANK", "STATUS", "COMMANDER_IIN", "HIRE_DATE", "CONTRACT_TYPE", "REBUKES"])
iin1 = ["75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "00", "01", "02", "03", "04"]
iin2 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
iin3 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
for i in range(56):
    a = iin1[random.randint(0, len(iin1) - 1)]
    b = iin2[random.randint(0, len(iin2) - 1)]
    c = iin3[random.randint(0, len(iin3) - 1)]
    if b in ["02"] and c in ["31", "30", "29"]:
        c = "28"
    elif b in ["04", "06", "09", "11"] and c == "31":
        c = "30"
    d = random.randint(0, 999)
    if d < 100 and d > 9: d = "0" + str(d)
    elif d < 10: d = "00" + str(d)
    else: d = str(d)
    e = random.randint(0, 999)
    if e < 100 and e > 9: e = "0" + str(e)
    elif e < 10: e = "00" + str(e)
    else: e = str(e)
    iin = (a + b + c + d + e)
    name = names[random.randint(0, 94)]
    surname = surnames[random.randint(0, 93)]
    rank = np.nan
    com_iin = np.nan
    con_type = np.nan
    if len(iin) == 11: iin = "0" + iin
    elif len(iin) == 10: iin = "00" + iin
    birth_date = f"{iin[4:6]}/{iin[2:4]}/{iin[0:2]}"
    address = f"{random.choice(streets)}, {random.choice(cities)}, {random.choice(states)} {random.choice(zip_codes)}"
    rebukes = random.randint(0, 2)
    df.loc[len(df)] = [iin, name, surname, birth_date, "MALE", address, rank, "FREE", com_iin, "10/03/2023", con_type, rebukes]
f = random.randint(0, 56)
df['RANK'][f] = 'WARRANT'
changed = [f]
for i in range(5):
    g = random.randint(0, 56)
    while g in changed:
        g = random.randint(0, 56)
    changed.append(g)
    df['RANK'][g] = 'STAFF SERGEANT'
    df['COMMANDER_IIN'][g] = df['IIN'][f]
    for k in range(10):
        l = random.randint(0, 56)
        while l in changed:
            l = random.randint(0, 56)
        changed.append(l)
        df['RANK'][l] = 'PRIVATE'
        df['COMMANDER_IIN'][l] = df['IIN'][g]
for i in range(56):
    if(df['RANK'][i] == 'PRIVATE'):
        df['CONTRACT_TYPE'][i] = 'PRACTICANT'
    else:
        df['CONTRACT_TYPE'][i] = 'STAFF'
print(df)
df.to_csv("C:\\Users\\Rakon\\Desktop\\SQL\\Medics.csv")