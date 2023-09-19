# Practica 1

## TAREA: Crea una imagen, p.e. 800x800, con la textura del tablero de ajedrez

Para crear un tablero de ajedrez debemos tener en cuenta las dimensiones del tablero que es de 8x8, por lo que al hacerlo en una imagen de 800x800 píxeles cada casilla tendrá una dimensión de 100x100 píxeles. Entonces para hacer el tablero realizaremos dos bucles recorriendo ambos ejes de la imagen e intercalando los colores de las casillas entre blanco y negro cada 100 píxeles dando así una imagen con textura de tablero de ajedrez.

## TAREA: Crear una imagen estilo Mondrian

## TAREA: Modifica de alguna forma los valores de un plano de la imagen



## TAREA: Pintar círculos en las posiciones del píxel más claro y oscuro de la imagen  ¿Si quisieras hacerlo sobre la zona 8x8 más clara/oscura?

En esta tarea se ha logrado pintar un círculo blanco en el pixel más ocuro y un círculo negro en el pixel más claro de la imagen mostrada por webcam. Para ello hemos creado una función para que lea todos los píxeles y sumando sus valores RGB determinar si
es el valor más oscuro o más claro. En caso del pixel más claro será el que mayor valor tenga al sumar los valores RGB, y en el más oscuro será el de menor valor.

En el caso de la zona 8x8 se ha conseguido también, pero requiere mucho más cálculos por lo que el rendimiento en tiempo real con la webcam se ve afectado. Estos cálculos extra vienen ya que de cada pixel, menos los últimos 7 de la altura y del ancho de la imagen,
hay que sumar todos sus valores RGB en una zona de 8x8 para determinar el brillo de las zonas, por lo que tendriamos que sumar los valores de 64 pixeles por cada pixel. Esto ralentiza bastante el proceso por eso es mejor usarlo en una imagen estática o con la webcam pero
con un temporizador para que no este constantemente calculando y ralentizando el funcionamiento de la misma.

## TAREA: Haz tu propuesta pop art


