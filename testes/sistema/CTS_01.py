import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginFeature(unittest.TestCase):
        URL_LOGIN = "http://localhost:5000/login"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.driver = webdriver.Firefox()            
            self.driver.get(self.URL_LOGIN)
            self.username_input = self.driver.find_element(By.NAME, "email")
            self.password_input = self.driver.find_element(By.NAME, "pswd")
            self.login_button = self.driver.find_element(By.NAME, "btn_singin")
        
        def test_login_usuario_valido(self):
            self.assertIn("Login", self.driver.title)  # Verifica se o título da página contém "MyImage | Log in"
            # Dados de um usuario valido
            self.username_input.send_keys("armando@ufpi.edu.br")
            self.password_input.send_keys("armando")
            self.login_button.click()
            # Aguarda um pouco para que a página seja carregada após o login (se necessário)
            self.driver.implicitly_wait(3)
            # Verifica se a página redirecionou corretamente após o login (verifique o título ou algum elemento na página)
            self.assertIn("dashboard", self.driver.current_url)  # Substitua "PÁGINA_DE_DESTINO" pela URL da página para onde o login deve redirecionar
            assert 'armando' in self.driver.page_source
            assert 'Análise Processo 1' in self.driver.page_source

        def test_login_invalido(self):
            self.assertIn("Login", self.driver.title) 
            # Dados de um usuario invalido
            self.username_input.send_keys("armando")
            self.password_input.send_keys("armando")
            self.login_button.click()
            # Aguarda 3 segundo
            self.driver.implicitly_wait(3)
            # Verifica se continua na pagina de login
            self.assertIn("login", self.driver.current_url)
            #assert 'Credenciais inválidas' in self.driver.page_source

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()