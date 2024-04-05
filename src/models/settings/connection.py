from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#A class that will manage the connection with database
class DBConnectionHandler:
    def __init__(self, database, dbfile) -> None:
        self.__string_connection = f"{database}:///{dbfile}" #Path to connect with database
        self.__engine = None #Variable that will make the connection
        self.session = None #Variable to enter in database

    #Method to get the engine
    def get_engine(self):
        return self.__engine
    
    #Method to make the connection with database
    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__string_connection)

    #Method to enter in database
    def __enter__(self):
        self.session = sessionmaker(bind=self.__engine)
        return self
    
    #Method to close the session
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


#Create the Connection Handler for database
database = "sqlite"
db_file = "storage.db"
connection_handler = DBConnectionHandler(database, db_file)