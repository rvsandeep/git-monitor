from pyspark.sql import SparkSession
from py2neo import Relationship
import re
from utils import util

#read dependency info and create dependency relation between two projects
def process(sc, job_args=None):

    spark = SparkSession.builder.appName("git-monitor").getOrCreate()

    spark_context = spark.sparkContext

    dependencies = spark.read.format("csv") \
                .option("header", "true")  \
                .option('quote', '"') \
                .option('escape', '"') \
                .load("s3a://rvsandeep-bucket/dependencies-1.4.0-2018-12-22.csv")

    dependencies_rdd = dependencies.rdd.filter(lambda x : x['Project ID'] is not None)
    dependencies_rdd = dependencies_rdd.filter(lambda x : x['Dependency Project ID'] is not None)

    sc.parallelize(dependencies_rdd).foreach(link_dep_nodes)

def link_dep_nodes(dependency):
    gc = util.GraphConnector()
    graph = gc.connector

    dependent_version_parsed = re.findall("\\b\\d+\\b", dependency['Version Number'])
    if len(dependent_version_parsed) !=0:
        dependent_prj_major_version = dependent_version_parsed[0]
    else :
        return

    dependency_version_parsed = re.findall("\\b\\d+\\b", dependency['Dependency Requirements'])
    if len(dependency_version_parsed) !=0:
        dependency_prj_major_version = dependency_version_parsed[0]
    else :
        return

    dependent_on = Relationship.type("DEPENDENT_ON")
    dependent_on.dependency_type = dependency['Dependency Kind']
    dependent_on.is_optional = dependency['Optional Dependency']
    dependent_on.dependency_platform = dependency['Dependency Platform']
    dependent_on.dependency_name = dependency['Dependency Name']

    dependent_version = graph.nodes.match("Version", id=dependency['Project ID'] + '_' + dependent_prj_major_version).first()

    dependency_version = graph.nodes.match("Version", id=dependency['Dependency Project ID'] + '_' + dependency_prj_major_version).first()

    if (dependent_version is not None and dependency_version is not None) :
        graph.create(dependent_on(dependent_version, dependency_version))
