import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProcessosSIPAC(unittest.TestCase):
        URL_PROCESSOS = "https://www.sipac.ufpi.br/public/jsp/portal.jsf"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.driver = webdriver.Firefox()            
            self.driver.get(self.URL_PROCESSOS)

        def test_acessa_pagina_processos(self, num_protocolo: str, ano_protocolo: str, dv_protocolo: str):
            assert 'Entrar no sistema' in self.driver.page_source            
            menu_processos = self.driver.find_element(By.ID, "l-processos")
            menu_processos.click()
            self.driver.implicitly_wait(3)
            assert 'Opções de Busca de Processos' in self.driver.page_source

            # Preenche os campos com os valores do processo
            num_protocolo_field = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.NAME, "NUM_PROTOCOLO")) 
            )
            num_protocolo_field = self.driver.find_element(By.NAME, "NUM_PROTOCOLO")
            num_protocolo_field.clear()
            num_protocolo_field.send_keys(num_protocolo)

            ano_protocolo_field = self.driver.find_element(By.NAME, "ANO_PROTOCOLO")
            ano_protocolo_field.clear()
            ano_protocolo_field.send_keys(ano_protocolo)

            dv_protocolo_field = self.driver.find_element(By.NAME, "DV_PROTOCOLO")
            dv_protocolo_field.clear()
            dv_protocolo_field.send_keys(dv_protocolo)
            
            # Clica no botao "Consultar Processo"
            botao_consultar = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.NAME, "processoForm:j_id_jsp_282183773_21"))
            )            
            botao_consultar.click()
            self.driver.implicitly_wait(3)

            # Clica no link "Visualizar Processo"
            link_visualizar = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='Visualizar Processo']/parent::a")) 
            )
            link_visualizar.click()
            self.driver.implicitly_wait(3)
            
            try:
                conteudo = self.driver.page_source
                nome_arquivo = f"{num_protocolo}-{ano_protocolo}-{dv_protocolo}.html"
                #cria um arquivo com o conteudo do processo 
                with open(nome_arquivo, mode='w', encoding="utf-8") as f_processo:
                    f_processo.write(conteudo)
                print(f"Arquivo {nome_arquivo} criado com sucesso!")
            except Exception as ex:
                print(f"Erro ao criar o arquivo {nome_arquivo} com o conteudo do processo.")
        
        def tearDown(self):
            self.driver.quit()

