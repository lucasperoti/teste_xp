import requests
import pandas as pd
import logging

class Teste_xp():

    def __init__(self) -> None:
        self.url = 'https://api.spacexdata.com/v3/launches'

    def main(self):
        """
            Função principal para chamar e executar as funçoes da classe.
        """
        json_response = self.get_api_response(self.url)
        most_lauch_year = self.date_with_most_launchs(json_response)
        most_launch_site = self.launch_site_with_most_launchs(json_response)
        launchs = self.launchs_between_years(json_response)
        self.create_xlsx_result(most_lauch_year,most_launch_site,launchs)


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
            list_years = self.filter_json_by_key(api_json,'launch_year')
            most_launch_year = self.most_appears_value_in_list(list_years) 
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
            list_sites = self.filter_json_by_key(api_json,'launch_site')
            list_site_names = self.filter_json_by_key(list_sites,'site_name_long')
            most_launch_site = self.most_appears_value_in_list(list_site_names)
            logging.info(f"launch_site com mais lançamentos: {most_launch_site}")
            return most_launch_site
        except Exception as e:
            logging.error(f"erro ao separar o launch site com mais lançamentos: {e}")
    
    def filter_json_by_key(self,json,key_value):
        """
            Funçao que recebe o json da api da SpaceX e retorna uma lista de 
            valores com base na chave que foi pasada como parametro.
            :param json: recebe o json da api 
            :type json: json
            :param key_value: recebe a chave que sera usada para filtrar o json
            :type key_value: str
            :return: retorna uma lista com os itens filtrados
            :type return: list
        """
        try:
            list_years = [k[key_value] for k in json if k.get(key_value)]
            return list_years
        except Exception as e:
            logging.error(f"erro ao separar o launch site com mais lançamentos: {e}")
    
    def most_appears_value_in_list(self,list):
        """
            Funçao que recebe uma lista como parametro e retorna o valor com a maior recorencia
            :param list: recebe uma lista
            :type list: list
            :return: retorna o valor com a maior recorencia
            :type return: str
        """
        try:
            most_appears = max(set(list), key = list.count)
            return most_appears
        except Exception as e:
            logging.error(f"erro ao separar o launch site com mais lançamentos: {e}")

    def launchs_between_years(self,api_json):
        """
            Funçao que recebe o json da api da SpaceX e retorna a quantidade de 
            lançamentos entre os anos de 2019-2020
            :param api_json: recebe o json da api 
            :type api_json: json
            :return: retorna a quantidade de laçamentos
            :type return: str
        """
        try:
            list_years = self.filter_json_by_key(api_json,'launch_year')
            launchs = len([year for year in list_years if year == '2019' or year == '2020' or year == '2021'])
            return launchs
        except Exception as e:
            logging.error(f"erro ao separar o launch site com mais lançamentos: {e}")
    
    def create_xlsx_result(self, most_lauch_year,most_launch_site,launchs):
        """
            Funçao que cria o arquivo xlsx de resultado
            :param most_lauch_year: Ano com mais lançamentos
            :type most_lauch_year: str
            :param most_launch_site: launch_site com mais lançamentos
            :type most_launch_site: str
            :param launchs: recebe numero de lançamentos
            :type launchs: str
        """
        data = {'Ano Com Mais Lançamentos': [most_lauch_year], 
                    'Launch site Com mais lançamentos': [most_launch_site], 
                    'Quantidade de lançamentos entre 2019-2021': [launchs]}
        dataframe = pd.DataFrame(data)
        dataframe.to_excel("result.xlsx", index=False)

if __name__ == '__main__':
    teste = Teste_xp()
    teste.main()