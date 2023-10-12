import gspread
import numpy as np
gc = gspread.service_account(filename='unitydatascience-400508-8b6b2fc9e349.json')
sh = gc.open("UnityWorkshop2")
damage = np.random.randint(1, 50, 11)
mon = list(range(1,11))
i = 0
while i <= len(mon):
    i += 1
    if i == 0:
        continue
    else:
        sh.sheet1.update(('A' + str(i)), str(i))
        sh.sheet1.update(('B' + str(i)), str(damage[i-1]))
        sh.sheet1.update(('C' + str(i)), str(100-damage[i-1]))
        print(damage)
