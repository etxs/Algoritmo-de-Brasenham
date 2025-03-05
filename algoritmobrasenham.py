import matplotlib.pyplot as plt
import numpy as np

def bresenham(inicio, fin):
    # (puntos de inicio y fin de la línea)
    (x0, y0) = inicio
    (x1, y1) = fin

    # (diferencias entre los puntos)
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    pendiente = dy / dx

    # Lista de puntos de toda la línea
    linea_puntos = [(x0, y0)]
    # x
    paso = 1 if x0 < x1 else -1
    # y
    cambio = 1 if y0 < y1 else -1

    if pendiente > 1:
        #Cambiar coordenadas si la pendiente es > 1
        x0, x1, y0, y1 = y0, y1, x0, x1
        dx, dy = dy, dx

    # Valor inicial de p
    p = 2 * dy - dx
    y = y0

    for x in range(x0, x1, paso):
        if pendiente > 1:
            # Cambiar coordenadas nuevamente para agregar a la lista de puntos
            linea_puntos.append((y, x))
        else:
            linea_puntos.append((x, y))

        if p >= 0:
            y += cambio
            p -= 2 * dx
        p += 2 * dy

    return np.array(linea_puntos)

# (definir los puntos de la línea)
inicio = (2, 3)
fin = (15, 12)

# (obtener los puntos de la línea mediante bresenham)
linea_puntos = bresenham(inicio, fin)

# Separar las coordenadas x, y para graficar
x_coords, y_coords = zip(*linea_puntos)

# Linea y el eje
fig, ax = plt.subplots()

# (graficar los puntos como una línea)
ax.plot(x_coords, y_coords, marker='D', markerfacecolor='pink', color='purple')

ax.grid(True)
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)

plt.show()