import pyspark
import argparse
import importlib
import sys
import os
from jobs import database_operations

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')

#PYSPARK requires two AWS jars, to open the files stored in S3
#this is required to access the jars packed in the libs/pyspark
os.environ['SPARK_HOME'] = os.getcwd()+'pyspark/'
parser = argparse.ArgumentParser()
parser.add_argument('--job', type=str, required=True)
parser.add_argument('--job-args', nargs='*')
args = parser.parse_args()

#creating indexes for different models in neo4j
database_operations.create_indexes()
sc = pyspark.SparkContext(appName=args.job)
job_module = importlib.import_module('jobs.%s' % args.job)

#invoke spark job's process entry point 
job_module.process(sc, args.job_args)
