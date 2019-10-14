### EKSEMPEL 1 - looping i løkker

tekst = "Programmering"
#print(tekst)
#print(type(tekst))

a = list(tekst)

#print(a)

# metode 1: tellevariabel som indeks
for i in range(len(a)):
    print(i) #printe tellevariabel
    print(a[i])#printer element i fra a

# metode 2: enumerate
for e in enumerate(a):
    print(e) #printer enumerate-objekt (indeks og )
    #print(e[0]) #printer indeksen
    #print(e[1]) #printer verdien

#metode 3: enumerate versjon 2

for i, e in enumerate(a):
    #print(i) #indekser
    print(e) #verdier i lista
"""

#metode 4: elementer i lista direkte
for item in a:
    print(item)



### EKSEMPEL 2 - splitting av strings til lister

tekst = "Programmering er ikke veldig vanskelig, eller?"

a = tekst.split()

print(a)

for e in enumerate(a):
    print(f"Indeks: {e[0]}, Verdi: {e[1]}")
    
    
    
### EKSEMPEL 3 - matematikk med listeelementer

tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
partall = [] 


#ei liste vi vil bruke til å samle partall

for x in tall: #bruker elementer i ei liste
    if x%2==0: #partall
        partall.append(x)

print(partall)

#DOBLING AV LISTA
print(tall*2) # gir to lister etter hverandre

dobling = tall

for i, e in enumerate(tall):
    #dobler hvert element i tall og lagrer det 
    #i lista dobling
    dobling[i] = tall[i] * 2
    
print(dobling)
    
    
    
    
