# Laboratorio evaluativo 01 - Fundamentos, complejidad y recurrencias

**Nombre:** Tomás González Zapata

## Reproducción del experimento

Desde la raíz del repositorio, en PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cd lab1-fundamentos-complejidad-recurrencias
python parte3_casos.py
python parte4_complejidad.py
```

Los scripts crean nuevamente las gráficas dentro de `graficas/` y muestran en
la terminal las mediciones usadas en este informe.

## Parte 1 - Analizar el algoritmo antes de comprar hardware

Que insertion sort haya producido durante ocho años una lista ordenada habla de
su **corrección**, pero no garantiza su **eficiencia** para la carga actual. La
corrección responde si los pacientes quedan de mayor a menor riesgo. La
eficiencia responde si ese resultado se obtiene con el tiempo y los recursos
disponibles. Un algoritmo puede ordenar bien y aun así dejar de ser viable al
crecer la entrada.

Tamiza ya no procesa los cerca de 20.000 registros para los que se construyó,
sino 1.200.000. Además, el proceso solo puede ejecutarse entre las 2:00 a. m. y
las 6:00 a. m. Su restricción concreta es una ventana máxima de cuatro horas,
que ya se incumplió al dejar listas parciales. Por eso hay que estudiar cómo
crece el trabajo de insertion sort antes de comprar hardware.

Un servidor con el doble de velocidad puede reducir el tiempo de una ejecución,
pero no cambia el crecimiento cuadrático del algoritmo. Si la cantidad o el
orden de los datos empeoran, el número de operaciones puede crecer mucho más
rápido que la mejora constante del procesador. La compra aplazaría el problema,
pero mantendría la misma causa.

Como segundo ejemplo, una aplicación de comercio electrónico podría buscar de
forma secuencial entre unos 500.000 productos después de cada tecla escrita por
el usuario. La búsqueda puede devolver los productos correctos, pero sería
inviable si la interfaz exige responder en menos de 300 milisegundos. En ese
caso, revisar la estructura de búsqueda y el algoritmo aporta más que limitarse
a aumentar la velocidad del servidor.

## Parte 2 - Responsabilidad ambiental y ética

Elegir el algoritmo que corre cada madrugada también determina el uso de
recursos. Más tiempo de CPU implica más tiempo del servidor bajo carga y, por
lo tanto, mayor consumo energético. No hace falta inventar una cifra de vatios
para reconocer la relación. El efecto tampoco ocurre una sola vez: se repite
todas las noches y se acumula durante los años de operación de Tamiza. Mantener
un algoritmo que hace trabajo innecesario aumenta ese consumo acumulado y la
infraestructura requerida para sostenerlo.

La decisión también tiene consecuencias para personas concretas. Primero, si
el proceso no termina, un paciente con riesgo cardiovascular alto puede quedar
fuera de la lista parcial y recibir tarde la llamada para valoración. El costo
principal lo asume el paciente por el retraso en la atención, aunque la
Secretaría también asume el riesgo institucional de prestar un servicio
inoportuno y el equipo técnico debe responder por una decisión previsible.

Segundo, un operador del centro de contacto puede iniciar su jornada con una
lista incompleta o mal priorizada. El operador pierde tiempo revisando casos o
contactando primero a personas de menor riesgo; la Secretaría paga esa pérdida
operativa y los pacientes desplazados en la lista soportan la demora. No es
razonable trasladarles esos costos cuando el origen está en una elección
técnica que puede analizarse y corregirse.

Además, aquí ordenar bien no es un detalle interno. La posición de cada registro
decide quién recibe primero una llamada. La implementación debe preservar el
orden de mayor a menor riesgo y producir una lista completa. Mejorar el tiempo
sin comprobar la corrección podría adelantar pacientes equivocados; conservar
la corrección sin cumplir la ventana podría excluir a quienes más necesitan el
contacto. La responsabilidad ética exige ambas condiciones.

## Parte 3 - Peor, mejor y caso promedio

[Código de la Parte 3](parte3_casos.py) | [Algoritmos](algoritmos.py) |
[Generadores de datos](datos.py)

### Explicación

Para un tamaño fijo `n`, el **peor caso** es el máximo trabajo que realiza el
algoritmo entre todas las entradas posibles de ese tamaño. El **mejor caso** es
el mínimo trabajo dentro del mismo conjunto de entradas de tamaño `n`. El
**caso promedio** es el trabajo esperado al considerar esas entradas bajo una
distribución definida, por ejemplo permutaciones aleatorias con igual
probabilidad. No es una entrada particular, sino un promedio condicionado por
la forma en que suponemos que llegan los datos.

Para autorizar Tamiza usaría principalmente el peor caso. La ventana de cuatro
horas es estricta y el canal de origen puede cambiar sin aviso, así que una
decisión basada solo en el promedio o en el lote favorable no ofrece la garantía
necesaria. El algoritmo elegido debe seguir siendo viable cuando llegue una
entrada del mismo tamaño con el orden más desfavorable.

### Predicción previa

La predicción se fija antes de ejecutar el experimento. Como el orden requerido
es de mayor a menor, el escenario B debería aproximarse al mejor caso: su 98 %
inicial ya está descendente y solo el 2 % final llega desordenado. El escenario
C debería ser el peor caso porque viene completamente ascendente, en el sentido
contrario, y cada clave debe desplazarse hasta el inicio. El escenario A
aleatorio debería aproximarse al caso promedio, con más trabajo que B y menos
que C.

### Resultados experimentales

Se usaron tamaños de 100, 200, 400, 800, 1600, 3200 y 6400. Para
cada combinación se generó primero el lote y luego se midieron únicamente tres
llamadas a `insertion_sort` con `time.perf_counter()`. La tabla y la gráfica de
tiempo usan la mediana de esas tres ejecuciones para reducir el ruido del
sistema operativo. El conteo de comparaciones es determinista para cada lote.

La situación describe riesgos enteros entre 0 y 1000, pero no pueden existir
6400 valores enteros distintos en ese rango. Para mantener la exigencia de
valores únicos se usaron identificadores enteros de `0` a `n - 1`. Sus
magnitudes no representan riesgos clínicos reales; solo conservan el orden
relativo necesario para estudiar los algoritmos.

Comparaciones entre elementos:

| Tamaño | A: aleatorio | B: casi ordenado | C: inverso |
|---:|---:|---:|---:|
| 100 | 2.542 | 100 | 4.950 |
| 200 | 9.970 | 201 | 19.900 |
| 400 | 40.436 | 409 | 79.800 |
| 800 | 160.484 | 852 | 319.600 |
| 1600 | 648.481 | 1.843 | 1.279.200 |
| 3200 | 2.533.103 | 4.242 | 5.118.400 |
| 6400 | 10.276.753 | 10.649 | 20.476.800 |

![Comparaciones de insertion sort](graficas/parte3_comparaciones.png)

Tiempo mediano en milisegundos:

| Tamaño | A: aleatorio | B: casi ordenado | C: inverso |
|---:|---:|---:|---:|
| 100 | 0,1523 | 0,0068 | 0,2981 |
| 200 | 0,6014 | 0,0134 | 1,1896 |
| 400 | 2,5021 | 0,0299 | 4,8720 |
| 800 | 10,7969 | 0,0656 | 20,4138 |
| 1600 | 42,7299 | 0,1444 | 83,4178 |
| 3200 | 167,8848 | 0,3293 | 340,8920 |
| 6400 | 686,0788 | 0,8068 | 1.357,0321 |

![Tiempo de insertion sort](graficas/parte3_tiempo.png)

### Contraste con la predicción

El escenario C fue el peor: con 6400 registros alcanzó 20.476.800
comparaciones y 1.357,0321 ms. Corresponde exactamente a
`n(n - 1) / 2`, porque cada elemento nuevo debe atravesar toda la parte ya
procesada. El escenario B fue el mejor, con 10.649 comparaciones y 0,8068 ms
para el mismo tamaño; su prefijo descendente casi no requiere movimientos y el
trabajo adicional se concentra en la cola del 2 %.

El escenario A quedó entre ambos y se aproxima al caso promedio. En `n=6400`
realizó 10.276.753 comparaciones, cerca de la mitad del escenario C, y tardó
686,0788 ms. La clasificación observada coincide con la predicción previa: B
se acerca al mejor caso, A al promedio y C representa el peor caso para el
orden descendente elegido.

## Parte 4 - Complejidad y validación

[Código de la Parte 4](parte4_complejidad.py) | [Algoritmos](algoritmos.py) |
[Generadores de datos](datos.py)

### Recurrencia de merge sort

Merge sort divide una entrada de tamaño `n` en dos partes, ordena cada una y
las combina. Su recurrencia es:

```text
T(n) = 2T(n/2) + Θ(n)
```

El `2` aparece porque se resuelven dos subproblemas. Cada uno recibe `n/2`
elementos. Finalmente, `Θ(n)` corresponde a la mezcla: para producir una sola
lista descendente hay que recorrer los elementos de ambas mitades.

### Resolución por método maestro

Para la forma `T(n) = aT(n/b) + f(n)` se obtiene:

```text
a = 2
b = 2
f(n) = Θ(n)

