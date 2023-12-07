# PRÁCTICA 6: ANÁLISIS FACIAL
### Por Alejando Rodríguez Moreno y Nauzet Déniz Perdomo

## 1. Modelo de análisis facial

El modelo que hemos usado para el análisis de las caras ha sido el creado para la demo de buscar parecidos. Hemos usado este modelo basado en el dataset de UTKFace porque contiene muchísimas caras para comparar.

## 2. Uso del modelo de análisis facial

Utilizando como referencia la demo de buscar parecidos, utilizamos los embeddings para el análisis facial y compararlo con las caras que tenemos en el modelo. Obtenemos los 15 vecinos más cercanos a los embeddings que le hemos pasado con el algoritmo kneighbors. Una de las variantes que hemos hecho es buscar la cara con menos parentesco a la mostrada, para ello invertimos los valores de los embeddings para que muestre caras poco parecidas y que sea lo contrario a lo mostrado.

Otra función que hemos realizado es la de mostrar la cara con mayor o menor parentezco que este más cerca a cierta edad que le pasemos, por ejemplo si le pasamos 30 años, nos devolverá la cara con la edad más próxima a los 30 entre los vecinos obtenidos para mostrar. Y por último una función, que muestra si hay entre las caras parecidas o no parecidas, alguna al sexo opuesto al detectado en la imagen pasada.