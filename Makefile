clean:
	rm -fr dist/

build: clean
	mkdir ./dist
	cp ./src/main.py ./dist
	cp ./src/credentials.py ./dist	
	cd ./src && zip -x main.py -x \*libs\* -r ../dist/jobs.zip .
	cd ./src/libs && zip -r ../../dist/libs.zip .
