# Laboratorio evaluativo 02 - Divide y vencerás

**Nombre:** Tomás González Zapata

## Reproducción

Desde la raíz del repositorio, en PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\venv\Scripts\Activate.ps1
cd lab2-divide-y-vencer
python pruebas.py
python medicion.py
```

El entorno virtual de la raíz contiene matplotlib. `pruebas.py` verifica las
dos soluciones y `medicion.py` repite el experimento y genera la gráfica en
`graficas/tiempo_vs_n.png`.

## Parte 1 - Implementación y verificación

[Algoritmos de subarreglo máximo](subarreglo.py) |
[Pruebas](pruebas.py)

Se implementarán dos soluciones para encontrar la mejor racha de días. La
primera recorrerá todos los pares de índices acumulando la suma, con costo
cuadrático. La segunda dividirá el rango en sus mitades y comparará la mejor
racha izquierda, derecha y cruzada.

La verificación cubrirá la serie de la cooperativa, entradas unitarias, valores
negativos, valores positivos, empates, decimales, un resultado que cruce el
punto medio y listas aleatorias reproducibles. También se comprobará que las
funciones no modifiquen la lista recibida.

## Parte 2 - Medición y gráfica

[Código de la medición](medicion.py)

Los datos se generarán con semilla fija antes de iniciar el cronómetro. Ambos
algoritmos recibirán exactamente la misma lista para cada tamaño. Se medirán
tres ejecuciones con `time.perf_counter()` y se usará la mediana para reducir
el efecto del ruido del sistema operativo.

## Parte 3 - Análisis

El análisis final relacionará la recurrencia, las complejidades calculadas y
los tiempos obtenidos en este equipo. Las estimaciones para un millón de
registros se presentarán como extrapolaciones, no como mediciones directas.
