# 24.11.26 Markus Kroon



#Matemaatika test (randint)
#Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
#Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse. Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”, kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
#Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.

import random
a = random.randint(1,10)
b = random.randint(1,10)
tehe = a + b
vastus = int(input(f"{a}+{b}="))
if tehe == vastus:
    print("õige")
else:
    print("vale")







print("--------------------------")







#Sa oled loomas programmi, mis aitab kontrollida, kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
#Programm palub kasutajal sisestada oma vanuse. Kui vanus on vähemalt 18 aastat, siis programm annab teada, et kasutaja võib üritusele siseneda. Kui vanus on alla 18, siis programm teatab, et üritusele sisenemiseks ei ole piisavalt vana.
#Kasuta if ja else lauseid, et luua see vanusekontrolli programm.

vanus = int(input("Sisesta vanus: "))

if vanus < 18:
    print("Ei saa")
else:
    print("OK")