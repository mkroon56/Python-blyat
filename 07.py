#24.11.26












#minu album
album = ["1. ALIKA – “Bridges", "2. Anett x Fredi – “Read Between The Lines”", "3. villemdrillem – “leekiv armastus”", "4. Clicherik & Mäx – “PAKSUD”", "5. nublu – “ära ärata”", "6. NOËP – “Move Your Feet”", "7. Trad.Attack! – “Bring It On”", "8. Bedwetters – “It Is What It Is”", "9. Reket – “Panama paberid”", "10. Grete Paia – “Võluväel”"]

#kuvab koik lood
for lugu in album:
    print(lugu)


#küsin kasutajalt loo numbrit
valik = int(input("Vali lugu: "))
print("------------------------")
#kuvan valiku ja korrigeerin -1
print(album[valik-1])