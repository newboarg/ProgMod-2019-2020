import numpy as np
from matplotlib import pyplot as plt

def f_derivert(ft):
    return(0.187*ft) #ft angir funksjonsverdien for en gitt t: f(t)

t_0 = 0 # startverdi for t (initialbetingelse)
f_0 = 9 # startverdi for f (initialbetingelse)
t_slutt = 60 # sluttverdi for t

N = 61 # antall steg
h = (t_slutt-t_0)/(N-1) # regner ut steglengden

t = np.linspace(t_0, t_slutt, N) # lager et array for verdier av t fra startverdi til sluttverdi
f = np.zeros(N) # lager et array for å lagre verdier for f
f[0] = f_0 # initialbetingelse


#Eulers metode
for i in range(N-1):
    f[i+1] = f[i] + f_derivert(f[i])*h # bruker formel for å regne ut "neste steg" 

plt.figure(figsize=(12,5))
plt.plot(t, f, 'o-') # plotter løsningen
plt.title("Enkel modell for COVID19-spredning")
plt.ylabel("Antall registrerte tilfeller")
plt.xlabel("Dager etter 22. januar 2020")
plt.ylim([-1e4,3e5])
plt.grid()
