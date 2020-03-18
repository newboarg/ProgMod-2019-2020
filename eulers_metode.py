import numpy as np
from matplotlib import pyplot as plt

def f_derivert(t):
    """Funksjon som returnerer den deriverte i henhold til oppgitt difflikning."""
    return(2*t)

t_0 = 0 # startverdi for t (initialbetingelse)
f_0 = 0 # startverdi for f (initialbetingelse)
t_slutt = 2 # sluttverdi for t

N = 1000 # antall steg
h = (t_slutt-t_0)/(N-1) # regner ut steglengden

t = np.linspace(t_0, t_slutt, N) # lager et array for verdier av t fra startverdi til sluttverdi
f = np.zeros(N) # lager et array for å lagre verdier for f
f[0] = f_0 # initialbetingelse


#Eulers metode
for i in range(N-1):
    f[i+1] = f[i] + f_derivert(t[i])*h # bruker formel for å regne ut "neste steg" 

    
plt.plot(t, f) # plotter løsningen
plt.title(r"Løsning av $f'(t)=2t$ med $f(0)=0$")
plt.xlabel(r"$t$")
plt.ylabel(r"$f(t)$")
