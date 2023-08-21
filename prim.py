def primzahl(nummber):
    if nummber < 2:
        return False
    for i in range(2, int(nummber ** 0.5) + 1):
        if nummber % i == 0:
            return False
    return True

eingabe = int(input("Enter a number: "))
primzahlen = []
for x in range(2, eingabe):
    if primzahl(x):
        primzahlen.append(x)
print(primzahlen)

import time
starttime = time.time()

calculationtime = time.time()

printtime = time.time()
print(f"Took {calculationtime - starttime} Seconds to Calculate, {calculationtime - printtime} to print to Screen. ({printtime - starttime} total)")
