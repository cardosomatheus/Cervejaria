# libs
import requests


def extract(vurl: str, vparams :dict = None, vheaders: dict = None) -> dict:  
    """_summary_

    Args:
        vurl (str): url da endopoint get
        vparams (dict, optional): Parametros da url. Defaults to None.
        vheaders (dict, optional): Headers da url. Defaults to None.

    Returns:
        dict: Retorna um json com os dados da requisção ou None caso tenha tido um erro.
    """
    try:
        requisicao_api  = requests.get(url=vurl, params=vparams, headers=vheaders, timeout=10)

        requisicao_api.raise_for_status()
        return requisicao_api.json()
    
    except Exception as e:
        print(f'Erro ao testar conexao da api: Erro:\n  {e}')        

    finally:
        print('Busca da api executada!!')
    
    return None    
    

