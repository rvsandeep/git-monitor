import models
from py2neo import Graph
import credentials

class GraphConnector():

    def __init__(self):
        self.connector = Graph( scheme='bolt+routing',
                    host=credentials.NEO4J_HOST, secure=True,
                    user=credentials.NEO4J_USERNAME, password=credentials.NEO4J_PASSWORD)



def create(node):
    gc = GraphConnector()
    tx = gc.connector.begin()
    tx.create(node)
    tx.commit()
    #[TODO: Update logic based on transaction successfully committed or not]
    return
