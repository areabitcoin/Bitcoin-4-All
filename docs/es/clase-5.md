# 5 Clase 5 - Dentro de Bitcoin: Minería, Halving y los Ciclos

##  Video de la Clase

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1085124591?badge=0&autopause=0&player_id=0&app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Clase 5"></iframe></div>

---

##  Guión Completo

# Guión Clase 5 - Dentro de Bitcoin: cómo funciona Bitcoin? (minería, halving y los ciclos)

![Slide 108](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-01.jpg)

Ahora que ya entendiste cómo funciona la blockchain de Bitcoin y que necesita consenso de los participantes para que exista coordinación descentralizada, entonces vamos a entender cómo la red hace para ponerse de acuerdo entre sí a través del mecanismo llamado Prueba de Trabajo, o Proof of Work en inglés (PoW).


![Slide 109](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-02.jpg)

La minería de Bitcoin es una analogía para el proceso de búsqueda de algo precioso, como el oro, solo que en la red Bitcoin ese algo precioso es el hash de cada bloque. En el oro, los mineros van cavando el yacimiento hasta encontrar el metal precioso, cuando lo encuentran, tienen algo escaso y valioso en la mano. El oro es escaso y con el tiempo se vuelve más difícil y más caro minar oro, porque tienes que cavar más profundo en el suelo. Exige equipos cada vez más modernos y eficientes para acceder a los yacimientos más profundos y complejos.

Con Bitcoin sucede algo muy parecido. En la red Bitcoin, los mineros compiten entre sí, a través de prueba y error, para ver quién llega primero al hash que cierra cada bloque de información.

![Slide 110](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-03.jpg)

Recuerdas que el bloque está formado por varios componentes? El hash del bloque anterior, una marca de fecha y hora llamada timestamp y todos los datos de las transacciones.

Junto con esta información también hay un dato llamado "nonce". Nonce significa "number used only once" - número que solo puede ser usado una vez. Cuando los mineros usan poder computacional para minar el bloque significa que están, a una velocidad computacional absurda, intentando encontrar ese número que solo puede ser usado una vez por la red. Es ese número el que todos los mineros compiten para encontrar.

En el encabezado del bloque va el hash que mezcla todos estos componentes: el hash del bloque anterior, el timestamp, la transacción raíz que resume todas las transacciones que entraron en el bloque y el nonce.


![Slide 111](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-04.jpg)

Todos quedan buscando la pieza correcta dentro de todas las posibilidades y quien la encuentra primero intenta encajarla en la imagen. Cuando el minero encuentra la pieza que faltaba, es muy fácil para todos percibir si encajó. Es solo mirar la imagen y ver si la pieza era correcta o no.

Esto quiere decir que la minería es un proceso difícil de defraudar y al mismo tiempo muy fácil de verificar. Así como es difícil encontrar la pieza correcta en un rompecabezas gigante, pero es fácil verificar si era la pieza que faltaba o no. Bitcoin es como si fuera un rompecabezas global en el que el mundo entero participa y acompaña en tiempo real los resultados.


![Slide 112](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-05.jpg)

Todo el proceso de minería y de consenso al registrar la blockchain de Bitcoin funciona así:

Los mineros emplean poder computacional, compran máquinas potentes con gran poder computacional para intentar encontrar el nonce del bloque lo más rápido posible. Cuando lo encuentran, crean el hash, lo muestran a la red, y los nodos verifican si el bloque propuesto está siguiendo las reglas. Si todo está bien, ese bloque es insertado en la cadena de bloques, propagado por la red y todos los participantes insertan ese bloque en sus copias de la blockchain. Y al final, los mineros reciben Bitcoin como recompensa por haber cumplido la tarea.

Todo este proceso es conocido como prueba de trabajo.


![Slide 113](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-06.jpg)

