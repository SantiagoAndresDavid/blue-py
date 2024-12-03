# Proyecto React con Backend Python

Este proyecto es una aplicación React que se conecta a un backend Python. Para facilitar la configuración y la construcción de la imagen Docker, se utilizan variables de entorno que se deben establecer correctamente.

## Variables de Entorno

El proyecto utiliza las siguientes variables de entorno:

### Variables en el archivo .env de React

Estas variables son necesarias para la configuración del frontend en React. Deben estar definidas en el archivo .env dentro de la raíz del proyecto.

- *REACT_APP_HOST_PYTHON_BACKEND*: La URL o dirección IP del backend Python.
  - Ejemplo: localhost

- *REACT_APP_PORT_PYTHON_BACKEND*: El puerto en el que el backend Python está escuchando.
  - Ejemplo: 22222

#### Ejemplo de archivo .env:

env
REACT_APP_HOST_PYTHON_BACKEND=localhost
REACT_APP_PORT_PYTHON_BACKEND=22222

## instalacion

### primer paso 
posicionate en el proyecto he instala las dependencias 
sh
npm install 

### segundo paso 
construye la imagen de la siguiente forma 
sh
docker build \
  --build-arg REACT_APP_HOST_PYTHON_BACKEND=localhost \
  --build-arg REACT_APP_PORT_PYTHON_BACKEND=1234 \
  --build-arg REACT_APP_HOST_NODE_BACKEND=localhost \
  --build-arg REACT_APP_PORT_NODE_BACKEND=7777 \
  -t react-app .

### tercer paso 
construye la imagen de la siguiente forma:
sh
docker run -p 80:80 react-app

(para cambiar el puerto se puede sustituir 3000:80)
