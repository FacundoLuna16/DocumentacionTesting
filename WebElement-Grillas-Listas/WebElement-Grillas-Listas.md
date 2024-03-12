# Elementos Web - Listas

En una pagina web nos podemos encontrar distintos tipos de elementos, hasta el momento analizamos los siguientes:
- Caja de texto (input)
- texto (lebel) 
- botones (button)

Pero ademas de estos existen mas elementos, como listas que pueden estar desplegadas o pueden ser desplegables


#### Listas

Como mencionamos anteriormente, existen 2 tipos de listas

- Listas Desplegadas:
    ![Lista desplegada](./img/listaDesplegada.png)

- Listas Desplegables:
    ![Lista Desplegable](./img/listaDesplegable.png)

En ambos casos se trabajan de la misma manera, pero hay que tener en cuenta que las listas desplegables estaran disponibles una vez sean desplegadas...


```python
    list_locator_origen_destino = (By.XPATH, "//ul[@role='listbox']//li[@role='option']")

    ####....

    @allure.step('Seleccionar origen')
    def seleccionar_lista_opciones(self, origen):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.list_locator_origen_destino)
        )
        elementos_destino_origen = self.driver.find_elements(*self.list_locator_origen_destino)

        for elemento in elementos_destino_origen:
            if origen in elemento.text:
                elemento.click()
                break
```

**elementos_destino_origen**: devuelve una lista con cada uno de los elementos que tengan ese locator, esta lista es de webElement


En ocaciones en nuestras paginas web nos encontraremos con etiquetas `Select`
```html
<Select>
    <Option>hola</Option>
    <Option>hola1</Option>
    <Option>hola2</Option>
    <Option>hola3</Option>
</Select>
```
y a estas etiquetas selenium las trata de un matera diferente

```python
select_locator=(By.XPATH, "//select[@name='language']")
def seleccionar_opcion(driver, valor):
    """
    Función para seleccionar una opción de un elemento <select> utilizando su valor.
    
    :param driver: Instancia del navegador WebDriver.
    :param valor: Valor de la opción que se desea seleccionar.
    """
    select_element = Select(driver.find_element(*select_locator))
    select_element.select_by_value(valor)
```