n^(log_b(a)) = n^(log_2(2)) = n
```

Por tanto, `f(n) = Θ(n)` tiene el mismo orden que
`n^(log_b(a)) = n`. Se cumple la condición del caso 2 del método maestro:
`f(n) = Θ(n^(log_b(a)) log^0(n))`. Al sumar un factor logarítmico, el
resultado es:

```text
T(n) = Θ(n^(log_2(2)) log(n))
T(n) = Θ(n log n)
```

### Análisis línea a línea de insertion sort

El análisis corresponde a las operaciones de `insertion_sort` en
[`algoritmos.py`](algoritmos.py). Para la iteración externa `i`, sea `t_i` el
número de comparaciones entre elementos y `s_i` el número de desplazamientos.
También sea `b_i` igual a 1 cuando esa iteración termina con `break` y 0 cuando
termina porque `posicion` llega a -1.

| Operación real | Costo | Veces que se ejecuta |
|---|---:|---:|
| `ordenados = datos.copy()` | `c1` por elemento | `n` |
| `comparaciones = 0` | `c2` | `1` |
| control de `for indice in range(...)` | `c3` | `n` |
| `clave = ordenados[indice]` | `c4` | `n - 1` |
| `posicion = indice - 1` | `c5` | `n - 1` |
| comprobación `posicion >= 0` | `c6` | como máximo `Σ(t_i + 1)` |
| `comparaciones += 1` | `c7` | `Σt_i` |
| comparación `ordenados[posicion] >= clave` | `c8` | `Σt_i` |
| `break` | `c9` | `Σb_i` |
| desplazamiento de un elemento | `c10` | `Σs_i` |
| `posicion -= 1` | `c11` | `Σs_i` |
| inserción `ordenados[posicion + 1] = clave` | `c12` | `n - 1` |
| `return ordenados, comparaciones` | `c13` | `1` |

Una expresión que reúne esos costos es:

```text
T(n) = c1*n + c2 + c3*n + (c4+c5+c12)(n-1)
     + c6*Σ(t_i+1) + (c7+c8)*Σt_i
     + c9*Σb_i + (c10+c11)*Σs_i + c13
