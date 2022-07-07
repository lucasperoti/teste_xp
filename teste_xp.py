from tkinter import E
import requests
import pandas as pd
import logging
import json

class Teste_xp():

    def __init__(self) -> None:
        self.url = 'https://api.spacexdata.com/v3/launches'

    def main(self):
        """
            Função principal para chamar e executar as funçoes da classe.
        """
        retorno = self.get_api_response(self.url)
        print(retorno)

    def get_api_response(self,api_url):
        """
            Função que realiza o Get no endpoint de uma api e retorna o resultado convertido em json.
            :param api_url: Url da API com o endpoint 
            :type api_url: str
            :return: retorna o resultado da api como json
            :type return: json
        """
        try:
            response = requests.get(api_url)
            logging.info(response)
            json_response = response.json()
            logging.info(json_response)
            return json_response
        except Exception as e:
            logging.error(f"erro durante o processamento da api: {e}")

if __name__ == '__main__':
    teste = Teste_xp()
    teste.main()