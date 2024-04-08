## Instrucciones para montar el ambiente virtual y dataset (Para Windows)
Se estará utilizando el puerto por defecto de Mongodb para la conexion local (27017)

1.- Crear una nueva base de datos dentro de Mongodb con nombre pythonCrud y una coleccion de nombre crud

2.- Importar a la coleccion el archivo .JSON ubicado dentro de la carperta dataset

3.- Instalar la dependencia virtualenv utilizando pip install virtualenv

4.- Crear el ambiente virutal utilizando el comando virtualenv env

5.- Crear el repositorio para el ambiente virtual utilizando el comando python -m venv mongo

6.- Navegar hasta el directorio de Scripts de la carpeta del ambiente virtual (En este caso dentro de la carpeta mongo)

7.- Iniciar el ambiente virtual con el comando ./activate 

8.- Instalar la dependencia de mongo para python utilizando el comando pip install pymongo

9.- Retroceder hasta la carpeta raiz del proyecto y navegar hasta la carpeta src y iniciar el programa con el comando Python ./CRUDmongo.py

## Esquema de la base de datos

La coleccion de la base de datos consiste en registros de las puntuaciones hasta el episodio 958 del anime One Piece

La columna Unnamed indica la id del capitulo (Comenzando desde el 0)

La columna rank esta obtenida mediante la cantiad promedio de votos por episodio ajustada entre el rating promedio (0 a 300 con decimales)

La columna trend representa la cantidad de votos del episodio en los ultimos 7 dias (0 a 10 con decimales)

La columna season es la temporada de emision del capitulo (int)

La columna episode es el numero del episodio (int)

La columna name es el nombre del episodio (String)

La columna start es el año donde se estreno el episodio (int)

La columna total_votes es la cantidad total de votos del capitulo (int)

La columna average_rating (de 0 a 10 con 1 decimal)

## Como utilizar el programa

Debe ingresar unicamente el numero de la accion a realizar entre el 1 y 5, cualquier numero superior o caracter ingresado se considerara como salir del programa y cerrar la conexion con Mongodb

Para las opciones de buscar por episodio, Actualizar y Eliminar se debe ingresar el numero del capitulo sobre el que se desea realizar la accion, para la opcion de insertar un dato deberá ingresar cada uno de los campos solicitados para rellenar las columnas, para la opcion de mostrar todos solo deberá seleccionar el numero de la opcion