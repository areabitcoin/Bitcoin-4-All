# Clase 10 - Soberanía con tu Bitcoin

### :movie\_camera: Video de la Clase

[![Ver Video](https://vumbnail.com/1085129648.jpg)](https://vimeo.com/1085129648)

:point\_right: [**Haz clic aqui para ver en Vimeo**](https://vimeo.com/1085129648)

***

### Guión Completo

## Clase 10 - ¿Cómo retirar del exchange y tener soberanía con tu Bitcoin?

Bitcoin es un punto de inflexión. Permite que cualquier persona haga la custodia de su propio patrimonio y pueda moverlo cuando y como quiera sin que nadie pueda impedirlo. Ninguna empresa o gobierno puede impedir que muevas tu propio dinero o quitártelo si lo guardas con soberanía. Soberanía es la palabra clave aquí. Tú eres tu propio banco. Pero para hacer esto de verdad, necesitas saber cómo usar herramientas, billeteras y cómo retirar tu Bitcoin de las manos de estos intermediarios. En la clase anterior aprendiste qué son las billeteras de Bitcoin y por qué es importante guardar bien las seeds para siempre tener acceso a tu saldo. El siguiente paso es llenar esa billetera con Bitcoin y comenzar a acumular para el futuro. Entonces en esta clase vamos a considerar que ya tienes bitcoin y quieres enviarlo de la dirección del exchange a la dirección de tu billetera. Pero antes de hacer esto en la práctica, vamos a entender qué son las direcciones y cómo funciona una transacción en la red bitcoin.

![Slide 256](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%2010/Sem%20ti%CC%81tulo-18-01.jpg) Cuando configuras tu billetera bitcoin, ella genera una lista de palabras llamada "seed phrase". Estas palabras representan códigos que te permiten recibir, almacenar y enviar bitcoin. A partir de las seeds, tu billetera va a generar otros códigos encriptados llamados claves públicas y privadas. La clave privada es una secuencia de letras y números que permite firmar transacciones y controlar el saldo de tu billetera. Con ella puedes mover bitcoin de una dirección a otra o importar un saldo específico. Cuando envías bitcoin de una billetera a otra, es la clave privada la que autoriza el saldo a ser movido. Por eso no debes compartir con nadie tu seed ni tus claves privadas de la billetera. Tiene ese nombre por eso: es privada, es una información que debe quedarse solo para ti. La gran diferencia entre seed y clave privada es que una seed phrase (la lista de 12, 18 o 24 palabras) puede recuperar varias claves privadas de diversos saldos vinculados, mientras que la clave privada recupera apenas los saldos de las direcciones que ella generó. Es en estas direcciones donde vas a recibir Bitcoin. Las direcciones son generadas a partir de estas claves y son públicas. Cuando haces una transacción, aparecen en la blockchain para que cualquier persona verifique tu transacción. No es posible descubrir la seed ni la clave privada a partir de una dirección, aunque esté visible en la blockchain de bitcoin. Pero si no cuidas bien las seeds o claves privadas, ahí sí la persona tendrá acceso no solo a tus Bitcoin, sino a todas las claves y direcciones generadas por ella.

![Slide 257](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%2010/Sem%20ti%CC%81tulo-18-02.jpg) Una billetera puede generar miles de direcciones diferentes a partir de la clave pública. Su función es generar direcciones. Incluso una de las buenas prácticas con bitcoin es nunca reutilizar direcciones. Las billeteras siempre están generando nuevas direcciones después de que haces una transacción, para justamente tener más privacidad y evitar la reutilización. Si ya usaste una billetera de bitcoin notarás que en cada transacción la dirección cambia, esto es a propósito. Al fin y al cabo, después de hecha una transacción, las direcciones quedan públicamente visibles en la blockchain y sería más fácil rastrear saldos por asociación. En resumen, la clave privada desbloquea el derecho del dueño de la billetera a gastar, mover, transaccionar las monedas asociadas a esa billetera. Como el nombre dice, es privada y no debes mostrarla a otras personas. Ya la dirección es hacia donde vas a enviar Bitcoin cuando hagas una transacción. Nadie puede adivinar tu clave privada a partir de tu dirección.

![Slide 258](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%2010/Sem%20ti%CC%81tulo-18-03.jpg) Me gusta pensar que la dirección es como si fuera la dirección de tu casa. Hasta la compartes con otras personas, es algo relativamente público, pero tampoco sales con un megáfono por ahí contándole a todo el mundo dónde vives. A veces necesitas mostrar tu dirección para recibir una entrega, pero eso no significa que las personas van a poder acceder a tu casa, para eso es necesario tener las llaves de la puerta. En el caso de las billeteras: las claves privadas. Entonces la dirección es como si fuera la dirección de tu casa y las claves privadas es lo que da acceso a lo que hay dentro de ella: tu saldo en bitcoin. Recordando que tus bitcoin no están guardados dentro de las billeteras. Siempre están en la blockchain. Los bitcoin siempre están en una dirección en la red blockchain y no dentro del dispositivo en sí. Cuando haces una transferencia, le dices a la red que quieres mover "x valor" en bitcoin de una dirección a otra dirección. Las billeteras hacen la función de autorizar esas transacciones que llevan los bitcoins de una dirección a otra a través de una firma digital hecha con la clave privada. Pero entonces, ¿cómo funciona una transacción?

![Slide 259](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%2010/Sem%20ti%CC%81tulo-18-04.jpg) Abres tu billetera, digitas el valor que quieres enviar, pegas la dirección del receptor y haces clic en enviar. Cuando haces clic en enviar, estás firmando la transacción con tu clave privada. Esto es lo que sucede detrás de los códigos de la billetera.

![Slide 260](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%2010/Sem%20ti%CC%81tulo-18-05.jpg) Cuando firmas la transacción probando a la red bitcoin que eres el verdadero dueño de la clave privada de la dirección de la billetera, esa transacción va a una sala de espera, conocida como mempool. Esta es la sala de espera de las transacciones que quedan aguardando hasta ser insertadas en un bloque por los mineros. Las transacciones son registradas en blockchain cuando un minero selecciona las transacciones para formar parte del bloque de información. Tan pronto como un minero inserte la transacción en un bloque, ese bloque es verificado por la red y ella actualiza sus registros de la blockchain. Ahí entonces ese bloque es propagado por toda la red como un bloque válido, con la transacción dentro de él. Cuando una transacción es insertada en un bloque se dice que tuvo una confirmación. Conforme más bloques son minados, más confirmaciones suceden. Generalmente una transacción es considerada irreversible después de 6 confirmaciones, cuando seis bloques pasan. Cuando las confirmaciones suceden, la billetera notifica al usuario, la transacción es considerada recibida y el saldo queda disponible para ser gastado. Así es como las transacciones on chain suceden cuando haces un envío de bitcoin. Bueno, ahora que ya entendiste la teoría, ¡vamos a la práctica!

Te voy a mostrar ahora cómo configurar una billetera desde cero, retirar Bitcoin del exchange hacia esa billetera y recuperar el saldo usando la seed phrase. Para este tutorial elegimos usar Sparrow Wallet !\[https://sparrowwallet.com/], porque es una billetera muy versátil y completa tanto para principiantes como para usuarios avanzados. Es auto custodial, de código abierto y funciona muy bien como billetera coordinadora entre diversas marcas de billeteras hardware: jade, ledger, trezor, coldcard, seed signer, krux... en fin... prácticamente todas las hardwares funcionan con Sparrow. La diferencia es que las billeteras que tienen un software propio como ledger y trezor, de cualquier forma piden que descargues el software ledger live o el trezor suite para hacer las actualizaciones de firmware del dispositivo antes de conectar con Sparrow. También ofrece recursos como crear multisigs, hacer transacciones air gapped, PSBT, gestionar y consolidar UTXO, posibilidades que se enfocan en aumentar la seguridad y privacidad de la billetera. Recordando entonces que Sparrow es una billetera solo de desktop, no tiene una aplicación para celulares ni iOS ni Android. Te voy a dejar el enlace aquí en la pantalla para que la descargues y también una lista con otras billeteras para que pruebes y veas cuál te adaptas mejor. Vamos a comenzar configurando Sparrow. El primer paso es descargar Sparrow e instalar el software.

(video tutorial Sparrow)

Ahí es solo abrir Sparrow y hacer clic en "new wallet" para crear una nueva billetera.

Ahora es solo elegir un nombre personalizado para esa billetera, voy a digitar "btc4all tutorial" y hacer clic en "create wallet".

Esta es la página inicial de Sparrow. Observa cómo la columna de la izquierda está gris y solo las configuraciones están en azul. Significa que está vacía y es necesario crear una billetera, importar o conectar una para que puedas acompañar saldos, recibir y enviar Bitcoin. Ahí en "settings" muestra el tipo de configuración: single sig. Esta configuración significa que necesitas apenas una clave para firmar las transacciones de esa billetera y apenas una lista de palabras para recuperar el saldo. Abajo aparece el tipo de script y más algunos detalles técnicos. Observa cómo en el campo keystore aparecen cuatro cajas con diferentes opciones. Estas son formas de usar Sparrow. Puedes conectar tu dispositivo hardware wallet en Sparrow y mover los saldos a través de ella. Puedes crear una billetera air gapped en la que nunca necesitas enchufar el dispositivo en la computadora para firmar las transacciones. Puedes crear desde cero o importar una billetera que ya tengas y usar Sparrow como una hot wallet o puedes crear una billetera watch only, para apenas acompañar el saldo y no mover nada. Voy a hacer clic en "New or imported software wallet" para crear una billetera desde cero y mostrarte cómo funciona la creación de las claves.

Aquí aparecen algunas formas de crear las palabras de recuperación de la billetera. Voy a hacer clic en la primera opción Mnemonic Words en "use 24 words". Aquí aparece la lista de palabras vacías. Voy a hacer clic en "Generate new" para que la billetera genere mis palabras.

Palabras generadas. Ahora es solo anotarlas con cuidado en el orden en que aparecen. Voy a hacer eso y hacer clic en "Confirm Backup" para confirmar que anoté todo. Sparrow pide digitar las palabras y así confirmar que realmente anoté todo. Observa que hasta que finalice el proceso el ícono "Checksum" aparece como inválido. Al insertar la última palabra de la seed phrase, el checksum cambia a válido, señalizando que fue insertada una secuencia de palabras válida para una billetera de Bitcoin. El siguiente paso es hacer clic en "Create Keystore" en el box azul. Y después en "import keystore".

Listo. Los datos de la seed que generé y todas las claves fueron importados. Ahora es solo hacer clic en "Apply" en la esquina derecha inferior de la pantalla. La billetera preguntará si quiero crear una contraseña para proteger la billetera en caso de que alguien tenga acceso a mi computadora. Voy a hacer clic en "no password", sin contraseña, pero es recomendable que tengas una contraseña para tener una capa más de seguridad en tu billetera.

Observa ahora cómo la columna de la izquierda de repente quedó azul. Significa que ahora la billetera está lista para recibir Bitcoin, enviar y gestionar direcciones. Bueno, ahora voy a mostrar cómo vas a enviar Bitcoin a esta billetera y recuperarla para probar si está todo correcto antes de enviar valores mayores. Es importante hacer esto para que identifiques si está todo funcionando correctamente antes de enviar todo tu hodl a esta billetera. Voy a hacer clic en "receive", recibir.

Y voy a copiar ese código que aparece en el campo "address". Este aquí es mi dirección en la red Bitcoin. Y voy a mostrar cómo vas a enviar Bitcoin aquí a esta billetera recién creada. Para eso voy a retirar Bitcoin del exchange. Voy a usar Coinbase solo como ejemplo, pero el mecanismo es el mismo en otras plataformas.

Bueno, aquí tengo 43 dólares en Bitcoin, cerca de 260 reales, y voy a retirar ese valor del exchange.

Para eso voy a hacer clic en la cuadrícula en la esquina izquierda de la pantalla.

Después hacer clic en "send", enviar.

Voy a pegar la dirección bitcoin de Sparrow, que ya había copiado, aquí en este campo en el tope de la página.

Voy a seleccionar Bitcoin.

Después seleccionar por la red Bitcoin. Todas las otras redes no son Bitcoin, cuidado para no confundir.

Ahora voy a insertar el valor que quiero retirar y hacer clic en preview para ver si las informaciones están correctas.

Todo correcto aquí.

Voy a hacer clic en "Send now", enviar ahora.

Listo. Retiro confirmado.

Ahora es solo acompañar en Sparrow cuándo llegue el valor. Debe tomar algunos minutos para que la red procese esa transacción.

Listo, la transacción llegó aquí en Sparrow: 40.633 satoshis ahora están bajo mi custodia.

Ahora vamos a imaginar que perdí el acceso a ese saldo en la billetera y voy a recuperarla desde cero. Y ahí vamos a ver si el saldo va a reaparecer. Cerré la billetera que creé antes y voy a hacer clic en la tercera opción "import wallet", importar wallet.

Van a aparecer varias formas de recuperación. Voy en la primera, que es la forma como generé antes con 24 palabras.

Ahora es solo insertar las mismas palabras que anoté cuando creé la billetera anterior y hacer clic en "Discover wallet", encontrar billetera. Va a pedir que cree un nombre para esa billetera que quiero importar. Voy a digitar "backup recovery", billetera recuperada, y hacer clic en "Create wallet". Listo. Sparrow trajo todos los datos, las claves y mi saldo en bitcoin.

Ahora voy a hacer el mismo proceso de recuperación en una billetera diferente de Sparrow para que veas cómo independiente de la aplicación o software que uses, es posible recuperar tu saldo en Bitcoin si tienes tu lista de palabras de backup. Entonces voy a recuperar esa misma billetera en Blue wallet, una billetera de celular muy conocida y muy fácil de usar. Voy a abrir mi Blue Wallet en el celular y hacer clic en "Add Now", para crear una nueva billetera.

Voy a seleccionar la última opción "import wallet", importar billetera.

En caso de que quieras crear una billetera desde cero, es solo seleccionar Bitcoin y después en "Create". Pero ahora quiero recuperar la billetera que creé en Sparrow, por eso voy directo a la opción de importar. Voy a digitar aquí las 24 palabras que generé en Sparrow en orden y cuidando de digitarlas correctamente, y hacer clic en "import" cuando termine. Mira ahí, Blue Wallet encontró la billetera.

Voy a hacer clic en "import".

Haciendo clic en ella aparece el saldo que transferí de Coinbase.

Esta es la maravilla de Bitcoin, como es open source puedes recuperar tu saldo en cualquier dispositivo que siga las mismas reglas iniciales que usaste a la hora de generar tus claves. Ahora que ya pasaste por todas las clases de Bitcoin4All, estás listo para poner manos a la obra, comenzar a acumular y a explorar el mundo de Bitcoin. Espero que te haya gustado Bitcoin4All y que este haya sido apenas el comienzo de tu jornada de aprendizaje, al fin y al cabo, Bitcoin no es apenas una tecnología, es un universo de conceptos que une economía, criptografía, redes descentralizadas e innovación continua. Cada día, nuevos desarrollos e ideas surgen, desafiando nuestras nociones tradicionales de dinero y soberanía. Comparte este curso con amigos, parientes y otras personas que también tienen curiosidad y quieren aprender sobre Bitcoin.

¡Hasta una próxima y Opt Out!

***

### Material Complementario

* [E-book de la Clase](https://github.com/areabitcoin/Bitcoin-4-All/tree/main/Bitcoin%204%20All%20-%20Spanish/Ebooks)
* [Slides de la Clase](https://github.com/areabitcoin/Bitcoin-4-All/tree/main/Bitcoin%204%20All%20-%20Spanish/Slides/CLASE%2010)

***

[Anterior](clase-9.md) | [Siguiente](intro.md)

***

#### :loudspeaker: Comparte esta clase!

[Twitter ](https://twitter.com/intent/tweet?text=Estoy%20aprendiendo%20sobre%20Bitcoin!%20Clase%2010%20del%20curso%20Bitcoin%204%20All%20\&url=https://areabitcoin.github.io/Bitcoin-4-All/es/clase-10\&via=aaborges_)[LinkedIn ](https://www.linkedin.com/sharing/share-offsite/?url=https://areabitcoin.github.io/Bitcoin-4-All/es/clase-10)[WhatsApp ](https://wa.me/?text=Estoy%20aprendiendo%20sobre%20Bitcoin!%20Clase%2010%20del%20curso%20Bitcoin%204%20All%20%20https://areabitcoin.github.io/Bitcoin-4-All/es/clase-10)[Telegram](https://t.me/share/url?url=https://areabitcoin.github.io/Bitcoin-4-All/es/clase-10\&text=Estoy%20aprendiendo%20sobre%20Bitcoin!%20Clase%2010%20del%20curso%20Bitcoin%204%20All%20)

#### :chart\_with\_upwards\_trend: Tu Progreso en el Curso

**Clase 10 de 10** (100% completo)
