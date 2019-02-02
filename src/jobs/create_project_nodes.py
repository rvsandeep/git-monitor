from py2neo import Graph
import credentials
from pyspark.sql import SparkSession

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

    projects = spark.read.csv("s3n://rvsandeep-bucket/projects.csv", header=True, inferSchema=True, multiLine=True, escape='"'')

    projects_rdd_tf = projects.rdd.map(lambda x : util.populate_project(models.Project(), x))

    ls_ = projects_rdd_tf.collect()
    print(ls_['ID'])
