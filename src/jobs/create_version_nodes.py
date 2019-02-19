from utils import util
from models.version import Version
from pyspark.sql import SparkSession, SQLContext
from py2neo import Relationship
import re

#read version information and create version nodes
def process(sc, job_args=None):

    spark = SparkSession.builder.appName("git-monitor").getOrCreate()

    sql_context = SQLContext(sc)

    versions = spark.read.format("csv") \
                .option("header", "true")  \
                .option('quote', '"') \
                .option('escape', '"') \
                .load("s3a://rvsandeep-bucket/versions-1.4.0-2018-12-22.csv")

    version_nodes_rdd = versions.rdd.map(lambda x : Version(x))
    created_version_nodes = version_nodes_rdd.mapPartitions(util.create_nodes_in).count()
    linked_versions = versions.rdd.map(link_version_project_nodes).count()
    print("total versions created : ", created_version_nodes, linked_versions)

#establish relationship with project nodes and version
def link_version_project_nodes(version):
    gc = util.GraphConnector()
    graph = gc.connector
    project = graph.nodes.match("Project", project_id=version['Project ID']).first()

    if project is None :
        return

    version_parsed = re.findall("\\b\\d+\\b", version['Number'])
    if len(version_parsed) !=0:
        number = version_parsed[0]
        id_version = version['Project ID']+'_'+number
    else :
        return

    version = graph.nodes.match("Version", id=id_version).first()
    belongs_to_project = Relationship.type("PROJECT")
    graph.create(belongs_to_project(version, project))
