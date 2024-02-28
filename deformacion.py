#Libreria que realiza las gráficas
import matplotlib.pyplot as plt

# Datos de deformación y fuerza
fuerza = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
deformacion = [0, 4, 6, 7.4, 7.4, 7.4, 8.6, 8.8, 9.0, 9.5, 9.7, 9.9, 10, 11.9, 12.3, 14.2, 14.5, 14.8, 15]

# Área transversal (asumiendo un valor constante)
area_transversal = 1.0 

# Calcular el esfuerzo (stress) dividiendo la fuerza por el área transversal
esfuerzo = [fuerza_i / area_transversal for fuerza_i in fuerza]

# Graficar los datos
plt.figure(figsize=(10, 6))

# Graficar los datos principales
plt.plot(deformacion, esfuerzo, marker='o', linestyle='-')

# Encontrar el punto de ruptura
punto_de_ruptura = (deformacion[-1], esfuerzo[-1])

# Resaltar el punto de ruptura
plt.scatter(*punto_de_ruptura, color='red', zorder=5)

# Anotación para el punto de ruptura
plt.annotate('Punto de ruptura', xy=punto_de_ruptura, xytext=(punto_de_ruptura[0] - 5, punto_de_ruptura[1] + 1),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Etiquetas y título
plt.xlabel('Deformación (mm)')
plt.ylabel('Esfuerzo (kg/mm^2)')  
plt.title('Diagrama de Esfuerzo-Deformación')

# Mostrar la cuadrícula
plt.grid(True)

# Mostrar la gráfica
plt.show()
