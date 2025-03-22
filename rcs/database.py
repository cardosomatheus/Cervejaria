# Libs
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def identifica_variaveis_vazias(params: list) -> None:
    """_summary_

    Args:
        params (list): Lista de variaveis de ambientes
    Raises:
        Exception: Se alguma dessas variaveis de ambiente estives vazia, Houve erro ao buscar os valores
    """
    if params is None:
        return
    
    for value in (params):
        if value is None:
            raise Exception(f'Houve erro ao buscar valores de variaveis de ambiente: {value}')


def conexao_banco(user: str, password: str, database: str, host: str, port: int) -> Engine:
    """_summary_

    Args:
        user (str, optional): _description_. Defaults to DB_USUARIO.
        password (str, optional): _description_. Defaults to DB_SENHA.
        database (str, optional): _description_. Defaults to DB_DATABASE.
        host (str, optional): _description_. Defaults to DB_HOST.
        port (int, optional): _description_. Defaults to DB_PORT.

    Returns:
        _type_: engine de conexao com o banco de dados
    """
    
    identifica_variaveis_vazias([user,password,database,host,port])

    vstring_conexao_banco =  f'postgresql://{user}:{password}@{host}:{port}/{database}'  
    engine = create_engine(vstring_conexao_banco)
    return engine
        
        
    

