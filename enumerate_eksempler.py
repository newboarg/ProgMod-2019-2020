### EKSEMPEL 1

a = ["en", "to", "tre", "åssåfir"]

print(list(enumerate(a, start=2)))

#hvert element i lista
for item in a:
    print(element)
    
#indekser
for i in range(len(a)):
    print(i)
    
#begge
for i, item in enumerate(a):
    print(i, element)
    
    
    
### EKSEMPEL 2

import numpy as np

x = np.linspace(0,10,11)
y = [1, 2, 3, 4]

for i in enumerate(x):
    print(i[0])
    x[i[0]]= i[1]*2
    
print(x)
