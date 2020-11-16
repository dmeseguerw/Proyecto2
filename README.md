# Proyecto 2: Página Web para citas de veterinaria
Este proyecto consiste en el desarrollo de una página web para la creación de citas veterinarias, esta página web brinda información sobre la veterinaria y proporciona una interfaz tanto para usuario como para administradores de la página. El proyecto crea utilizando la biblioteca de django y se entrega con un dockerfile que permite la creación de un contenedor para la misma.

# Integrantes
* Daniel Meseguer
* Esteban Valverde

# Requirements
* Django>=3.0,<4.0
* django-widget-tweaks>=1.4.5
* django-bootstrap4>=2.0.0
* js.jquery>=3.3.1
* django-bootstrap-datepicker-plus>=3.0.5
# Uso con python
Se puede utilizar la aplicación instalando los requerimientos y ejecutándola directamente con python o utilizando el contenedor, a continuación se detalla el uso para ambos casos. Dentro de la carpeta del proyecto en Proyecto2/Veterinary, ejecutar el siguiente comando:

* Ejecución de la aplicación:
```sh
python3 manage.py runserver
```

* Uso en el navegador, ingresar en la barra de búsqueda la siguiente direccion:
```sh
localhost:8000
```

# Uso con docker
Ejecuctar la creación del contenedor dentro de la carpeta Proyecto2/:

* Creación del contenedor:
```sh
docker build --tag proyecto2:latest .
```

* Ejecución del contenedor:
```sh
docker run -p 80:80 proyecto2:latest
```
Para esta ejecución se realiza la exposición del puerto 80 (por defecto del localhost) y se mapea con el 80 que se usa en la aplicación dentro del contenedor, esta selección se realiza para simplificar el uso en el navegador y solo requerir acceder a "localhost".
* Uso en el navegador, ingresar en la barra de búsqueda la siguiente direccion:
```sh
localhost
```
