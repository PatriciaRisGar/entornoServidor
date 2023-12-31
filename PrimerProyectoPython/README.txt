Desarrollo de una Aplicación Python

Descripción: En este proyecto, tenéis la libertad de elegir un tema de interés y desarrollar una aplicación Python.

La aplicación debe cumplir con los siguientes requisitos mínimos:

    Descarga de Datos: La aplicación debe ser capaz de descargar datos JSON desde al menos una fuente en línea, como una API web o un archivo JSON remoto.

    Procesamiento de Datos: Los datos JSON descargados deben ser procesados y almacenados en estructuras de datos adecuadas, como listas, diccionarios u objetos personalizados 
    según la naturaleza de los datos.

    Manipulación de Datos: Los usuarios deben poder realizar alguna forma de manipulación de datos, como búsqueda, filtrado, ordenamiento o cálculos sobre los datos descargados.

    Interfaz de Usuario (Opcional): Como apartado opcional, se propone crear una interfaz de usuario simple para interactuar con la aplicación. Esto podría ser una interfaz de 
    línea de comandos o una GUI básica.

    Documentación: Debéis proporcionar documentación clara y concisa que explique cómo funciona su aplicación, cómo se ejecuta y cómo se pueden utilizar sus características. 
    Si la aplicación tiene dependencias parafuncionar, debes explicar claramente cómo se instalan.

    Control de Versiones: Se debe utilizar un sistema de control de versiones, como Git, para realizar un seguimiento de las actualizaciones del código y colaborar en el 
    desarrollo si se trabaja en grupo.

    Entorno en container (Opcional). En este apartado opcional te propongo la creación de un container con docker en el que esté todo configurado y listo para funcionar.

    Presentación: Al final del proyecto, el alumnado debe presentar su aplicación y su funcionamiento ante el grupo y el profesor, destacando las características 
    implementadas y los problemas superados. Además, deberá crear un vídeo de menos de 2 minutos con los highlights de la app.



Temática:

    He decidido usar PokéAPI (https://pokeapi.co/api/v2/pokemon-form/).
    Mi aplicación escogerá un pokemon aleatoriamente y mostrará la imagen al usuario, el cual debe introducir el nombre del mismo. 
    El lenguaje a usar es Python3 y crearé la interfaz para el usuario con Tkinter.

Documentación:
    Presento mi primera aplicación: Pokemón adivino, en el que intento recrear el juego de televisión
    en el que ponían la sombra del pokemon y tenías que decir su nombre.

    Al iniciarse genera un número random que corresponde al ID del pokemon en la api. Una vez en la api
    del pokemon correspondiente, recogemos los datos de su nombre y su imagen (frontal).
    Para así crear la ventana en la que nos aparece la imagen del pokemon y una entrada para que el usuario
    introduzca el nombre que considere oportuno.
    Al pulsar el botón se procesan los datos en el controlador para comparar que sean iguales. De ser así
    aparece una ventana modal indicando el acierto.De lo contrario ejecuta una ventana modal de error.

    Tras cerrar la ventana modal, habilito un botón que permite finalizar el programa.

Ejecución:

    Para instalar las dependencias necesarias, vamos a ejecutar el siguiente comando:
        $ pip install -r requirements.txt
        tkinter ~= 0.1.0 es una biblioteca que no se instala con pip: 
            sudo apt-get install python3-tk
            
    *es posible que nos informe de una nueva version de pip. Ignoramos.

    A continuación ejecutamos la aplicación. La ruta completa hasta llegar a ventana.py.