import DTO_and_Models.models_pstg as model
from sqlalchemy import create_engine



# postgres+psycop2://<username>:<password>@<IP>:<Port>/<Database_name>
DatabaseURI = 'postgres+psycopg2://api:123@localhost:5432/local'

#Configura o acesso para o bd
engine = create_engine(DatabaseURI)


def create_tables():
    model.Table.drop_all(engine)
    model.Table.metadata.create_all(engine)




