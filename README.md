# Cuadernos de Jupyter

Este repositorio contiene una colección de cuadernos de Jupyter relacionados con Complejos . Los cuadernos cubren las diferentes operaciones que puedo realizar con los números complejos, proporcionando ejemplos y análisis que pueden ser útiles.

## Contenidos

1. **ComplexIntro** - En este cuadernos nos presentan el primer acercamiento a los numeros complejos y su forma de operar. También nos dan una introducción a como generar gráficas. 
2. **Complex_Vector_Matrix_Operations_with_NumPy-2** - Este cuaderno explora los conceptos fundamentales de los espacios vectoriales complejos. Comienza con una explicación teórica sobre las operaciones clave en estos espacios, como la suma de vectores, la multiplicación por escalares complejos y la conjugación. También incluye ejemplos prácticos en NumPy para manipular vectores columna complejos, demostrando operaciones como transposición, adjunto y conjugado.
3. **TallerEsp.Vect-ProdInterno-VectoPropios** - Este cuaderno se centra en los valores y vectores propios, propiedades del producto interno y espacios vectoriales.
4. **TallerEsp.Vect-Hermitian-Unitary-Tensor-Circuits** - Este cuaderno se centra en las matrices hermitianas y unitarias. Explica las propiedades de las matrices hermitianas, como la relación con los valores propios reales y vectores propios ortogonales, y cómo se utilizan en la representación de observables en sistemas cuánticos. Además, incluye ejemplos en Python para implementar estas matrices y comprender sus aplicaciones en el contexto cuántico.

## Requisitos

Para ejecutar los cuadernos, necesitarás instalar las siguientes herramientas y bibliotecas:

- Visual Studio Code: Lo utilizaremos para crear el entorno virtual de Python 
- [Python 3.12](https://www.python.org/downloads/)
- Bibliotecas necesarias (puedes instalarlas con el siguiente comando): pip
    1. **Numpy**
    2. **matplotlib.pyplot**
    3. **ipywidgets**

## ¿Cómo obtener una copia del repositorio?
### Pre-requisitos
Antes de comenzar con la ejecución de este proyecto, es necesario asegurarse de que se tiene instalado Python en su computador, debido a que este es el lenguaje de programación utilizado para desarrollar este proyecto. 
En caso de no tenerlo siga los siguientes pasos:
1. Dirigirse a la página https://www.python.org/downloads/
2. Dar click en la opción de descarga
   - ![image](https://github.com/alexandrac1420/CNYT/assets/138069735/03d02dfb-a346-4bc8-8e9c-066816e2f80e)
   
4. Ejecutar el programa que se descarga automáticamente.

### Instalación 
Para instalar la librería debe tener en cuenta estos pasos:
1. Abra la carpeta en donde desea guardar la librería.
2. De click derecho y seleccione la opción "Git Bash"
3. Clone el repositorio utilizando el comando 'https://github.com/Mar972310/CNYT.git'
4. Ejecute la seccion que quiera compilar o todo el cuaderno.

# Libreria matrices y vectores utilizando la libreria Numpy
Este proyecto consiste en desarrollar un programa que permita realizar operaciones de vectores y matrices complejas, tales como:
* Adición de vectores complejos.
* Inverso (aditivo) de un vector complejos.
* Multiplicación de un escalar por un vector complejo.
* Adición de matrices complejas.
* Inversa (aditiva) de una matriz compleja.
* Multiplicación de un escalar por una matriz compleja.
* Transpuesta de una matriz/vector
* Conjugada de una matriz/vector
* Adjunta (daga) de una matriz/vector
* Producto de dos matrices (de tamaños compatibles)
* Función para calcular la "acción" de una matriz sobre un vector.
* Producto interno de dos vectores
* Norma de un vector
* Distancia entre dos vectores
* Valores  y vectores propios de una matriz
* Revisar si una matriz es unitaria
* Revisar si una matriz es Hermitiana
* Producto tensor de dos matrices/vectores

## Sintaxis operaciones 
A continuación se presenta la sintaxis correcta para el uso de las operaciones disponibles:
* __Adición de vectores complejos__:add_complex_vectors (_vector 1, vector 2_)
* __Inverso (aditivo) de un vector complejos__:iverso_vector (_vector_)
* __Multiplicación de un escalar por un vector complejo__:multiplication_scalar_vector (_escalar, vector_)
* __Adición de matrices complejas__: add_complex_matrix(_matriz 1, matriz 2_)
* __Inversa (aditiva) de una matriz compleja__:inversa_complex_matrix(_matriz_)
* __Multiplicación de un escalar por una matriz compleja__: multiplication_scalar_matrix(_escalar, matriz_)
* __Transpuesta de una matriz__: transpose_complex_matrix_vecto(_matriz_)
* __Conjugada de una matriz/vector__: conjugate_complex_matrix_or_vector(_matriz_)
* __Adjunta (daga) de una matriz__: adjunct_matrix_or_vector(_matriz_)
* __Producto de dos matrices (de tamaños compatibles)__: product_complex_matrix(_matriz 1, matriz 2_)
* __Función para calcular la "acción" de una matriz sobre un vector__: action_matix_vector(_matriz, vector_)
* __Producto interno de dos vectores__: product_int_vectors(_vector 1, vector 2_)
* __Norma de un vector__: norm_vec(_vector_)
* __Distancia entre dos vectores__: distance(_vector 1, vector 2_)
* __Valores y vectores propios de una matriz__: values_vector(_matriz_)
* __Revisar si una matriz es unitaria__: unit_matrix(_matriz_)
* __Revisar si una matriz es Hermitiana__: hermitian_matrix(_matriz_)
* __Producto tensor de dos vectores o matrices__: prod_tens_vec(_vector 1, vector 2_)

## Construido con
* Phyton 3.12.5
  
## Autor 
__Maria Valentina Torres Monsalve__ 

   
