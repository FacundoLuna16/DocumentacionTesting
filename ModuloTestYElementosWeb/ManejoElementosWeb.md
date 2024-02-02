# Identificación de Elementos Web en Clases

En este ejemplo, utilizaremos Page Object para estructurar nuestro test.

- Creamos una clase llamada [`StackHomePage`](#stackhomepage) que será la Page Object. En esta clase, definimos atributos que representan los elementos web de la página y métodos que proporcionan funcionalidades sobre esta página.

Para identificar los elementos web en Python, podemos hacerlo de dos formas:

1. Identificando en variables:

```python
buscador = "//input[@placeholder='Buscar…']"
btn_usuarios = "#nav-users"
```
En el primer ejemplo, utilizamos XPath, y en el segundo, CSS.

2. Otra forma es identificarlos como tuplas:
```python
buscador = (By.XPATH, "//input[@placeholder='Buscar…']")
btn_usuarios = (By.CSS_SELECTOR, "#nav-users")
```
**Este enfoque es más flexible y fácil de mantener, ya que permite cambiar el tipo de localizador sin modificar todos los lugares donde se utiliza el elemento web.**


## ¿Cómo utilizo cada uno?
Según la forma en la que desees marcar, lo que haremos es utilizar el método del driver llamado `find_element`, al cual le pasaremos como parámetro el elemento web.
### para el caso 1
> formato find_element(tipoElemento, identificador)
```python
find_element(By.XPATH, self.buscador)
```

### para el caso 2

utilizando una tupla solo debemos pasarle la variable un previamente un ``*`` para desempaquetar la tupla

```python
find_element(*self.buscador)
```


