import pyspark
import argparse
import importlib
import sys
import os

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')

os.environ['SPARK_HOME'] = os.getcwd()+'pyspark/'
parser = argparse.ArgumentParser()
parser.add_argument('--job', type=str, required=True)
parser.add_argument('--job-args', nargs='*')
args = parser.parse_args()

sc = pyspark.SparkContext(appName=args.job)
job_module = importlib.import_module('jobs.%s' % args.job)
job_module.analyze(sc, args.job_args)
