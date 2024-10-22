#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import re

data = []

with open('bolsa.dat', 'r') as file:
    renglones = file.readlines()
    
    for renglon in renglones:
        if renglon.startswith('MEX'):
            carac = re.split(r'\s+', renglon.strip())  # Dividir la línea por espacios
            data.append([carac[0], float(carac[1]), float(carac[2]), float(carac[3]), float(carac[4]), float(carac[5])])  # Datos relevantes de cada columna 

# columnas importantes 
columns = ['Code', 'Min', 'Begin', 'Average', 'Close', 'Max']

#DataFrame
stock_prices = pd.DataFrame(data, columns=columns)

#print(stock_prices)  

plt.figure()

# Filtrar las velas que suben y las que bajan
up = stock_prices[stock_prices.Close >= stock_prices.Begin]
down = stock_prices[stock_prices.Close < stock_prices.Begin]

# Colores
col_up = 'green'   # Velas hacia arriba
col_down = 'red'   # Velas hacia abajo

# Ancho de las velas
width = 0.3
width2 = 0.1

# Acciones que suben
plt.bar(up['Code'], up['Close'] - up['Begin'], width, bottom=up['Begin'], color=col_up)
plt.bar(up['Code'], up['Max'] - up['Close'], width2, bottom=up['Close'], color=col_up)
plt.bar(up['Code'], up['Min'] - up['Begin'], width2, bottom=up['Begin'], color=col_up)


plt.bar(down['Code'], down['Close'] - down['Begin'], width, bottom=down['Begin'], color=col_down)
plt.bar(down['Code'], down['Max'] - down['Begin'], width2, bottom=down['Begin'], color=col_down)
plt.bar(down['Code'], down['Min'] - down['Close'], width2, bottom=down['Close'], color=col_down)

plt.title('Velas Japonesas labolsa')
plt.xlabel('Code')
plt.ylabel('Price')
plt.xticks(rotation=30, ha='right')  # Rotar etiquetas del eje x
plt.tight_layout()  

plt.show()  
