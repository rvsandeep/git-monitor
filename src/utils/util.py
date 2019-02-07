import models
from py2neo import Graph
import credentials

class GraphConnector():

    def __init__(self):
        self.connector = Graph( bolt=True,
                    host=credentials.NEO4J_HOST, secure=True,
                    user=credentials.NEO4J_USERNAME, password=credentials.NEO4J_PASSWORD)

    def create(self, nodes):
        tx = self.connector.begin()
        for i in nodes:
            tx.create(i)
        return tx.commit()


def create(nodes):
    gc = GraphConnector()
    gc.create(nodes)
    #[TODO: Update logic based on transaction successfully committed or notßßß]
    return [True]
