import numpy as np  
import matplotlib.pyplot as plt  

radio = float(input('Diga un número para el radio de la órbita, estara en kilometrso automaticamente\n'))
angulos = np.linspace(0, 2*np.pi, int(input('Diga el número de angulos que quiere\n')))

if radio <= 2000:
    print('Es una órbita baja sobre el nivel del mar')
elif radio >= 1500001:
    print('Esta fuera de la órbita sobre el nivel del mar')
elif radio >= 35787:
    print('Es una órbita alta sobre el nivel del mar')
elif radio >= 2001:
    print('Es una órbita media sobre el nivel del mar')

x = radio * np.cos(angulos)  
y = radio * np.sin(angulos)  

plt.plot(x, y, color='blue')  
plt.title('Órbita Simple',
          fontsize=14,
          color='blue')  
plt.xlabel('X (km)',
           fontsize=11)  
plt.ylabel('Y (km)',
           fontsize=11)  
plt.axis('equal')  
plt.show()