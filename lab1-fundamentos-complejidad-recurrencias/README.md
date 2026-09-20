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

Los resultados se incorporan después de ejecutar las mediciones.

## Parte 4 - Complejidad y validación

El desarrollo teórico y la comparación experimental se incorporan en los
siguientes avances del laboratorio.
