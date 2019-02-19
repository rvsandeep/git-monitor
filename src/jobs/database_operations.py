from utils import util
from py2neo.database import Schema

def create_indexes():
    graph = util.GraphConnector().connector
    
    db_schema = Schema(graph)
    db_schema.create_index("Project","project_id")
    db_schema.create_index("Platform","name")
    db_schema.create_index("License","name")
    db_schema.create_index("Language","name")
    db_schema.create_index("Status","name")
    db_schema.create_index("Version","id")
    db_schema.create_index("Version","number")
