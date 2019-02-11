import models
from py2neo import Graph
import credentials

#Connector utility for Neo4J database
class GraphConnector():

    def __init__(self):
        self.connector = Graph( scheme='bolt+routing',
                    host=credentials.NEO4J_HOST, secure=True,
                    user=credentials.NEO4J_USERNAME, password=credentials.NEO4J_PASSWORD)



def create_nodes_in(partition):
    gc = GraphConnector()
    tx = gc.connector.begin()
    for node in partition:
        tx.merge(node)
    tx.commit()