Prueba de trabajo significa que el minero encontró el nonce, creó el hash del bloque, siguió las reglas y prestó un servicio computacional para la red. Cuando toda la información del bloque es encontrada, pasa por el proceso de criptografía, de transformar la información en un enigma criptográfico usando SHA-256. El resultado es ese número enorme allí abajo, que representa el hash del bloque, resultado de todo el trabajo del minero.


![Slide 114](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-07.jpg)

Este proceso no es exclusivo de Bitcoin, sino de cualquier cosa que puede ser criptografiada, y SHA-256 es el algoritmo que hace esto. SHA-256 toma una información de cualquier tamaño y crea una secuencia de 256 bits: una serie de 256 ceros y unos. A partir de ese número enorme lleno de 01010101 el algoritmo crea una secuencia hexadecimal formada por 64 dígitos entre letras y números más fácil de anotar. Es decir, es fácil verificar si está correcto, pero es prácticamente imposible forjar la información que fue criptografiada.

Intentar acertar de forma aleatoria un hash y romper la criptografía SHA-256 es prácticamente imposible. Involucra un número absurdamente alto de combinaciones posibles, son más números que la cantidad de átomos en el universo observable! Esto exigiría un número de intentos tan grande, pero tan grande, que una computadora normal tardaría miles de millones de años para conseguir hacerlo.

Es ahí donde surge la historia de la computadora cuántica! Las personas siempre nos preguntan si una computadora cuántica podría romper la criptografía de Bitcoin. Esta es una de las grandes esperanzas de los haters de Bitcoin, pero la verdad es que probablemente ninguna computadora cuántica conseguiría matar a Bitcoin.

