## Instrucciones para montar el ambiente virtual y dataset (Para Windows)
1.- Importar a mongodb el archivo .JSON ubicado dentro de la carperta dataset

2.- Instalar la dependencia virtualenv utilizando pip install virtualenv

3.- Crear el ambiente virutal utilizando el comando virtualenv env

4.- Crear el repositorio para el ambiente virtual utilizando el comando python -m venv mongo

5.- Navegar hasta el directorio de Scripts de la carpeta del ambiente virtual (En este caso dentro de la carpeta mongo)

6.- Iniciar el ambiente virtual con el comando ./activate 

7.- Instalar la dependencia de mongo para python utilizando el comando pip install pymongo

8.- Retroceder hasta la carpeta raiz del proyecto y navegar hasta la carpeta src y iniciar el programa con el comando Python ./CRUDmongo.py
