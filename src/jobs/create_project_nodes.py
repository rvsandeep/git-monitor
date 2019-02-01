from py2neo import Graph
import credentials

def analyze(sc, job_args=None):
    gg = Graph( bolt=True,
                host=credentials.NEO4J_HOST, secure=True,
                user=credentials.NEO4J_USERNAME, password=credentials.NEO4J_PASSWORD)

    hadoop_conf=sc._jsc.hadoopConfiguration()
    hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    hadoop_conf.set("fs.s3a.awsAccessKeyId", os.environ['AWS_ACCESS_KEY_ID'])
    hadoop_conf.set("fs.s3a.awsSecretAccessKey", os.environ['AWS_SECRET_ACCESS_KEY'])

    projects = spark.read.format("csv").option("header", "true").load("s3a://rvsandeep-bucket/projects.csv")

    projects_rdd_tf = projects.rdd.map(lambda x : util.populate_project(models.Project(), x))

    projects_rdd_tf.take(5)
