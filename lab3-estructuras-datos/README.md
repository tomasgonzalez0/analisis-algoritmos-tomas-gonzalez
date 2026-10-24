# Laboratorio evaluativo 03 - Estructuras de datos

**Nombre:** Tomás González Zapata

## Reproducción

Desde la raíz del repositorio, en PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\venv\Scripts\Activate.ps1
cd lab3-estructuras-datos
python pruebas.py
python medicion.py
```

El entorno virtual de la raíz contiene matplotlib. `pruebas.py` verifica las
estructuras y `medicion.py` repite los experimentos y genera las gráficas.

## Parte 1 - Implementación y verificación

[Estructuras](estructuras.py) | [Pruebas](pruebas.py)

La lista enlazada insertará cada guía al inicio y realizará búsquedas
iterativas. La tabla hash reutilizará una lista por casilla y distribuirá las
guías con el método de la división. Se comprobarán búsquedas exitosas y
fallidas, colisiones forzadas, el factor de carga y colecciones aleatorias
reproducibles.

## Parte 2 - Medición y gráficas

[Código de la medición](medicion.py)

La medición usará guías únicas de diez dígitos generadas con semillas fijas.
Para cada dato se cronometrarán únicamente 200 búsquedas fallidas. Cada lote se
repetirá cinco veces y se conservará la mediana de los tiempos medios por
búsqueda. Se espera que el tiempo de la lista crezca con `n`, que la tabla se
mantenga aproximadamente constante cuando `α` no cambia y que búsquedas en la
tabla se hagan más costosas al aumentar `α`.

## Parte 3 - Análisis

El análisis se completará con los resultados reproducibles de los
experimentos.
