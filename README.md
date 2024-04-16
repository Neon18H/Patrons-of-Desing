# Patrons-of-Desing
:)
Estos patrones de diseño fueron creados usando "Python"

#Patrones creacionales
Estos patrones proporcionan mecanismos de creación de objetos que incrementan
la flexibilidad y la reutilización del código existente.

#Builder: -----> Patrones Creacionales

![Patrones-colegiados-Construccion-recomendada-de-constructores-de-viviendas-superiores](https://github.com/Neon18H/Patrons-of-Desing/assets/92942417/a5c2370e-7fd9-48ed-b7e2-2bbb07d56022)


Imagina que quieres construir una casa con bloques y estos bloques tiene un colo asignado

Columns-Rojo ❤️(Tipo de Columna)

Fachada-Verda 💚(Tipo de Fachada)

Interior-Marron 🤎(Tipo de interior)

Entones supongamos que quieres construir una casa moderna y un edificio, pero cada uno de estos sigue un orden de construccion diferente
ademas usan un tipo diferente de: Columnas , fachadas, interior. Entonces en lugar de mezclar todos estos bloques de colores y sus tipos y 
confundirte, hay unas instruccuines para cada tipo de construccion la cual quieras realizar, estonces cada instruccion tiene un tipo de construcctor
de esta manera habra un construcctor para casas modernas y otros para edificios.

El patrón Builder te ayuda a separar la construcción de un objeto complejo (como una casa) de su representación, permitiéndote crear diferentes tipos de objetos usando los mismos pasos de construcción, pero con diferentes detalles.


#Decorator: --------- > Patrones Estructurales

![Decorator_example](https://github.com/Neon18H/Patrons-of-Desing/assets/92942417/6951f349-f288-4ad3-96f7-629be717d0b8)

imaginas que estas en tu juego favorito Call of Duty  tienes un arma, y este patron trata de ir agregando accesorios a esta arma
decorandola. Entonces comensarias con un arma base y le puedes ir agragando consas para potenciarla, como una culata, o un tubo mas largo
para disparos a larga distancia, cada uno de estos accesorios se le suma al arma base y la hace mas genial.

El patrón Decorator funciona de manera similar. Te permite agregar nuevas funcionalidades o comportamientos a un objeto existente sin cambiar su estructura básica. Cada decorador envuelve el objeto original y agrega su propio toque especial, como agregar capas de decoraciones a un arma.


#Observer: ---------------> Patrones de comportamiento


![e-El-papel-del-supervisor-en-las-organizaciones](https://github.com/Neon18H/Patrons-of-Desing/assets/92942417/e36c0ffe-d716-455f-94c3-e13c825b9665)

Ahora imagina que trabajas en una planta nuclear y tu eres supervisor, en este plantel nuclear, hay un reactor nuclear y este siempre te avisa
cuando la temperatura cambia, cuando la temperatura cambia, este reactir avisa y luego tu como supervisor decides que hacer.
En esta situacion: 
Tu eres el observador, el reactor nuclear "objeto observedo", cambio de temperatura es el "evento"

Observador (tú): Eres la persona que está observando el comportamiento del reactor nuclear.
Objeto Observado (Reactor nuclear): Es el objeto que está siendo observado. En este caso, Reactor nuclear está atento al cambio de temperatura.
Evento (cambio de temperatura): Es lo que sucede y que interesa al observador. Cuando la temperatura cambie, es un evento que ocurre y que el reactor nuclear nota 

El patrón de diseño Observer es como una relación entre tú (el observador) y el Reactor nuclear (el objeto observado). Reactor nuclear siempre te notifica cuando algo importante sucede (como cuando la temperatura varia), y luego tú decides qué hacer en función de esa notificación (revisar el reactor nuclear). De esta manera, puedes estar al tanto de lo que está sucediendo sin tener que estar constantemente vigilando los cambios de temperatura tú mismo.


#Iterator: ---------------------> Patrones de comportamiento


![traditional-wooden-steps-in-vintage-library-royalty-free-image-1666591817](https://github.com/Neon18H/Patrons-of-Desing/assets/92942417/02470678-be5c-4495-9385-9f9744b3f3ac)



Imagina que estás en una biblioteca y necesitas encontrar un libro específico en una gran estantería llena de libros. La estantería es como la colección de elementos, y los libros individuales son los elementos dentro de esa colección.

Ahora, sin el patrón Iterator, tendrías que saber cómo está organizada la estantería (quizás por género, autor, o título) y buscar manualmente el libro que necesitas, exponiéndote a la complejidad de la organización interna de la biblioteca.

Sin embargo, con el patrón Iterator, puedes pensar en el bibliotecario como un Iterador. Le pides al bibliotecario un libro y él te da uno a la vez, sin que tengas que preocuparte por cómo están organizados los libros en la estantería. El bibliotecario conoce la estructura interna de la estantería y te da los libros uno por uno sin revelar esa estructura.

La estantería es la colección de elementos.
Los libros individuales son los elementos dentro de la colección.
El bibliotecario es el Iterador, que te permite recorrer la colección sin exponer su estructura interna.


 

