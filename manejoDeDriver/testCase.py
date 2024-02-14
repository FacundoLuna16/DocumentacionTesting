import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestWiki:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome(
            # Se puede utilizar un driver externo si asi lo quisieran
            service=Service(ChromeDriverManager().install())
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
        print(f"la caja tiene: {caja_busqueda.get_attribute(
            'value')}")
        with allure.step("verificar que la caja de busqueda este vacia"):
            assert caja_busqueda.get_attribute(
                "value") == "", "El elemento no se encuentra"

        with allure.step("verificar que la caja de busqueda este vacia"):
            assert len(caja_busqueda.get_attribute(
                "value")) == 2, "El elemento no se encuentra"

        print(f"Ingresamos el valor {"TDD"} en la caja de busqueda")
        caja_busqueda.send_keys("TDD")
        with allure.step("verificar que la caja de busqueda este vacia"):
            assert caja_busqueda.get_attribute(
                "value") == "TDD", "El elemento no se encuentra"
        print("Presionamos ENTER")
        caja_busqueda.send_keys(Keys.ENTER)


if __name__ == "__main__":
    pytest.main()
