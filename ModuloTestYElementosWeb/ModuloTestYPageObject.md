# Importancia de un Módulo Test y Page Objects

## Módulo Test

- **Organización y Mantenimiento:** Un módulo de prueba organiza pruebas relacionadas, facilitando la identificación y corrección de errores.

- **Ejecución Independiente:** Cada módulo es independiente, permitiendo ejecutar pruebas específicas sin ejecutar todo el conjunto.


- **Parametrización y Configuración:** Se pueden usar variables o configuraciones para personalizar la ejecución de pruebas.

Un ejemplo de aplicacion del modulo Test es la siguiente:

```python

import pytest
from pages.stack_home_page import StackHomePage
from pages.stack_result_page import StackResultPage

parametros_busqueda = [
    ("pytest", "pytest"),
]

class Tests:

    @pytest.mark.parametrize("var_buscar, resultado", parametros_busqueda)
    def test_validar_caja_texto_nuevo(self,var_buscar, resultado,driver):#driver viene de conftest.py los demas parametros vienen del parametrize
        """
        Test para validar la funcionalidad de la caja de búsqueda.
        """
        driver.get("https://es.stackoverflow.com/")
        print("Validamos que se cargue la página")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.buscar(var_buscar)

        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL(resultado)



    def test_ir_usuarios(self,driver):
        """
        Test para verificar la navegación a la página de usuarios.
        """
        driver.get("https://es.stackoverflow.com/")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_usuarios()

        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL("users")

if __name__ == "__main__":
    pytest.main()


```
## Page Objects

- **Abstracción de la Interfaz de Usuario:** Una clase Page Object encapsula la interfaz de usuario, ofreciendo métodos más legibles y comprensibles.

- **Reusabilidad:** Los Page Objects se pueden reutilizar en múltiples pruebas, facilitando la actualización ante cambios.

- **Mantenimiento Sencillo:** Actualizar un Page Object en caso de cambios en la interfaz de usuario reduce el impacto en las pruebas.

- **Legibilidad del Código:** Mejora la legibilidad del código de prueba al utilizar métodos descriptivos en lugar de acciones directas sobre elementos.

- **Colaboración:** Facilita la colaboración entre desarrolladores y equipos de prueba al separar la implementación de la interfaz de usuario.

un ejemplo de este, puede ser el home de StackOverflow 

```python
class StackHomePage:
    """
    Clase que representa la Page Object de la página principal de Stack Overflow en español.
    """

    buscador = (By.XPATH, "//input[@placeholder='Buscar…']")
    btn_aceptar_cookies = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    btn_iniciar_sesion = (By.XPATH, "//a[normalize-space()='Iniciar sesión']")
    btn_registrarse = (By.XPATH, "//a[normalize-space()='Registrarse']")
    btn_usuario = (By.CSS_SELECTOR, "#nav-users")

    def __init__(self, driver):
        self.driver = driver
    
    def click_aceptar_cookies(self):
        """
        Método para hacer clic en el botón de aceptar cookies.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_aceptar_cookies)
        )
        
        if self.driver.find_element(*self.btn_aceptar_cookies).is_displayed():
            self.driver.find_element(*self.btn_aceptar_cookies).click()
            print("Aceptamos las cookies")
        else:
            print("Ya se aceptaron las cookies")
```

En resumen, la estructuración en módulos y el uso de Page Objects son prácticas esenciales para desarrollar pruebas automatizadas limpias, mantenibles y efectivas.

Pueden ver el ejemplo completo en este [repositorio](https://github.com/FacundoLuna16/AutomatizacionPython.git)