```

En el peor caso, la entrada viene ascendente y se necesita el resultado
descendente. En la iteración `i`, la clave se compara y se desplaza frente a
los `i` elementos anteriores: `t_i = s_i = i`. Así aparece la suma:

```text
1 + 2 + ... + (n - 1) = n(n - 1) / 2
```

Ese término cuadrático domina los costos lineales, por lo que el peor caso es
`Θ(n²)`. En el mejor caso la entrada ya está descendente: se hace una
comparación entre elementos por iteración, no hay desplazamientos y
`Σt_i = n - 1`. Incluso contando la copia inicial, el costo total es `Θ(n)`.
En una permutación aleatoria se desplaza en promedio una fracción lineal del
prefijo por cada clave; la suma sigue siendo cuadrática y da `Θ(n²)`.

### Tabla de complejidades

| Algoritmo | Mejor caso | Caso promedio | Peor caso |
|---|---:|---:|---:|
| Insertion sort | `Θ(n)` | `Θ(n²)` | `Θ(n²)` |
| Merge sort | `Θ(n log n)` | `Θ(n log n)` | `Θ(n log n)` |

### Validación experimental

Se generó una sola entrada aleatoria por tamaño y ambos algoritmos recibieron
ese mismo lote sin modificarlo. Cada algoritmo se ejecutó tres veces y se tomó
la mediana de `time.perf_counter()`, midiendo solo el ordenamiento.

| Tamaño | Insertion sort (ms) | Merge sort (ms) |
|---:|---:|---:|
| 100 | 0,2691 | 0,1652 |
| 200 | 0,6932 | 0,1985 |
| 400 | 2,5596 | 0,5880 |
| 800 | 10,4194 | 1,0228 |
| 1600 | 42,2188 | 2,1435 |
| 3200 | 172,3186 | 4,5345 |
| 6400 | 699,4981 | 10,0719 |

![Tiempo de insertion sort y merge sort](graficas/parte4_tiempo.png)

La curva de insertion sort se hace cada vez más inclinada. Cuando `n` se
duplica, su tiempo tiende a acercarse a cuatro veces el anterior, como se
espera de `Θ(n²)`. Merge sort crece con mucha más suavidad, de acuerdo con
`Θ(n log n)`. En 100 registros los tiempos todavía están cercanos porque merge
sort paga llamadas recursivas y creación de listas, aunque en esta ejecución ya
fue más rápido. En 6400 registros, insertion sort necesitó 699,4981 ms y merge
sort 10,0719 ms, una ventaja aproximada de 69,5 veces para merge sort. La forma
de ambas curvas coincide con las cotas calculadas y muestra que merge sort
escala mejor para Tamiza.

### Extrapolación a 1.200.000 registros

La extrapolación parte de la medición aleatoria de `n0 = 6400`, la mayor del
experimento. No se ejecutaron 1.200.000 registros. Para insertion sort se usó
el modelo cuadrático y su tiempo real `t0 = 0,6994981 s`:

```text
t = 0,6994981 * (1.200.000 / 6.400)^2
t = 24.591,7301 s = 409,8622 min = 6,8310 h
```

Para merge sort se usó su tiempo real `t0 = 0,0100719 s` y el crecimiento
`n log2(n)`:

```text
t = 0,0100719 *
    (1.200.000 * log2(1.200.000)) / (6.400 * log2(6.400))
