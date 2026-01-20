#!/bin/bash

PROGRAMA="./labolsa"
TIMEOUT=60
mkdir -p resultados

# === PARÁMETROS ===
MERCADO="TEST"     
COMPANIAS=10
USUARIOS=100
ORDENES=2000
PRECIO_INI=20.0
ACCIONES=100
CASH=1000.0

# === BARRIDO DE PARÁMETROS ===
# variable y los valores aquí:
for VALOR in 50 500 5000; do
    echo "Ejecutando simulación con parámetro: $VALOR"
    
    timeout $TIMEOUT $PROGRAMA $MERCADO $COMPANIAS $USUARIOS $VALOR $PRECIO_INI $VALOR $CASH > test1.dat 2>&1

    # Llamada dinámica al script de visualización
    python3 visualizacion.py $MERCADO
    
    cp test1.dat "resultados/output_$VALOR.dat"
    if [ -f stock.png ]; then
        mv stock.png "resultados/grafica_$VALOR.png"
    fi
done

echo "¡Barrido terminado!"