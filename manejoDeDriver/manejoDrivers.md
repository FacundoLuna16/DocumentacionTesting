# Manejo de Drivers en Selenium 
## Introducción 
**Selenium** es una herramienta popular para la automatización de pruebas en navegadores web. El manejo de los drivers es esencial para interactuar con diferentes navegadores. 
Un driver es un componente esencial que permite a Selenium comunicarse con un navegador específico


> ## **🚗 Tipos de driver.**


### ChromeDriver

**Instalacion:**

```python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

**ChromeDriverManager().install()** : Este método instala y gestiona automáticamente el controlador de Chrome.

**webdriver.Chrome()** : Define la instancia del driver para su posterior utilización, almacenada en la variable **driver**

### GeckoDriver (para Firefox)

**Instalacion**

```python
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
```
Cambiamos el argumento del import de `webdriver_manager` por el de "GeckoDriverManager", realizando a posterior los mismos pasos que se realizaron con el driver de Chrome



### EdgeDriver

**Instalacion**

```python
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeDriverManager

driver = webdriver.Edge(service=Service(EdgeDriverManager().install()))
```

### Otros Drivers
Además de Chrome, Firefox y Edge, Selenium admite otros navegadores como Safari, Opera, etc. Cada navegador tiene su propio driver específico.

> https://pypi.org/project/webdriver-manager/


> ## 🖥️ Gestión de Drivers con WebDriver Manager
El webdriver_manager es una herramienta útil que maneja automáticamente la descarga e instalación de los controladores necesarios. 
Esto nos envita descargarlos manualmente y proporciona una forma consistente de gestionar los controladores en diferentes entornos.

**Intalacion**

> pip install webdriver_manager

### Configuración y Cierre del Navegador


```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://wikipedia.org")

    yield driver  # Lo que esté después de yield se ejecuta después de cada test

    print("Cerrar Browser")
    driver.quit()
```
* **@pytest.fixture(autouse=True)** : Este es un decorador de fixture de Pytest. El parámetro **autouse=True** significa que este fixture se *ejecutará automáticamente* antes de cada prueba sin necesidad de llamarlo explícitamente.

* **def setup_teardown():** : Esta es la función del fixture que realiza la configuración y el cierre del navegador. Los fixtures en Pytest suelen tener un nombre descriptivo que refleje su propósito.

* **driver.maximize_window()** : Esta línea maximiza la ventana del navegador para asegurarse de que las pruebas se ejecuten en una ventana con el tamaño adecuado.



## Ejemplo

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWiki:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()) # Se puede utilizar un driver externo si asi lo quisieran
        )  
        self.driver.maximize_window()
        self.driver.get("http://wikipedia.org")

        yield  # Lo que este despues de yield se ejecuta despues de cada test

        print("Cerrar Browser")
        self.driver.quit()

    def test_validar_caja_texto_nuevo(self):
        # Ingresar búsqueda en la caja
        caja_busqueda = self.driver.find_element(By.ID, "searchInput")
        print("Limpiamos la caja de busqueda")
        caja_busqueda.clear()
        assert caja_busqueda.get_attribute("value") == "", "El elemento no se encuentra"
        print("Ingresamos el valor TDD en la caja de busqueda")
        caja_busqueda.send_keys("TDD")
        print("Presionamos ENTER")
        caja_busqueda.send_keys(Keys.ENTER)


if __name__ == "__main__":
    pytest.main()
```




