"""
1. Identifique la descripción medida de rendimiento, entorno, acciones, percepciones
(a) Agente Robot que juega al fútbol.

Medida de rendimiento: Para la medida de rendimiento podemos incluir ciertos factores como:
- El número de goles anotados 
- La precisión de los pases
- La efectividad de la defensa  
- Cumplimir con las reglas
- Una colaboracion entre otros agente (Puede ser un jugador humano como otro programados)

Lo que se busca es tener la capacidad de ganar el partido manteniendo un buen desempeño tomando en cuenta las
tareas que se realizan en el fútbol.

Entorno: El entorno del agente va a ser el campo de futbol, en el cual podemos incluir otros agentes que pueden ser
tanto companeros de equipo como oponentes, debemos tomar en cuenta el balon, el terreno, los limites del campo,
las reglas del juego(faltas entre Agentes, jugadas permitidas,etc).

Acciones: Las acciones que va a realizar nuestro agente va desde moverse en el campo, patear el balon, 
pasar el balon, interceptar el balón, correcta posicion para defender o marcaje del oponente, 
colaboracion de equipo(Perdir la pelota, asistencias), acciones para cubrir el balon el caso de que el oponente logre
patear, tambien generar jugadas ofensivas.

Percepciones: El agente va a percibir la posición y movimiento del balon, la ubicacion de otros jugadores (tanto 
companeros como oponentes),  los limites del campo, la posición de la porteria, el estado del juego (como 
tiempo restante, tiempo anadido, faltas cobradas)


(b) Agente Delivery

Medida de rendimiento: Como medidas de rendimiento podemos tomar en cuenta la eficiencia en la entrega del pedido, 
la cual puede ser medida por el tiempo de tardanza de entrega, la precisión  en la que se entrega el pedido, 
el consumo de combustible por entrega o en total, el numero de entregas completadas exitosamente, 
la satisfacción del cliente.

Entorno: Como entorno podemos tomar en cuenta la ciudad o área de entrega, en esta se pueden incluir calles, 
edificios, el trafico, las señales de tránsito, peatones, condiciones del clima, hora de la entrega, asi como 
situaciones inesperadas como accidentes externos o contratiempos.

Acciones: Nuestra acciones tienen que ver con la navegacion por las calles, esquivar obstaculos, detenerse en 
semaforos, seleccionar la ruta optima al lugar de recojo y entrega, recoger paquetes, interactuar con clientes, 
realizar entregas en las ubicaciones correctas.

Percepciones: Las percepciones de nuestro agente van a ser el trafico existente,  senales de tránsito, la ubicacion 
tanto del destino como del recojo, las condiciones del clima, la ubicacion actual del agente mediante GPS, 
posibles obstaculos que se puedan presentar en el camino

2. Para los casos anteriores, caracterice su entorno explicando el porque de su elección.

a) Agente Futbol

Caracterizacion del entorno: El entorno del agente es dinamico, esto ya que el entorno cambia rapidamente debido 
al movimiento constante, tanto de los jugadores como del balon y las estrategias y decisiones que se van tomando en 
tiempo real, tambien nos encontramos con un entorno no son completamente predecibles, como las acciones de
los jugadores, tanto contrarios como companeros, lo que nos lleva a que las acciones del agente no siempre  van a 
tener el mismo resultado en su ejecucion, tambien contamos con que es multiagente, ya que no esta solo en su entorno
, se debe interactuar con otros agentes, tanto compañeros de equipo como oponentes, lo que anade complejidad en la 
toma de decisiones.

(b) Agente Delivery
Caracterizacion del entorno: El entorno del agente es dinamico, esta en constante cambio debido al trafico, 
las señales de transito, las condiciones climaticas, junto a otros factores que el agente no puede controlar 
directamente, como distintos contratiempos como acciedentes, etc, tambien aunque en cierta parte contamos con un
entorno en el cual muchas reglas del entorno son determinísticas, como seguir los semaforos, senales de pare, etc. Existen
elementos inesperados como el tráfico, accidentes, o cambios climaticos que pueden alterar los resultados esperados.
El agente tambien se encuentra limitado o afectado por las condiciones del entorno por lo que no puede percibir 
todo el entorno en todo momento mas que lo que pueda captar, tambien se trata de que es un agente secuencial, ya que
cada acción influye en las siguientes, significa que debe tener una planificación cuidadosa y tomar decisiones 
basadas en el contexto que tiene actualmente.

3. Diferencias y similitudes entre un agente reactivo simple, agente basado en modelos y agente basado en objetivos.

Diferencias: 
- El agente reactivo simple no usa memoria ni guarda información pasada, el agente basado en modelos 
tiene un estado interno en el que se refleja la historia pasada del entorno, mientras el agente basado en 
objetivos utiliza tanto su modelo interno como su objetivo a largo plazo para planificar las acciones, es por 
esto que cada agente tiene diferencias en su uso de memoria.

- Las decisiones del agente reactivo simple son inmediatas y directas, los agentes basados en modelos y 
los agentes basados en objetivos pueden tomar decisiones mas complejas al predecir futuros estados del entorno o 
evaluar el progreso hacia para alcanzar una meta.

- El agente reactivo simple no planea, el agente basado en modelos puede predecir el futuro y el agente basado en 
objetivos planifica acciones que lo acerquen a su meta, asi se permite que el se pueda adaptar el tipo de agente 
a la complejidad del entorno en el que operan y a los requerimientos especificos de la tarea a realizar.

Similitudes:
- Todos los agentes perciben el entorno y toman acciones en respuesta a las percepciones.
- Todos buscan seleccionar acciones que mejoren su desempeño según algún criterio, ya sea reaccionando
, utilizando un modelo del mundo, o siguiendo objetivos específicos, lo unico seria que se hacen con diferentes 
grados de complejidad.
- Estos agentes siguen algun tipo de regla de de accion-reaccion, se podriar definir como si ocurre tal accion, 
se debe hacer cierta accion, solo varia la complejidad de estas reglas segun el tipo de agente.
- Todos los agentes se adaptan al entorno, donde pueden reaccionar instantáneamente a condiciones inmediatas
o llegar a planificar a largo plazo para cumplir el objetivo.

4. Sea una frontera ordenada por f(n) = (2w)*gn+wh(n). iPara qué valores del w está garantizado que el algoritmo
sea óptimo? Qué tipo de búsqueda realiza cuando w - 0, ;cuándo w = 1? y "cuándo w=2

- Para que sea optimo debemos tomar en cuenta que se encuentre la busqueda al menor costo que sea posible, por lo tanto
se debe tener una buena heuristica que nunca debe sobreestimar el costo real de alcanzar el objetivo. Si tomamos un 
valor de w mayor a 1 el peso se incrementa, lo que nos podria llevar a tabajar con una busqueda conservadora, mientras
que sea mas pequeno, podemos ver que va a ser mas ambicioso, por que si quisieramos trabajar con una busqueda *A mientras
tengamos una heristica admisible se va a logra en:
0 < w <= 1

- w = 0
f(n)=0
no tiene en cuenta ni el costo acumulado ni la heurística.

- w = 1 
f(n)=2g(n)+h(n)
Dependiendo de la heuristica que se tome, si se puede llegar a una busqueda *A, si no se puede lograr que se exploren
mas nodos de los que se deben 

-w =2 
f(n)=4g(n)+2h(n)
Tenemos que el peso de g(n) es mayor a h(n), pero se puede observar que crecieron uniformemente, por lo que se podria
tomar en cuenta la busqueda de costo uniforme

5. Considere un espacio de estados donde el estado comienzo es el número 1 y la función sucesor para el estado n 
devuelve 2 estados, los números 2n y 2n+1. 
a) Dibuje el trozo del espacio de estados para los estados del 1 al 15. 
- R: Dibujo_5a.png

b) 
- BFS: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
se encuentra tras 11 pasos

- DFS: 1, 2, 4, 8, 9, 5, 10, 11
se encuentra en octava posicion
"""