Debajo de esta clase voy a dejar un [artículo](https://blog.areabitcoin.com.br/computadores-quanticos-podem-destruir-o-bitcoin/) que explica esto.

Te quiero mostrar un [sitio](https://codebeautify.org/sha256-hash-generator) muy interesante. Es este de aquí, llamado code beauty. Este sitio permite que experimentes y conviertas cualquier información en una función SHA-256.

Voy a escribir aquí Bitcoin4All y mira cómo el código en el box de abajo va cambiando con cada letra, espacio o puntuación insertada. Esto es lo que sucede con el hash del bloque de la red Bitcoin si cualquier información es modificada. Observa también lo rápido que fue, no exigió un mega poder computacional para encontrar este hash. Entonces si fue tan fácil así crear un hash aquí en este sitio, por qué en la red Bitcoin tarda 10 minutos y ya no es posible minar desde la computadora de casa?


![Slide 115](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-08.jpg)

Esto tiene que ver con un mecanismo llamado ajuste de dificultad.

El ajuste de dificultad tiene el papel de regular la emisión de nuevos Bitcoin. Es este ajuste el que garantiza que el promedio de creación de nuevos bloques y la recompensa entregada por la red sea de 10 minutos. Esto porque cada 2016 bloques minados, aproximadamente 15 días en promedio, hay un algoritmo que va a analizar la cantidad de poder computacional de la red y aumentar o disminuir la dificultad de encontrar el hash del bloque.

Si de repente aumenta mucho la cantidad de mineros, la red se va a autorregular para aumentar la dificultad de minería para no acelerar la velocidad con que nuevos bloques son creados y consecuentemente no acelerar la velocidad con que nuevos Bitcoin son creados.


![Slide 116](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-09.jpg)

Funciona así: conforme más mineros se unen a la red y el hashrate aumenta (la tasa de creación de nuevos bloques), los mineros comienzan a encontrar bloques más fácilmente y se vuelve más rápido el tiempo promedio de minería entre un bloque y otro. La red percibe esto a través de los algoritmos y aumenta la dificultad de minería, con esto la velocidad de creación de nuevos bloques cae, porque se volvió más difícil para los mineros encontrar bloques, hasta estabilizarse en el promedio de 10 minutos entre un bloque y otro.

Es así como la red se autorregula con el aumento de la demanda para nunca perder su previsibilidad.


![Slide 117](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-10.jpg)

Se puede saber el nivel de dificultad de minar cada bloque de acuerdo con la cantidad de ceros que aparecen antes del número del hash del bloque. Este bloque por ejemplo tiene 24 ceros delante del código del hash, fue minado en octubre de 2022 y es uno de los bloques que tuvo más dificultad en ser minado en la época.

El objetivo del minero es armar un bloque donde el código hash sea menor que el objetivo actual (penúltima línea en blanco). Cuanto menor el objetivo, más difícil es encontrar un bloque válido. Cuantos más mineros en la red, más difícil se vuelve.


![Slide 118](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-11.jpg)

Es decir, cuantos más ceros liderando un hash, más difícil de minar, más el minero necesitó quedarse buscando el nonce del bloque hasta encontrarlo.


![Slide 119](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-12.jpg)

Es por causa del ajuste de dificultad que la minería evolucionó y ya no es tan fácil minar desde la PC de casa, desde una CPU. Hoy la minería de Bitcoin se hace con máquinas específicas llamadas ASICS. Conforme el precio de Bitcoin fue subiendo, acabó atrayendo cada vez más personas, más poder computacional fue siendo empleado en la red y con eso el algoritmo de ajuste de dificultad fue subiendo para mantener el promedio de un bloque minado cada 10 minutos.

Con el aumento de la dificultad, las personas más atentas comenzaron a usar máquinas más potentes: las GPUs, muy usadas en computadoras gamers. Bitcoin continuó atrayendo cada vez más personas queriendo minar, hasta que decidieron crear una máquina específica: las ASICs.

Este tipo de máquina es mucho más potente y les gana a las CPUs y GPUs en la velocidad de encontrar el hash del bloque. La minería se convirtió en una industria gigante y dedicada, que busca incansablemente eficiencia. Es decir, producir el máximo de Bitcoin con el mínimo de energía o con energía barata.

Por eso no importa el precio. Bitcoin puede ir a 10 mil millones de dólares. La velocidad de emisión de nuevos bitcoin no cambia. Incluso el aumento en el poder del hashrate no puede llevar a la emisión de más Bitcoin más allá de lo que está planificado para cada ciclo de halving. La entrada de más mineros en la red no produce más bitcoin, pero hace la red más segura y descentralizada.


![Slide 120](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-13.jpg)

Y por qué este mecanismo hace la red más segura? Esto sucede porque cuanto mayor el poder computacional, más difícil es atacar la red. En este gráfico la línea representa el hashrate, el poder computacional, y los colores más rojizos la dificultad de minar cada bloque. La dificultad y el hashrate han aumentado exponencialmente desde que Bitcoin comenzó a funcionar. Conforme la línea se va poniendo naranja, mayor la dificultad de minar un bloque. Cuanto mayor el poder computacional, más la red se adaptó para proteger las propiedades de Bitcoin. Es por eso que Bitcoin no tiene competidor en la minería, es el protocolo con más mineros distribuidos alrededor del planeta y con mayor poder computacional de todos.


![Slide 121](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-14.jpg)

Bitcoin es 631 veces más potente que las 500 mayores supercomputadoras del mundo combinadas, representadas en la línea blanca, y Bitcoin se muestra en la línea naranja. Bitcoin tiene la red computacional más resistente a ataques y 600 veces más fuerte que cualquier sistema computacional o data center centralizado.

Pero el avance de la minería no paró en las ASICs. Con el tiempo, incluso teniendo una máquina súper potente, fue volviéndose cada vez más difícil encontrar bloques y los mineros acabaron agrupándose en pools. Hacen una vaquita de poder computacional para tener más chances de encontrar bloques y dividir la recompensa.


![Slide 122](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-15.jpg)

Los pools de minería funcionan entre el software Bitcoin y los mineros, permite que los mineros agrupen el poder computacional de sus máquinas y tengan más chances de encontrar un bloque. Pool viene de la palabra piscina en inglés, un concentrado de poder computacional agrupado.


![Slide 123](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-16.jpg)

Para que tengas noción de la dificultad que es minar fuera de un pool, o sea, minar solo, una S19JPRO que es una de las máquinas ASICS más modernas, tiene 0,000 000 208% de chance de minar un bloque de Bitcoin. Esto significa una chance en casi 4.8 mil millones de intentos en toda la vida útil de la máquina, que dura en promedio de 5 a 8 años. Esta probabilidad va a continuar disminuyendo a lo largo del tiempo, conforme más mineros llegan, el hashrate sube y la dificultad aumenta.


![Slide 124](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-17.jpg)

Es por eso que los pools son como una vaquita de poder computacional, que cuando alguien encuentra el bloque todos ratean la recompensa en Bitcoin proporcionalmente al poder de hash de cada uno. Así, los mineros consiguen tener ingresos frecuentes en vez de quedarse esperando la suerte de encontrar un bloque por cuenta propia, lo que puede tardar años y todavía sin garantía ninguna de que suceda.


![Slide 125](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-18.jpg)

Hoy la red Bitcoin tiene decenas de pools, pero cinco de ellas son las mayores y las que agregan la mayor parte del hashrate: son Foundry, Antpool, F2Pool, ViaBTC y Mara. A pesar de que mucha gente dice que esto sería un mecanismo de centralización, en realidad los mineros pueden salir del pool en cualquier momento e ir a otro, o pueden incluso minar solo si quieren probar suerte. Es decir, la concentración en estos cinco mayores pools fue un movimiento de mercado natural de los propios mineros queriendo estar en los pools con mayor probabilidad de encontrar bloques y compartir las recompensas. Los pools no mandan en la red, hasta porque son los nodos los que verifican y deciden si los bloques minados son válidos o no.

Y el último punto importantísimo en el funcionamiento de Bitcoin son los halvings, que tienen todo que ver con la minería. Conforme pasa el tiempo, Bitcoin se vuelve cada vez más escaso. La escasez creciente sumada a la demanda creciente es lo que ha causado movimientos parabólicos de subida de precio en Bitcoin. Es el halving el que hace que Bitcoin se vuelva gradualmente más escaso y al mismo tiempo cree ciclos de valorización que se han repetido.


![Slide 126](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-19.jpg)

Halving viene de la palabra "halfing" y significa "cortar a la mitad", en inglés. Quiere decir que cada 210 mil bloques minados, en promedio cada 4 años, el protocolo corta a la mitad la recompensa entregada a los mineros.


![Slide 127](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-20.jpg)

El primer halving sucedió el día 28 de noviembre de 2012, bien al inicio de la red. En la época la red Bitcoin producía 50 bitcoin por bloque de información procesado. Es decir, cada 10 minutos, en promedio, en aquella época, los mineros recibían 50 btc como recompensa. Con el halving de 2012, los mineros pasaron a recibir 25 bitcoin por bloque minado.

En 2016 sucedió el segundo halving, en el bloque 420 mil, y cortó de nuevo a la mitad la emisión. En vez de recibir 25 bitcoin por bloque, cada minero pasó a recibir 12,5 bitcoin por bloque minado. Y el tercer halving sucedió en 2020, el día 11 de mayo, en el bloque 630 mil, donde los mineros pasaron a recibir 6,25 btc por bloque.

El último halving registrado, el cuarto, sucedió en abril de 2024 a la altura del bloque 840 mil. El próximo será en 2028. Y lo bueno de todo esto es que sabemos de antemano en qué bloque va a ser, a la altura del bloque un millón y cincuenta mil. La nueva recompensa va a pasar a ser de 1,5625 bitcoin para los mineros.


![Slide 128](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-21.jpg)

Esta imagen demuestra cómo a cada escalón de la línea naranja, o sea a cada halving, Bitcoin va lentamente volviéndose más escaso y acercándose a la oferta límite de unidades, en la línea en azul.

Esta imagen es increíble, porque muestra cómo Bitcoin es transparente, programable y tiene una política monetaria previsible que no puede ser expandida o modificada. Es algo muy diferente de cualquier otro activo o moneda que cambia las reglas o las políticas monetarias en cualquier momento.

El último satoshi va a ser minado en el año 2140 y es cuando acaba la emisión de nuevos bitcoin. Solo las tasas de la red van a ser la fuente de ingresos de los mineros para pagar los costos de operación.


![Slide 129](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-22.jpg)

Y esta tabla de aquí, es otra forma de mostrar lo mismo. En esta tabla está toda la política monetaria de Bitcoin, desde el primer satoshi, el primer halving hasta el último halving en 2140.

Esta tabla muestra que más del 90% de los Bitcoin ya fueron emitidos y que, hasta el año 2036, van a ser minados el 99% de los bitcoin. El resto, el otro 1% final va a ser creado de 2036 hasta 2140. Son 110 años para minar el 1% de la oferta de bitcoin!

En el año 2030 es cuando, probablemente, la mayor fuente de ingresos de los mineros pasa a ser las tasas. En ese momento, la demanda por Bitcoin debe ser muy grande, al punto de que las tasas cobradas por los mineros sostengan la operación de ellos, incluyendo el mantenimiento de las máquinas y el costo de energía, y ya no tanto la recompensa por el bloque.


![Slide 130](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-23.jpg)

Cuando hablamos de 2140 viene el miedo a lo desconocido y la duda: "qué pasa cuando el último bitcoin sea minado?"

La respuesta es: nada. Este gran cambio ya comienza mucho antes. Ya en 2030 las tasas tienden a ser la principal fuente de ingresos de los mineros. Cuando llegue 2140 los mineros probablemente estarán recibiendo mucho más en tasas que los pocos satoshis ofrecidos por la red, por causa del creciente aumento de la escasez de la moneda, aumento de precio en fiat y aumento del uso de la red.

Y por qué es el halving tan importante?


![Slide 131](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-24.jpg)

Los halvings crean un "shock de oferta": menos Bitcoins quedan disponibles mientras la demanda continúa igual. A cada halving, la cantidad de Bitcoins creada por bloque es cortada a la mitad. Esto reduce la oferta, lo que hace que el precio suba. Si mucha gente quiere comprar Bitcoin y no se pueden crear más unidades, la única forma de convencer a los hodlers de vender es ofreciendo un precio más alto.


![Slide 132](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-25.jpg)

Hodlers son los bitcoiners que acumulan bitcoin para el largo plazo y no venden ni en las mayores caídas de corto plazo. El término hodler se volvió un meme porque un tipo en bitcoin talk, un foro famoso de bitcoin, escribió mal y la gente adoptó la jerga para diferenciarse de la gente de la bolsa tradicional. Esta imagen en la pantalla es el print de la publicación que dio nombre a los hodlers: bitcoiners que sostienen bitcoin con fuerza y no venden de ninguna manera.

Esta subida forma movimientos parabólicos, llama la atención de todos, Bitcoin sale en las noticias y aumenta aún más la demanda. Y es ahí donde comienza la euforia alucinante del bullrun.

Esto sucede porque la única forma de tener la misma liquidez para satisfacer a los nuevos compradores es aumentando el premio para que aquellos que tienen Bitcoin cambien de idea y quieran vender. Es la ley más simple de economía: ley de la oferta y la demanda. Si existe mucha demanda y la oferta se reduce, los precios suben. Como el número de Bitcoin está limitado a 21 millones de unidades y no hay forma de emitir más, cuando la demanda aumenta, la única forma de que la oferta atienda la demanda es con el precio subiendo.

Los halvings causan shocks de oferta que hacen que bitcoin suba hasta un nuevo descubrimiento de precios. Todo este proceso crea movimientos cíclicos de valorización y contracción hasta que el nuevo precio sea definido.


![Slide 133](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-26.jpg)

Los ciclos de Bitcoin están formados por cuatro fases. La primera fase es el BEAR, cuando el mercado es de los osos. Es cuando el precio cae mucho después de un período de alza y es cuando quien entró en el alza se va. 2011, 2014, 2018 y 2022 fueron años de bear de Bitcoin. Es cuando solo salen noticias negativas y quien estaba de turista en Bitcoin, se va.

Después del bear viene una fase MUY agoniante, que es la fase de acumulación. Es cuando bitcoin anda de lado por un año entero. Nada sucede, es puro aburrimiento y parece que no va a acabar nunca.

La siguiente fase es la fase de expansión o crecimiento. Cuando bitcoin comienza a subir lentamente, como quien no quiere la cosa. Es la fase en que los haters atacan porque no creen en una nueva subida y los bitcoiners comienzan a renovar las esperanzas de que un nuevo bull run se acerca. 2012, 2016, 2020 y 2024 fueron años de expansión.

Y por último viene el bull run, la corrida de toros. Cuando bitcoin alcanza la máxima del ciclo y corre como un toro desbocado sin que nada consiga detenerlo. Esta fase es solo alegría, euforia y los haters desaparecen! Bitcoin está en boca de todos, llama la atención y alcanza un nuevo nivel de precio. Cuando la euforia pasa, viene la caída y un nuevo piso de precio se establece, y así vuelve todo al inicio, a la fase de bear. Es una montaña rusa mental y emocional.


![Slide 134](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-27.jpg)

Tanto que para medir el estado emocional del mercado fue creado el índice de codicia y miedo, el fear and greed index. Donde cuanto más cerca de 0 significa "Miedo Extremo", y cuanto más cerca de 100 representa "Codicia Extrema".


![Slide 135](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-28.jpg)

Generalmente las personas quieren que Bitcoin se valorice en línea recta, pero las mayores subidas tardaron un año en llegar al ápice del movimiento. Aquí acerqué para que analicemos el precio de Bitcoin en los halvings. Del halving hasta el tope del ciclo ha tardado cerca de un año en alcanzar ATH (all time high), pero esto no sucede en línea recta, el gráfico oscila mucho, pero con un promedio ascendente de valorización. Bitcoin se valorizó 11 mil por ciento después del primer halving, 2.500 por ciento después del segundo halving y mil por ciento después del tercer halving en 2020, cuando alcanzó el último ATH en 69 mil dólares. En 2024 el cuarto halving sucedió, Bitcoin ya superó los $100k y quien viva verá hasta dónde el precio puede ir en este ciclo.


![Slide 136](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-29.jpg)

Pero todo lo que sube, también baja. Bitcoin a pesar de haber tenido valorizaciones grandes y de que estas han disminuido de intensidad a lo largo de los años, lo mismo ha sucedido con las caídas.

En 2012 Bitcoin tuvo una caída brutal del 93%, después del primer halving 84%, en el segundo cayó 84% de nuevo y en el último halving la caída fue del 77%, menor que en los bears anteriores. Significa que a lo largo del tiempo bitcoin está volviéndose menos volátil. Obvio que está lejos de andar en línea recta, pero ya es posible observar esta tendencia.


![Slide 137](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-30.jpg)

Lo que se observa también es que Bitcoin ha tenido mínimas cada vez mayores a lo largo de los ciclos. En 2012 bitcoin valía menos de un dólar, en 2014 la mínima ya fue diez dólares, en 2016 cien dólares, en 2019 mil dólares y en 2022 diez mil dólares.

Es decir, por más que Bitcoin caiga mucho, ha mantenido precios mínimos cada vez más altos con el paso del tiempo. Pero será que va a ser siempre así? Bitcoin va a continuar valorizándose para siempre?

Este es el tema de la próxima clase. Ahora que aprendiste cómo funciona bitcoin y el historial de ciclos de Bitcoin, llegó la hora de que entiendas por qué tiende a continuar creciendo a largo plazo. Hasta entonces.
