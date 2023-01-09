x1 = int(input("Zadej x souřadnici 1. bodu: "))
y1 = int(input("Zadej y souřadnici 1. bodu: "))
x2 = int(input("Zadej x souřadnici 2. bodu: "))
y2 = int(input("Zadej y souřadnici 2. bodu: "))
b3 = 0

#Použité výpočty (lineární funkce)
# a = (y2 - y1) / (x2 - x1)																#Výpočet "a" v lineární funkci
# b = y1 - a * x1																		#Výpočet "b" v lineární funkci
# y = b																					#Pro x = 0
# x = (-b) / a																			#Pro y = 0

if x1 > x2:
	if (y1 > y2):
		if ((x1 - x2) > x1 or (x1 - x2) > x2) and ((y1 - y2) > y1 or (y1 - y2) > y2):	#Jestli úsečka protíná 3 kvadranty (Zde je jasné, že úsečka musí začínát v 1. kvadrantu a končit ve 3., pouze se určuje přes který kvadrant směřuje)
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) > 0:									#Jestli je v bodě x = 0 y-ová osa větší než 0 (V podmínce je rozepsaný výpočet pro "y")
				b3 = 2
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) == 0:								#Jestli je v bodě x = 0 y-ová osa 0
				b3 = "počátek"
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) < 0:									#Jestli je v bodě x = 0 y-ová osa menší než 0
				b3 = 4
	if (y2 > y1):
		if ((x1 - x2) > x1 or (x1 - x2) > x2) and ((y2 - y1) > y1 or (y2 - y1) > y2):	#Jestli úsečka protíná 3 kvadranty (Zde je jasné, že úsečka musí začínát ve 4. kvadrantu a končit ve 2., pouze se určuje přes který kvadrant směřuje)
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) > 0:									#Jestli je v bodě x = 0 y-ová osa větší než 0 (V podmínce je rozepsaný výpočet pro "y")
				b3 = 1
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) == 0:								#Jestli je v bodě x = 0 y-ová osa 0
				b3 = "počátek"
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) < 0:									#Jestli je v bodě x = 0 y-ová osa menší než 0
				b3 = 3
if x2 > x1:
	if (y1 > y2):
		if ((x2 - x1) > x1 or (x2 - x1) > x2) and ((y1 - y2) > y1 or (y1 - y2) > y2):	#Jestli úsečka protíná 3 kvadranty (Zde je jasné, že úsečka musí začínát v 2. kvadrantu a končit ve 4., pouze se určuje přes který kvadrant směřuje)
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) > 0:									#Jestli je v bodě x = 0 y-ová osa větší než 0 (V podmínce je rozepsaný výpočet pro "y")
				b3 = 1
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) == 0:								#Jestli je v bodě x = 0 y-ová osa 0
				b3 = "počátek"
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) < 0:									#Jestli je v bodě x = 0 y-ová osa menší než 0
				b3 = 3
	if (y2 > y1):
		if ((x2 - x1) > x1 or (x2 - x1) > x2) and ((y2 - y1) > y1 or (y2 - y1) > y2):	#Jestli úsečka protíná 3 kvadranty (Zde je jasné, že úsečka musí začínát v 3. kvadrantu a končit ve 1., pouze se určuje přes který kvadrant směřuje)
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) > 0:									#Jestli je v bodě x = 0 y-ová osa větší než 0 (V podmínce je rozepsaný výpočet pro "y")
				b3 = 2
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) == 0:								#Jestli je v bodě x = 0 y-ová osa 0
				b3 = "počátek"
			if (y1 - ((y2 - y1) / (x2 - x1)) * x1) < 0:									#Jestli je v bodě x = 0 y-ová osa menší než 0
				b3 = 4

if ((x1 > 0) and (y1 > 0)):
    b1 = 1
if ((x1 > 0) and (y1 < 0)):
    b1 = 4
if ((x1 < 0) and (y1 > 0)):
    b1 = 2
if ((x1 < 0) and (y1 < 0)):
    b1 = 3

if ((x2 > 0) and (y2 > 0)):
    b2 = 1
if ((x2 > 0) and (y2 < 0)):
    b2 = 4
if ((x2 < 0) and (y2 > 0)):
    b2 = 2
if ((x2 < 0) and (y2 < 0)):
    b2 = 3

if b3 == "počátek":
	print("Úsečka začíná v",b1,"kvadrantu, pokračuje přes",b3,"a končí v",b2,"kvadrantu")
if ((b3 == 1 or b3 == 2 or b3 == 3 or b3 == 4) and b3 != "počátek"):
	print("Úsečka začíná v",b1,"kvadrantu, pokračuje přes",b3,"kvadrant a končí v",b2,"kvadrantu")
if (b3 != 1 and b3 != 2 and b3 != 3 and b3 != 4 and b3 != "počátek"):
	print("Úsečka začíná v",b1,"kvadrantu a končí v",b2,"kvadrantu")