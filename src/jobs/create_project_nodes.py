import credentials
from pyspark import StorageLevel
from pyspark.sql import SparkSession, SQLContext
from utils import util
from models.project import Project
from models.platform import Platform
from models.language import Language
from models.status import Status
from models.license import License
from py2neo import Relationship

def process(sc, job_args=None):
    # Creating SparkSession
    spark = SparkSession.builder.appName("git-monitor") \
            .config("spark.executor.cores", "8") \
            .config("spark.executor.memory", "6gb") \
            .config("spark.sql.join.preferSortMergeJoin", "false") \
            .getOrCreate()

    spark_context = spark.sparkContext
    sql_context = SQLContext(spark_context)

    projects = spark.read.format("csv") \
                .option("header", "true") \
                .load("s3a://rvsandeep-bucket/projects.csv")

    sql_context.registerDataFrameAsTable(projects, "projects_tbl")

    #[TODO : refractor this code to be generic for a given column name, requires object detection based on column name]
    create_platform_nodes(sql_context)
    create_language_nodes(sql_context)
    create_status_nodes(sql_context)
    create_license_nodes(sql_context)

    prj_nodes_rdd = projects.rdd.map(lambda x : Project(x))
    #print(prj_nodes_rdd.getNumPartitions())
    prj_nodes_rdd.mapPartitions(util.create).collect()

    establish_relationships(sql_context)

def create_platform_nodes(sql_context):
    distinct_platforms = sql_context.sql("SELECT DISTINCT(Platform) from projects_tbl")
    distinct_platforms = distinct_platforms.rdd.filter(lambda x : x.Platform is not None)
    platform_nodes = distinct_platforms.map(lambda x : Platform(x))
    platform_nodes.mapPartitions(util.create).collect()

def create_language_nodes(sql_context):
    distinct_languages = sql_context.sql("SELECT DISTINCT(Language) from projects_tbl")
    distinct_languages = distinct_languages.rdd.filter(lambda x : x.Language is not None)
    language_nodes = distinct_languages.map(lambda x : Language(x))
    language_nodes.mapPartitions(util.create).collect()

def create_status_nodes(sql_context):
    distinct_statuses = sql_context.sql("SELECT DISTINCT(Status) from projects_tbl")
    distinct_statuses = distinct_statuses.rdd.filter(lambda x : x.Status is not None)
    statuses_nodes = distinct_statuses.map(lambda x : Status(x))
    statuses_nodes.mapPartitions(util.create).collect()

def create_license_nodes(sql_context):
    distinct_licenses = sql_context.sql("SELECT DISTINCT(Licenses) from projects_tbl")
    distinct_licenses = distinct_licenses.rdd.filter(lambda x : x.Licenses is not None)
    license_nodes = distinct_licenses.map(lambda x : License(x))
    license_nodes.mapPartitions(util.create).collect()

def establish_relationships(sql_context):
    relationships = sql_context.sql("SELECT ID, Platform, Language, Status, Licenses from projects_tbl")
    print(relationships)
    relationships.rdd.map(link_project_nodes).collect()

def link_project_nodes(relationship):
    gc = util.GraphConnector()
    graph = gc.connector
    project = graph.nodes.match("Project", project_id=relationship['ID']).first()

    if relationship['Platform'] is not None :
        is_in_platform = Relationship.type("IS_IN_PLATFORM")
        platform = graph.nodes.match("Platform", name=relationship['Platform']).first()
        graph.create(is_in_platform(project, platform))

    if relationship['Language'] is not None :
        is_in_language = Relationship.type("WRITTEN_IN")
        language = graph.nodes.match("Language", name=relationship['Language']).first()
        graph.create(is_in_language(project, language))

    if relationship['Status'] is not None :
        in_status = Relationship.type("STATUS")
        status = graph.nodes.match("Status", name=relationship['Status']).first()
        graph.create(in_status(project, status))

    if relationship['Licenses'] is not None :
        has_license = Relationship.type("HAS_LICENSE")
        license = graph.nodes.match("License", name=relationship['Licenses']).first()
        graph.create(has_license(project, license))
