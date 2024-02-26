# Esperas en Python con Selenium
    
La mayoría de las aplicaciones web utilizan técnicas AJAX. Cuando el navegador carga una página, los elementos dentro de esa página pueden cargarse en diferentes intervalos de tiempo.


Selenium Webdriver proporciona dos tipos de esperas: implícitas y explícitas.

Una espera **explícita** hace que WebDriver espere a que se produzca una determinada condición antes de continuar con la ejecución.
Una espera **implícita** hace que WebDriver sondee el DOM durante un cierto período de tiempo al intentar localizar un elemento.


- #### Esperas Explicitas
    una espera ``explícita`` te permite especificar un tiempo máximo de espera para que se cumpla una cierta condición. Sin embargo, si la condición se cumple antes del tiempo máximo, Selenium continuara con la ejecucion sin esperar el tiempo completo.

    Continuando con el ejemplo de Stack Overflow, teniamos un elemento que era un botton para aceptar la cookies, La forma para esperar este boton es la siguiente

    ```python
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.btn_aceptar_cookies))
    ```
    En este codigo, selenium esperara un maximo de 10 segundo para encontrar el elemento
    si no se encuentra lanza una exception del tipo ``TimeoutException``

    - Condiciones Esperadas
    Existen algunas condiciones comunes que se utilizan con frecuencia

    1. **title_is(titulo)**: Espera a que el título de la página sea exactamente igual a ``titulo``
        ```python
        WebDriverWait(driver, 10).until(EC.title_is("Stack Overflow en español"))
        ```
    2. **title_contains(titulo_parcial)**: Espera a que el título de la página contenga la cadena `titulo_parcial`
        ```python
        WebDriverWait(driver, 10).until(EC.title_contains("Stack"))
        ```
    3. **presence_of_element_located(locator)**: Espera a que al menos un elemento coincida con el criterio de localización ``locator``
    4. **visibility_of_element_located(locator)**:Espera a que al menos un elemento coincida con el criterio de localización ``locator`` y sea visible.
    5. **visibility_of(element)**: Espera a que el elemento sea visible.
        ```python
        btn_aceptar_cookies =  driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
        WebDriverWait(driver, 10).until(EC.visibility_of(btn_aceptar_cookies))
        ```
    6. **visibility_of_element_located(locator)**: Espera a que al menos un elemento coincida con el criterio de localización locator y sea visible en la página.
        ```python
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.txt_locator_caja_busqueda))
        ```
    > Para mas condiciones de espera, acceda [Aqui](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions)

    > Tambien se pueden crear condiciones de espera personalizadas [link](https://selenium-python.readthedocs.io/waits.html#explicit-waits) 

    > Utilizacion de ``until`` y ``until_not`` [Documentacion](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.wait)



- #### Esperas Implicitas
    Estas establecen un tiempo de espera global para todas las operaciones de localización de elementos.

    ```python
    driver.implicitly_wait(10)
    ```
    En el ejemplo anterior, se fija una espera implícita de 10 segundos. Esto significa que cada vez que Selenium intenta encontrar un elemento y no lo encuentra de inmediato, esperará hasta 10 segundos antes de arrojar una excepción 

    Tambien podemos utilizar la libreria `time` con la funcion **sleep(segundos)**
    para decidir en que momento esperar, y no por cada elemento
    ```python
    from time import sleep

    sleep(5)
    ```

    La espera implícita es útil para gestionar casos donde los elementos de la página pueden tardar en cargarse, pero estos generan un tiempo de espera adicional, por lo tanto se recomienda el uso de **Esperas Explicitas** para mejorar la eficiencia de las pruebas