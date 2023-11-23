# PRÁCTICA 5: RECONOCIMIENTO DE MATRÍCULAS
### Por Alejando Rodríguez Moreno y Nauzet Déniz Perdomo

## 1. Detección de vehículos

Para la detección de vehículos se ha usado el modelo YOLO original que nos posibilita localizar los coches en una imagen. Utilizando el modelo YOLO, obtendremos las zonas de píxeles que contienen nuestros vehículos que en nuestra práctica los señalaremos con un rectángulo negro.



## 2. Detección de matrículas

En esta parte de la práctica se puede plantear de 2 formas, suponer donde se ubicaría la matrícula en el coche para obtener la mejor imagen de la matrícula y mandárselo al OCR para que detecte los carácteres, o entrenar otro modelo para la detección de matrículas.

### 2.1. Entrenamiento del modelo

Para entrenar el modelo obtuvimos un dataset en kaggle donde nos proporcionaban 300 imágenes y las etiquetas las cuales tuvimos que cambiar de formato para que se ajustaran al modelo YOLO. Una vez tuvimos las imágenes y las etiquetas preparadas dividimos las imágenes entre las 3 carpetas que se usan durante el entrenamiento, el 70% en la de entrenamiento, el 20% en la de validación y el 10% final en la de test.

![Training](https://github.com/xskere/practicasVC/assets/45332444/4e1ec587-1120-4733-bd9f-6c860a686dc6)

### 2.2. 


