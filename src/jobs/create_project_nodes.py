import credentials
from pyspark.sql import SparkSession
from utils import util
from models.project import Project

def analyze(sc, job_args=None):
    # Creating SparkSession
    spark = SparkSession.builder.appName("git-monitor").getOrCreate()


    projects = spark.read.format("csv") \
                .option("header", "true") \
                .load("s3a://rvsandeep-bucket/projects.csv")
    prj_nodes_rdd = projects.rdd.map(lambda x : Project(x))
    gc = util.GraphConnector()
    gc.create(prj_nodes_rdd.collect())
