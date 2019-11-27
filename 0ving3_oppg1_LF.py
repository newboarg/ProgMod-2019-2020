# FUNKSJONER

def faktorer(x, reverse = 1):
    """
    Denne funksjonen returnerer alle faktorene til et argument x.
    Argumentet reverse avgjør om faktorene returneres i stigende (reverse=0)
    eller synkende (reverse=1, default) rekkefølge.
    """
    
    faktorer = [] # lager en tom liste for å lagre faktorene i
    
    for i in range(1,x+1): # sjekker alle tall fra 1 til x 
        if x%i==0:
            faktorer.append(i) # legger til tall som deler x med 0 i rest i lista over faktorer
    """
    MERK: vi trenger egentlig bare å sjekke opp til x/2 (for partall) 
    eller til x/3 (for oddetall). Hvorfor?
    """

    if reverse:
        faktorer.reverse() # reverserer lista med faktorer
        
    return(faktorer) 


def isPrime(x):
    """
    Funksjon for å sjekke om et tall x er et primtall. Returnerer True eller False.
    """
    
    f=faktorer(x)
    return(len(f)==2) #hvis det er bare to faktorer (1 og tallet selv) er x et primtall


def primtallsum(sum):
    """Denne funksjonen finner og summerer primtall fra 2 og oppover helt til
    summen blir større enn argumentet sum.
    Returnerer antall primtall som summeres.
    """
    
    s = 0 # variabel for å holde sum av primtall
    i = 2 # indeksvariabel for å sjekke primtall
    
    primtall = [] # oppretter en tom liste for å lagre primtall

    while s<sum:
        if isPrime(i):
            primtall.append(i) # hvis i er et primtall økes s med i
            s += i
        i += 1 # i økes med 1 for hver gjennomgang av while-løkka
        
    for index, prime in enumerate(primtall): # går gjennom alle elementer i primtallslista
        if isPrime(index):
            print(prime) # printer ut primtallet hvis indeksen i lista er et primtall 
    return(len(primtall))



# HOVEDSKRIPT

sum = 20
antall = primtallsum(sum) # antall blir antallet primtall som tas med for å få en sum større enn variabelen sum

print(f"Antall primtall for å nå en primtallsum på {sum}: {primtallsum(sum)}") # output
