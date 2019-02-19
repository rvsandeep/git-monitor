make clean
make build
cd dist/
spark-submit --num-executors 1 --executor-cores 1 --executor-memory 5G  --conf spark.network.timeout=900s --master spark://ip-10-0-0-4.us-west-2.compute.internal:7077 --py-files credentials.py,jobs.zip,libs.zip main.py --job create_project_nodes
spark-submit --num-executors 1 --executor-cores 1 --executor-memory 5G  --conf spark.network.timeout=900s --master spark://ip-10-0-0-4.us-west-2.compute.internal:7077 --py-files credentials.py,jobs.zip,libs.zip main.py --job create_version_nodes
spark-submit --num-executors 1 --executor-cores 1 --executor-memory 5G  --conf spark.network.timeout=900s --master spark://ip-10-0-0-4.us-west-2.compute.internal:7077 --py-files credentials.py,jobs.zip,libs.zip main.py --job create_dependencies
