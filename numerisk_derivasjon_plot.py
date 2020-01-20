import numpy as np
from matplotlib import pyplot as plt
 
def f(x): # lager en funksjon for en funksjon
    return(((x-0.5)**2))
 
def derivert(f, x, h): # definerer en funksjon for den deriverte
    return((f(x+h) - f(x))/h) # bruker Newtons kvotient
 
N = 100 # antall punkter
h = 0.001 # h-verdi for Newtons metode
xmin = -2
xmax = 2
xes = np.linspace(xmin, xmax, N) # lager et array med N x-verdier fra xmin til xmax
 
func = f(xes) # lager et nytt array med funksjonsverdier definert av f
 
df = derivert(f, xes, h) # lager et array med verdier for den deriverte av f
 
plt.plot(xes, func, label = "f(x)") # plotter f(x)
plt.plot(xes, df, label = "f'(x)")# plotter f'(x)
plt.xlabel("x")
plt.grid("both")
plt.legend()
