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
        json_response = self.get_api_response(self.url)
        most_lauch_year = self.date_with_most_launchs(json_response)
        most_lauch_site = self.launch_site_with_most_launchs(json_response)
        
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

    def date_with_most_launchs(self,api_json):
        """
            Funçao que recebe o json da api da SpaceX e retorna o ano com mais lançamentos de foguetes
            :param api_json: recebe o json da api 
            :type api_json: json
            :return: retorna o ano com mais lançamentos
            :type return: str
        """
        try:
            list_years = [k['launch_year'] for k in api_json if k.get('launch_year')]
            most_launch_year = max(set(list_years), key = list_years.count)
            logging.info(f"ano com mais lançamentos: {most_launch_year}")
            return most_launch_year
        except Exception as e:
            logging.error(f"erro ao separar a data com mais lançamentos: {e}")

    def launch_site_with_most_launchs(self,api_json):
        """
            Funçao que recebe o json da api da SpaceX e retorna o launch site com mais lançamentos de foguetes
            :param api_json: recebe o json da api 
            :type api_json: json
            :return: retorna o launch site com mais lançamentos
            :type return: str
        """
        try:
            list_sites = [k['launch_site'] for k in api_json if k.get('launch_site')]
            site_names = [k['site_name_long'] for k in list_sites if k.get('site_name_long')]
            most_site_name = max(set(site_names), key = site_names.count)
            logging.info(f"launch_site com mais lançamentos: {most_site_name}")
            return most_site_name
        except Exception as e:
            logging.error(f"erro ao separar o launch site com mais lançamentos: {e}")


if __name__ == '__main__':
    teste = Teste_xp()
    teste.main()