# 19.11.26 Markus Koon

#Ülessanne 3.7: Python turtle kolmnurk
import turtle
kylg = 300
nurk = 120
varv = "red"

turtle.color(varv)
for i in range (3):
    turtle.fd(kylg)
    turtle.lt(nurk)
turtle.done()


#Ülessanne 3.3: Reisiplaan
sk ="Haapsalu"
pa = 4
hind = 15.6
print(sk,"reis kestab",pa,"päeva ja üks öö maksab",hind,"eurot.")



#Ülesanne 3.2: Ostunimekiri
toode = "Sussid"
kogus =  10
hind = 1.10
print("Soovin " + toode + " " + str(kogus) + " , mille tüki hind on "+str(hind)+" eurot.")

#Ülessanne 3.1: Tervitus
nimi = "Markus"
vanus = 16
keskmine_hinne = 5.0
print(nimi,vanus,keskmine_hinne)