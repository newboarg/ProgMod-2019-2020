### PSEUDOKODE

"""
Pseudokode:
Vi må starte med et ord. Lagre i liste.
Spiller må få vite antall bokstaver.
Variabel som holder styr på antall feil tippinger.
Totalt mulig med 10 feil.

Så lenge vi har gjenstående forsøk:
Spiller gjetter en og en bokstav.
Hvis riktig tippet:
    Gi tilbakemelding med hvor bokstaven finnes
    i ordet.
Hvis ikke:
    Skriv opp "strek".
    Antall gjenstående forsøk reduseres med 1.
"""




### HANGMAN

ordet = "FRIMINUTT" #ordet som skal gjettes
fasit = ordet
ordet = list(ordet)

bokstaver = len(ordet) #antall bokstaver
oversikt = list("_"*bokstaver)

feil = 0 #antall feil som er begått
max_feil = 10 #maksimalt tillatte feil

print(oversikt)

while feil<max_feil:
    gjette = input("Gjett en bokstav! (CAPS ON)")
    
    if gjette in ordet:#riktig gjettet
        while gjette in ordet: #løkke for å få med alle bokstaver i ordet
            
            indeks = ordet.index(gjette)
            oversikt[indeks] = gjette
            ordet[indeks] = "*"
        if "_" not in oversikt:
            print("YOU WINS!")
            break
    else: #feil gjettet
        feil += 1
        print(f"Feil tippet! Du har nå {max_feil-feil} feil å gå på.")
    print(oversikt)
    if feil == max_feil:
        print("You looses!")
print(f"Det riktige ordet var: {fasit}")
