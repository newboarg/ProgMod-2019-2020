import numpy as np
from matplotlib import pyplot as plt

def f(x): # lager en funksjon for en funksjon
    return(((x-0.5)**2))

def derivert(f, x, h): # definerer en funksjon for den deriverte
    return((f(x+h) - f(x))/h) # bruker Newtons kvotient

h = 0.01 # avstanden i Newtons kvotient
xmin = -2 # startverdi for x
xmax = 2 # sluttverdi for x
N = int((xmax - xmin)/h) + 1 # antall x-verdier
xes = np.linspace(xmin, xmax, N) # lager et array med N x-verdier fra xmin til xmax

func = f(xes) # lager et nytt array med funksjonsverdier definert av f
df = derivert(f, xes, h) # lager et array med verdier for den deriverte av f

plt.plot(xes, func, label = "f(x)") # plotter f(x)
plt.plot(xes, df, label = "f'(x)")# plotter f'(x)
plt.xlabel("x") # navn på x-akse
plt.grid("both") # setter grid
plt.legend() # viser legend
