# Entornos Virtuales en Python con `Requirements.txt`


> ## Importancia de los entornos Virtuales

Los entornos virtuales son cruciales para mantener la **consistencia** y la **reproducibilidad** en el desarrollo de software.
Garantizan que todas las personas que colaboran en un proyecto utilicen las mismas versiones de las bibliotecas, evitando posibles conflictos y facilitando la distribución y ejecución del código en diferentes entornos.

***

> ## Creacion de un Entorno Virtual

Para crear un entorno virtual en Python, puedes utilizar ``venv`` ejecutando el siguiente comando en la terminal ubicado en la *raiz del proyecto*

```bash
> python -m venv nombre_del_entorno
```
> ejemplo : **python -m venv autoTest**

Esto creará un directorio llamado ``nombre_del_entorno`` que contiene un entorno virtual aislado

>NOTA: Este comando nos creara una carpeta con el nombre del entorno en la raiz del proyecto 
> en caso de no tener venv colocar en la terminal **sudo apt install python3-venv**

***

> ## Activar el entorno Virtual

En windows para poder activar un entorno virtual (previamente creado), tenemos que ubicarnos en la raiz del proyecto donde se creo el entorno y colocar en la terminal
- para windows:
    ```bash
    > autoTest\Scripts\activate
    ```
    Se debe agregar el nombre del entorno virtual en nuestra terminal como se ve en la imagen
    ![](../img/terminal.png)
- Para linux:
    ```bash
    source autoTest/bin/activate
    ```

para desactivarlo, colocamos en la terminal

```bash
> deactivate
```

***
> ## Instalando dependencias desde un archivo requirements.txt

El archivo ``requirements.txt`` es un archivo de texto plano que lista las dependencias del proyecto y sus versiones por ejemplo:

```
pytest
selenium
webdriver-manager
allure-pytest
pytest-xdist
faker
```
Para instalar las dependencias desde el archivo ``requirements.txt``, ejecuta el siguiente comando

```bash
> pip install -r requirements.txt
```
Esto instalará todas las bibliotecas enumeradas en el archivo, asegurando que se utilicen las versiones correctas.

> en caso de no tener pip instalado colocar **sudo apt install python3-pip**

