import unittest
import testes.sistema.CTS_Processos

print("Faz o acesso ao processo de testes do Armando")

if __name__ == "__main__":
    try:
        print('Carrega a aplicação')
        print('Executa os testes automáticos do Selenium')
        # Create a test suite and add the test case with arguments
        test_case = testes.sistema.CTS_Processos.TestProcessosSIPAC('test_acessa_pagina_processos')
        test_case.test_acessa_pagina_processos(num_protocolo="037395", ano_protocolo="2024", dv_protocolo="59")
        test_case.run()
        unittest.main()
    except Exception as ex:
        print(f"Erro na execução dos Testes Cases: {str(ex)}")        