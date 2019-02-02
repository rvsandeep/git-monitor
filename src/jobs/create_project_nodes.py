from py2neo import Graph
import credentials
from pyspark.sql import SparkSession
from utils import util

def analyze(sc, job_args=None):
    gg = Graph( bolt=True,
                host=credentials.NEO4J_HOST, secure=True,
                user=credentials.NEO4J_USERNAME, password=credentials.NEO4J_PASSWORD)

    #hadoop_conf=sc._jsc.hadoopConfiguration()
    #hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    #hadoop_conf.set("fs.s3a.awsAccessKeyId", credentials.AWS_ACCESS_KEY_ID)
    #hadoop_conf.set("fs.s3a.awsSecretAccessKey", credentials.AWS_SECRET_ACCESS_KEY)

    # Creating SparkSession, Spark Context and SQL Context Objects
    spark = SparkSession.builder \
                .appName("S3 READ TEST") \
                .config("spark.executor.cores", "6") \
                .config("spark.executor.memory", "6gb") \
    	    .config("spark.sql.join.preferSortMergeJoin", "false") \
    	    .getOrCreate()

    projects = spark.read.format("csv").option("header", "false").load("s3a://rvsandeep-bucket/projects.csv")
    print(projects)
