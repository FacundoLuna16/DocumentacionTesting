import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

parametros_busqueda = [
    ("Selenium", "Selenium"),
    ("TDD", "Desarrollo guiado por pruebas"),
    ("JAVA", "Java (lenguaje de programación)"),
    ("DATA DRIVEN TESTING", "Data-driven testing")
]


class TestWiki:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))  # Se puede utilizar un driver externo si asi lo quisieran
        self.driver.maximize_window()
        self.driver.get("http://wikipedia.org")

        yield  # Lo que este despues de yield se ejecuta despues de cada test

        print("Cerrar Browser")
        self.driver.quit()

    @pytest.mark.parametrize("var_buscar, resultado", parametros_busqueda) # Parametrizar el test
    def test_validar_caja_texto_nuevo(self, var_buscar, resultado):
        # Ingresar búsqueda en la caja
        caja_busqueda = self.driver.find_element(By.ID, "searchInput")
        print("Limpiamos la caja de busqueda")
        caja_busqueda.clear()
        print(f"Ingresamos el valor {var_buscar} en la caja de busqueda")
        caja_busqueda.send_keys(var_buscar)
        print("Presionamos ENTER")
        caja_busqueda.send_keys(Keys.ENTER)

        # Validar título en resultados
        titulo_resultados = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading")))
        print(f"Validar que el título sea {resultado}")
        assert resultado in titulo_resultados.text, f"El valor {resultado} no se encuentra en el título"


if __name__ == "__main__":
    pytest.main()