# Scraping Properati.com

## Descripción
El obgetivo de esta practica es realizar scraping  del sitio web properati.com, dicho sitio web almacena información de bienes inmuelbles en Ecuador. Por lo que se intentará obtener información como: estado, precio, localización, de los inmuebles encontrados. 

## Características principales
##### - Extracción de datos: 
Utilizando Pycharm se realiza scraping en la pagina de properatti.como y se obtiene información de los bienes inmuebles publicados en dicha pagina como: precio, localización, número de habotaciones, número de baños, tamaño, entre otros.
##### - Procesamiento:
Una vez obtenida la información requerida del sitio web se creo una conexión hacia mondodb donde almacenamos la información obtenida para en lo postrior procesarla.
##### - Sitio web:
Con los datos almacenasdos en mondobd se intentará crear un sitio web y mostrar la información recopilada desde el sitio web properati.com.

## Requisitos
- Pycharm, Python 3.11
- Github, Mondobd

## Desarrollo
1. Se utiliza Pycharm con Python 3.11 como consola de progtramación.
2. Se instala las librerias necesarias para realizar el proceso de scraping y conexión con la base de datos como son selenium, pymongo, python-dotenv.
3. Una vez instalada las librerías empezamos a programar con el obgetivo de tener solo la información necesaria.
4. A continuación es necesario crear una conexión hacia mondobd para almacenar la información obtenida, para lo cual creamos el archivo mongo.py en el cual se ejecutarán la conexión. Para este necesitaremos la información de usuario, contraseña y host de mongodb.
5. Para proteguer los datos y estructura de datos crearemos un archivo .env el cual se excluye en la publicación, en este repositorio almacenaremos las claves y evitaremos fuga de información.  
6. Lo siguiente es crear un sitio web que permita mostrar los datos extraidos de properati.como y luego almacenados en MOngoDB.

## Retos - Dificultades
- Iniialmente el encontrar un sitio web que no bloquee el scriping fue complicado, en algunas paginas al ejecutar el debug se veía que que retornba un error de click, lo que iventigando quería decir que como no se habia realizado un click la información no era visible.
- Una vez escogida la pagina que no contenga este tipo de conexiones, lo dificil fue encontrar las clases y dependencias necesarias, una vez adquirida la espertis fue muy rapido.
- Finalmente y los mas dificil fue poder extraer la información desde mondodb para que los datos puedan mostrarse en un sitio web. 

## ANEXOS
![ Repositorio gtihub](https://github.com/Inolivos89/Inolivos-final)

![ Repositorio Mongodb](https://cloud.mongodb.com/v2/64ff903fd296196a1917a149#/overview)
