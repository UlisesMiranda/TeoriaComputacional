Practica 1:
Programar el universo de las cadenas binarias (\Sigma^n). Dada una "n" que introduzca el usuario o que el programa lo determine automáticamente. El rango de "n" debe de estar en el intervalo de [0, 1000].

1. El programa debe de preguntar si quiere calcular otra "n" o no y salir hasta que se le especifique.
2. La salida debe ser expresada en notación de conjunto, debe ir a un archivo de texto.
3. Del archivo de salida, graficar el número de 1s de cada cadena. El eje de las "x" representan la cadena y el eje de las "y" el número de 1s que tiene esa cadena. Específicamente en el reporte, calcular y graficar cuando n=27. Adicionalmente, en un archivo unir todas las cadenas en una sola cadena y segmentarla en subcadenas de 64 bits, para graficar los unos de cada cadena resultante. Al mismo tiempo, con los mismos valores, calcular la gráfica pero ahora logaritmo base 10.
4. En el reporte debe de estar también el código de la implementación.


Practica 2:
Programar el lenguaje binario definido por los números primos. Dada una "n" que introduzca el usuario o que el programa lo determine automáticamente. El rango de "n" debe de estar en el intervalo de [2, 10^7]. "n" determina hasta qué número primo se desea calcular.

1. El programa debe de preguntar si quiere calcular otra "n" o no y salir hasta que se le especifique.
2. La salida debe ser expresada en notación de conjunto, debe ir a un archivo de texto. En un archivo especificar el conjunto en binario y en otro el conjunto en decimal.
3. Del archivo de salida, graficar el número de 1s de cada cadena. El eje de las "x" es la cadena y el eje de las "y" el número de 1s que tiene esa cadena. Específicamente en el reporte, calcular y graficar cuando n=200^3. Al mismo tiempo, calcular adicionalmente dos gráficas más, una calculando su logaritmo en base 2 y otra en base 10.
4. En el reporte debe de estar también el código de la implementación.

Practica 3:
Realizar un programa que simule el funcionamiento de un protocolo utilizando un AFD.

1. El programa debe funcionar automáticamente.
2. Debe de verificar si el protocolo está encendido o apagado y ejecutarse nuevamente si está encendido. El programa deberá determinar automáticamente para detenerse.
3. Generar 10^6 cadenas binarias aleatoriamente de longitud 64.
4. Hacer que el programa se espere 1 segundo.
5. Posteriormente validar cada una de las cadenas con el AFD de paridad.
6. Generar tres archivos de texto para las salidas. El primer archivo tendrá todas las cadenas generadas, el segundo archivo tendrá las cadenas aceptadas y el tercer archivo las cadenas rechazadas. Si el programa entra más de una vez, los archivos deben de almacenar los datos de todas las corridas.
7. Tener la opción de graficar el AFD completo (protocolo y paridad en el mismo grafo).
8. En el reporte debe de estar también el código de la implementación.

Practica 4:
Elaborar un programa para realizar movimientos ortogonales y diagonales en un tablero de ajedrez de 4x4 con dos piezas. Los movimientos y las reglas están explicadas en las láminas del curso de Stanford.

Adicionalmente, el programa debe de contar con las siguientes características:

1. Debe de correr en modo automático (todo) y forma manual.
2. En el caso de forma manual, el usuario podrá introducir la cadena de movimientos o generarla aleatoriamente.
3. El programa puede correr con una pieza o dos.
4. En el caso de dos piezas, la segunda iniciará en el estado 4 y su estado final es el estado 13.
5. Cuando inicie el juego, de manera aleatoria el programa debe decidir quién inicia primero.
6. Una vez definida la cadena de movimientos para uno o dos piezas, se deben generar los archivos de todos los movimientos posibles por pieza, generar otro archivo con todos los movimientos ganadores por pieza. Estos dos últimos archivos servirán para reconfigurar las rutas.
7. Si se reconfigura una ruta y aún así no se puede avanzar, entonces habrá que esperar una iteración para continuar.
8. Graficar el tablero y mostrar los movimientos de una pieza o dos piezas.
9. Si se escoge el modo automático las cadenas generadas no deben ser mayores a 10 movimientos para la animación.
10. El número máximo de movimientos deberá de ser de a lo más 100 símbolos.
11. En un archivo de salida (imagen) dibujar el árbol(les) de la cadena(s) evaluadas en esa corrida.

Practica 5:
Realizar un programa que construya palíndromos de un lenguaje binario. El lenguaje deberá solicitar únicamente la longitud del palíndromo a calcular, de esta manera el programa deberá construir el palíndromo de manera aleatoria. La longitud máxima que podría alcanzar un palíndromo será de 100,000 caracteres. La salida del programa se irá a un archivo de texto y ahí especificarán qué regla se seleccionó y la cadena resultante hasta llegar a la cadena final. El programa deberá ofrecer dos opciones: que el usuario defina la longitud del palíndromo o que lo genere todo de manera automática.

La gramática libre de contexto que construye palíndromos, se define con las siguientes reglas de producción.

(1) P -> e
(2) P -> 0
(3) P -> 1
(4) P -> 0P0
(5) P -> 1P1

Practica 6:
Programar un autómata de pila que sirva para reconocer el lenguaje libre de contexto {0^n 1^n | n >= 1}.

Adicionalmente, el programa debe de contar con las siguientes características:

1. La cadena puede ser ingresada por el usuario o automáticamente. Si es aleatoriamente, la cadena no podrá ser mayor a 100,000 caracteres.
2. Mandar a un archivo y en pantalla la evaluación del autómata a través de descripciones instantáneas (IDs).
3. Animar el autómata de pila, solo si la cadena es menor igual a 10 caracteres.
4. En el reporte deben de estar pantallas del programa en ejecución de todas las características solicitadas.

Practica 7:
El programa de la máquina de Turing debe de reconocer el lenguaje {0^n1^n | n>= 1}. La máquina de Turing se encuentra en el libro de John Hopcroft (ejercicio 8.2, segunda edición). La tabla de transiciones está adjunta en este mensaje.

1. El programa debe de recibir una cadena definida por el usuario o que sea determinada automáticamente por la máquina, una cadena de longitud como máximo de 1000 caracteres.
2. La salida del programa debe ser a un archivo de texto y utilizando descripciones instantáneas en cada paso de la computación.
3. Animar la máquina de Turing con cadenas menores iguales a 10 caracteres.

Practica 8:
Programar el autómata finito determinístico que reconozca las palabras:


Gripa, Contagio, Distancia, Calentura, Covid, Cansancio, Cubrebocas, Dolor
1. Diseñar el NFA.
2. Realizar la conversión a DFA mostrando todo el proceso a través de los subconjuntos y tablas.
3. El programa deberá de leer un archivo de texto, podría ser de una página web.
4. El autómata deberá de identificar cada palabra reservada con el DFA, contarlas e indicar dónde las encontró (posición).
5. En un archivo imprimir la evaluación del autómata por cada carácter que lea y cambio de estado, es decir, toda la historia del proceso.
6. En otro archivo enumerar, contar y anotar donde están las palabras encontradas.
7. Tener una opción para ver el autómata, es decir, hay que graficarlo.