t = 3,0163 s = 0,0503 min
```

Estas cifras son **estimaciones**, no mediciones directas. Suponen que las
constantes de esta implementación y este equipo se mantienen, que la entrada
se comporta como el escenario aleatorio y que no intervienen lectura de disco,
base de datos, red ni otros procesos. Con esos supuestos, insertion sort supera
la ventana de cuatro horas, mientras merge sort queda ampliamente por debajo.

### Concepto técnico para la Secretaría de Salud

Al equipo de ingeniería de la Secretaría de Salud le recomiendo reemplazar
insertion sort por merge sort como único algoritmo de ordenamiento de Tamiza.
La decisión no depende de que insertion sort sea incorrecto. Ambos producen la
lista descendente requerida, pero sus márgenes ante el crecimiento y los
cambios del canal de entrada son muy distintos.

En la medición aleatoria con 6400 registros, insertion sort tardó 699,4981 ms
y realizó 10.276.753 comparaciones. Merge sort recibió el mismo lote, tardó
10,0719 ms y realizó 72.967 comparaciones. En ese punto merge sort fue unas
69,5 veces más rápido. La diferencia también aumentó con el tamaño: al duplicar
la entrada, la curva de insertion sort tendió a multiplicar el tiempo por
cuatro, mientras la de merge sort creció de forma cercana a `n log n`. Esta
evidencia coincide con `Θ(n²)` frente a `Θ(n log n)`.

Para aproximar el lote real se tomó la mayor medición, `n0 = 6400`. El modelo
cuadrático estima para insertion sort `0,6994981 * (1.200.000 / 6.400)²`, que
equivale a 24.591,7301 segundos o 6,8310 horas. Para merge sort se escaló el
tiempo de 0,0100719 segundos mediante la razón entre
`1.200.000 log2(1.200.000)` y `6.400 log2(6.400)`, con un resultado de 3,0163
segundos. Son estimaciones, no mediciones directas. Excluyen carga de datos,
escritura de la lista, competencia por CPU y cambios de plataforma, por lo que
deben validarse después con una prueba de integración representativa. Aun con
esa limitación, insertion sort rebasa las cuatro horas y merge sort conserva un
margen mucho mayor.

No recomiendo aprobar la compra del servidor como solución del problema. Bajo
el supuesto ideal de reducir exactamente a la mitad el tiempo, la estimación
aleatoria de insertion sort bajaría a 3,4155 horas, dejando cerca de 35 minutos
para el resto del proceso y cualquier variación. Además, el canal puede cambiar
sin aviso. En el escenario C, insertion sort ya tardó 1.357,0321 ms para 6400
registros; la extrapolación cuadrática da 13,2523 horas y aun un servidor dos
veces más rápido dejaría cerca de 6,6261 horas. El hardware reduce una
constante, pero no elimina el crecimiento cuadrático ni ofrece la garantía
requerida.

Insertion sort sí mostró una ventaja especial cuando el lote estaba 98 %
ordenado: solo tardó 0,8068 ms en 6400 registros. Sin embargo, escogerlo por ese
caso obligaría a confiar en que el reproceso conservará siempre esa forma o a
mantener varias rutas de ordenamiento. Como el equipo quiere una sola
implementación y el origen puede ser aleatorio, casi ordenado o inverso, merge
sort ofrece el comportamiento más predecible.

El cambio tiene costos que deben registrarse. Esta implementación de merge sort
crea listas auxiliares y usa más memoria que insertion sort. A cambio, mantiene
`Θ(n log n)` en todos los casos y es estable: ante riesgos iguales toma primero
el elemento de la mitad izquierda, conservando su orden relativo. Esa propiedad
ayuda a no alterar arbitrariamente prioridades equivalentes. Recomiendo probar
el consumo de memoria con datos cercanos a producción, conservar pruebas de
orden descendente y estabilidad, y desplegar merge sort con monitoreo del
tiempo total del proceso nocturno.
