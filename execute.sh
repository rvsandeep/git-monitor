make clean
make build
cd dist/ && spark-submit --master spark://ip-10-0-0-4.us-west-2.compute.internal:7077 --py-files credentials.py,jobs.zip,libs.zip main.py --job create_project_nodes
