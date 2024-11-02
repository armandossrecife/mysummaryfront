import requests
from bs4 import BeautifulSoup

def get_html_content_from_file(nome_arquivo):
  html_content = ""
  try:
    with open(nome_arquivo, mode='r') as f_html:
        conteudo = f_html.read()
    html_content = conteudo
    return html_content
  except Exception as ex:
      raise ValueError("Error fetching the file:", ex)

def extract_data_from_table(table, headers):
    """Extrai dados de uma tabela HTML e retorna uma lista de dicionários."""
    data = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if cells:  # Verifica se a linha contém dados
            row_data = dict(zip(headers, [cell.text.strip() for cell in cells]))
            data.append(row_data)
    return data

class ProcessoExtractorFromFile:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.soup = self._get_soup()

    def _get_soup(self):
        html_content = get_html_content_from_file(self.nome_arquivo)
        return BeautifulSoup(html_content, 'html.parser')

    def extract_interessado(self):
        table = self.soup.find('table', class_='subListagem')
        headers = ['Tipo', 'Identificador', 'Nome']
        return extract_data_from_table(table, headers)

    def extract_documentos(self):
        table = self.soup.find_all('table', class_='subListagem')[1]  # Assumindo que a tabela de documentos é a segunda
        headers = ['Tipo do Documento', 'Data do Documento', 'Origem', 'Natureza']
        return extract_data_from_table(table, headers)

    def extract_movimentacoes(self):
        table = self.soup.find_all('table', class_='subListagem')[2]  # Assumindo que a tabela de movimentações é a terceira
        headers = ['Data Origem', 'Unidade Origem', 'Unidade Destino', 'Enviado Por', 'Recebido Em', 'Recebido Por']
        return extract_data_from_table(table, headers)

    def get_all_data(self):
        return {
            "interessado": self.extract_interessado(),
            "documentos": self.extract_documentos(),
            "movimentacoes": self.extract_movimentacoes()
        }

# Usando a classe
extractor = ProcessoExtractorFromFile(nome_arquivo='037395-2024-59.html')

# Obtendo todos os dados do processo
dados_processo = extractor.get_all_data()

# Acessando os dados:
print(dados_processo['interessado'])
print(dados_processo['documentos'])
print(dados_processo['movimentacoes'])