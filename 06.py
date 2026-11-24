#24.11.26 Markus
#Kasuta Python Turtles’i, et joonistada stseen, kus redel toetub majale 53° nurga all. Redeli ülemine ots peaks ulatuma 4,4 meetri kõrgusele maja seinal virtuaalses mõõtkavas.
#Muuda nurgad radiaanideks (radian)
#Redeli kaugus seinast: kasuta tangensfunktsiooni (tan) ja antud nurka, et leida, kui kaugele redeli alumine ots on seinast. Valem: Kaugus=Kõrgus_seinal/tan⁡(Nurk)
#Redeli pikkus: kasuta Pythagorase teoreemi, et leida redeli pikkus, kui tead redeli kõrgust seinal ja kaugust seinast. Valem: Pikkus=(Kõrgus seinal)2+(Kaugus_seinast)2
#Ümarda vastus 2 komakohta
#Kuva vastused konsoolid

import math
import turtle
nurk = math.tan(53)
h = 4.4
kaugus = abs(h/nurk)
pikkus = math.sqrt((h**2)+(kaugus**2))


print(f"Kaugus: {kaugus:.2f}, pikkus: {pikkus:.2f}")
kordaja = 30
turtle.fd(kaugus*kordaja)
turtle.lt(90)
turtle.fd(h*kordaja)
turtle.lt(113.5) #ei tea kust tuleb
turtle.fd(pikkus*kordaja)
turtle.done