# Practica 2. Funciones básicas de OpenCV

## TAREA: Realiza la cuenta de píxeles blancos por filas, determina el máximo para filas y columnas (uno para cada) y muestra el número de valores que superan en cada caso 0.95*máximo.

Siguiendo como se hizo para contar los píxeles blancos por columna de la imagen Canny del mandril, se han obtenido los datos desde el eje Y, se ha contado el nº de píxeles blancos, y se ha representado dando una imagen que tiene sentido con lo observado. Además, se ha determinado la columna y la fila con más píxeles blancos, siendo en el caso de la columna, la columna 105 con 191 píxeles blancos, y en el de la fila, la fila 510 con 406 píxeles blancos. Podemos fijarnos que casi en la última fila se ha trazado una línea blanca al añadir Canny a la imagen, esto hace que no haya valores próximos al 95% del máximo en las filas, solo el máximo, ya que el valor es demasiado alto. En cuantos a las columnas podemos encontrar hasta 8 valores que superan el 95% del máximo.

## TAREA: Elige otra imagen, muestra el contenido de alguna de las imágenes resultado de Sobel antes y después de ajustar la escala

En esta tarea hemos escogido la imagen de un fotógrafo en blanco y negro de 256x256. Hemos ajustado de diferentes maneras la escala del Sobel, y se puede observar los resultados en el código.

## TAREA: Aplica umbralizado a la imagen resultante de Sobel (valores 0 a 255 y convertida a 8 bits por ejemplo sobel8 = np.uint8(sobel)), y posteriormente realiza el conteo por filas y columnas similar al realizado en el ejemplo con la salida de Canny. Calcula los máximos por filas y columnas, y determina las filas y columnas por encima del 0.95*máximo. Remarca con alguna primitiva gráfica dichas filas y columnas sobre la imagen ¿Cómo se comparan los resultados obtenidos a partir de Sobel y Canny?

Hemos realizado el mismo proceso hecho con la imagen Canny, pero con la imagen de Sobel umbralizada. Le hemos aplicado 60 en el umbral a la foto Sobel, para poder distinguir la mayor parte de las facciones de la cara. La fila que mayor valor dió fue la 101 con 206 píxeles blancos, y la columna 126 con un valor de 208 píxeles blancos. En ambos casos solo pasan 2 valores por encima del 95% del máximo de píxeles blancos, siendo 1 los mismos máximos. En el Sobel la línea blanca que había en el Canny ha desaparecido, y ambos máximos están más próximos entre sí. Además hay menos columnas por encima del 95%, esto puede variar según el valor del umbral escogido.

## TAREA: Asumiendo que quieren mostrar a personas que no forman parte del curso de VC el comportamiento de una o varias funcioens de las vistas hasta este momento aplicadas sobre la entrada de la webcam. ¿Cuál(es) escogerían?

Escogeríamos la detección de bordes Gaussiana, nos parece una herramienta muy útil y fácil de aplicar. A esto se le puede aplicar diferencia de frames para solo mostrar objetos en movimiento, fácilmente pudiendo detectar personas, animales, etc.

## TAREA: Tras ver los vídeos [My little piece of privacy](https://www.niklasroy.com/project/88/my-little-piece-of-privacy), [Messa di voce](https://youtu.be/GfoqiyB1ndE?feature=shared) y [Virtual air guitar](https://youtu.be/FIAmyoEpV5c?feature=shared) propongan (los componentes de cada grupo) una reinterpretación del procesamiento de imágenes con las técnicas vistas o que conozcan.

Hemos realizado que la cámara capture las zonas donde se encuentre algún tipo de color rojo, y se aplique una capa de blur por encima como si estuviera censurando.
