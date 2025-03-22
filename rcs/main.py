from api import Fazer_requisicao_get
from database import conexao_banco
from pandas import DataFrame
from dotenv import load_dotenv
from os import environ


if __name__ == '__main__':
    # url api
    vurl_cervejaria_openbrewerydb = 'https://api.openbrewerydb.org/breweries'

    # Variaveis de ambiente
    load_dotenv()
    DB_SENHA    = environ.get('POSTGRES_PASSWORD')
    DB_USUARIO  = environ.get('POSTGRES_USER')
    DB_DATABASE = environ.get('POSTGRES_DATABASE')
    DB_HOST     = environ.get('POSTGRES_HOST')
    DB_PORT     = environ.get('POSTGRES_PORT')   
    
    
    try:
        dados_json   = Fazer_requisicao_get(vurl=vurl_cervejaria_openbrewerydb)
        engine_banco = conexao_banco(user=DB_USUARIO, password=DB_SENHA, database=DB_DATABASE, host=DB_HOST, port=DB_PORT)
        
        if dados_json:
            # Importar registros para o banco  de dados
            dataframe_pandas = DataFrame(data=dados_json)
            dataframe_pandas.to_sql(name='dados_api',con=engine_banco, if_exists='replace', index=False)        
            
    except Exception as e:
        print(e)
    
    finally:
        print('Execução na main finaliza!!!')