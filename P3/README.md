# Practica 3. Detección de formas

## TAREA: Captura una o varias imágenes con monedas no solapadas y algún objeto que no lo sea. Filtra los contornos que no se correpondan con monedas, y muestra el número total de monedas presentes en la imagen. Una alternativa consiste en contar círculos utilizando la Transformada de Hough. La selección de parámetros puede ser "divertida", más [información](https://docs.opencv.org/4.x/da/d53/tutorial_py_houghcircles.html)

Con la técnica de Hough resultó más fácil filtrar las monedas, por tanto se utilizó la función HoughCircles de cv2. Con esto y un filtrado del área del círculo, se puede de forma relativamente clara encontrar fácilmente las monedas.

## TAREA: Captura una o varias imágenes con monedas no solapadas, y otras con monedas solapadas. Identificada una moneda de un euro en la imagen, por ejemplo con un clic de ratón, calcular la cantidad de dinero presente en la imagen. ¿Qué problemas han observado?

Para el conteo el dinero, se utilizó la función ya determinada anteriormente de Hough. Gracias a que se indica el área del círculo, se puede estimar qué moneda es cuál, teniendo como referencia un euro clickado anteriormente. Hay varios problemas con este método, dependiendo de la perepectiva, alguna monedas puede ser detectada como un círculo de mayor tamaño de lo que realmente es.

## TAREA: Estas tres imágenes han sido extraidas de las imágenes de mayor tamaño contenidas en la carpeta. Determina patrones geométricos para cada una de las tres clases y evalúa los aciertos y fallos con las imágenes completas la matriz de confusión. Para cada clase, determina el número de muestras que se clasifican correctamente de dicha clase, y el número de muestras que se clasifica incorrectamente por cada una de las otras dos clases.

Con las técnicas de umbralizado vistas, se ha detectado los contornos de cada una de las clases en sus respectivas imágenes. Una vez obtenido los contornos, se ha calculado las diferentes propiedades geométricas que se resaltan en la tarea que en el código se verían así:
<p align="center">
    <image src="images/calculoGeometrias.PNG" alt="Descripción de la imagen">
</p>

Estas características geométricas de las figuras que nos da los contornos se han guardado para luego crear un modelo de predicción. Para el proceso de obtener los contornos de las imágenes de mayor tamaño que son usadas para la validación de nuestro modelo, se han usado diferentes métodos para eliminar el ruido que había en las imágenes, que son redimensionar la imagen a un 40%, recortar partes de la imagen donde no hay ningún elemento o pintar zonas donde habían sombras con el color que el umbralizado entiende que es el fondo.

Por último para la clasificación se han utilizado diferentes modelos observando los usados en el trabajo original, sin obtener ningún éxito rotundo. Estos modelos fueron el K Nearest-Neighbor con valor de 5 vecinos, el SVC con kernel lineal, el SVC con kernel RBF con valor en C igual a 15 y en gamma igual a 0.05, y el Random Forest con 100 estimadores. Para todos estos clasificadores se ha hecho una matriz de confusión. Los resultados no han sido buenos, para KNN obtuvo un Accuracy del 40%, Precision 26%, Recall 40% y F1 Score 24%, prácticamente todos los aciertos se realizan en la primera clase que en nuestro caso es la de fragmentos, siendo incapaz de detectar de las otras 2 clases. En el SVC lineal obtuvo un Accuracy del 49%, Precision 39%, Recall 49% y F1 Score 42%, el resultado es mejor siendo capaz de predecir entre fragmentos y alquitrán, pero sin detectar un solo pellet. El modelo SVC con kernel RBF obtuvo un Accuracy del 30%, Precision 9%, Recall 30% y F1 Score 14%, predijo todos las muestras como pelet. Y finalmente el modelo de Random Forest obtuvo un Accuracy del 53%, Precision 40%, Recall 53% y F1 Score 45%, como el lineal predijo entre fragmentos y alquitrán pero no detecta pellet.
