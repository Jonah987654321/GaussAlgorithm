eq1 = [2, -4, 5, 3]
eq2 = [3, 3, 7, 13]
eq3 = [4, -2, -3, -1]

start_eq1 = eq1.copy()
start_eq2 = eq2.copy()
start_eq3 = eq3.copy()

i = 0
for num in eq3:
    eq3[i] = num*start_eq2[0]
    i += 1

i = 0
for num in eq2:
    eq2[i] = num*start_eq3[0]
    i += 1

if eq3[0] == eq2[0]:
    i = 0
    for num in eq3:
        eq3[i] = num*(-1)
        i += 1
i = 0
for num in eq3:
    eq3[i] = num+eq2[i]
    i += 1
#########################################
last_eq1 = eq1.copy()
last_eq2 = eq2.copy()
last_eq3 = eq3.copy()
i = 0
for num in eq2:
    eq2[i] = num*last_eq1[0]
    i += 1

i = 0
for num in eq1:
    eq1[i] = num*last_eq2[0]
    i += 1

if eq1[0] == eq2[0]:
    i = 0
    for num in eq2:
        eq2[i] = num*(-1)
        i += 1
i = 0
for num in eq2:
    eq2[i] = num+eq1[i]
    i += 1
############################################
last_eq1 = eq1.copy()
last_eq2 = eq2.copy()
last_eq3 = eq3.copy()
i = 0
for num in eq3:
    eq3[i] = num*last_eq2[1]
    i += 1

i = 0
for num in eq2:
    eq2[i] = num*last_eq3[1]
    i += 1

if eq3[1] == eq2[1]:
    i = 0
    for num in eq3:
        eq3[i] = num*(-1)
        i += 1
i = 0
for num in eq3:
    eq3[i] = num+eq2[i]
    i += 1
try:
    z = eq3[3]/eq3[2]
    print(z)
    eq2[3] = eq2[3]-(eq2[2]*z)
    eq2[2] = 0
    y = eq2[3]/eq2[1]
    print(y)
    eq1[3] = eq1[3]-(eq1[2]*z)-(eq1[1]*y)
    eq1[1] = 0
    eq1[2] = 0
    x = eq1[3]/eq1[0]
    print(x)
except ZeroDivisionError:
    print("Unendlich viele Lösung!")