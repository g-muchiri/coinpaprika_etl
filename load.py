def load_coin_data(transformed_data):
    import os
    from dotenv import load_dotenv
    from datetime import datetime

    ##This command enables us to read from .env file
    load_dotenv(override=True)
    ## The override = True enables you to update the variables in the environment without relying on cached values

    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PASSWORD =os.getenv('DATABASE_PASSWORD')
    DATABASE_PORT= os.getenv('DATABASE_PORT')

    import psycopg2
    from sqlalchemy import create_engine,text

    ## Create the engine
    engine = create_engine(f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')

    ##The command here creates a table 'coins' in the db name stated in the env and if the table exists,

    ## It appends new records

    transformed_data.to_sql('coins',engine, if_exists='append', index=False)
    
    print("The data has been loaded successfully")