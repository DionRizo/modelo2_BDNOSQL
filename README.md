# modelo2_BDNOSQL
Mi modelo del proyecto de nuestra clase de bases de datos no sql 2023


### Setup a python virtual env with python cassandra installed
```
# Activate virtual env
python3 -m venv ./venv
source ./venv/bin/activate

# Install project python requirements
python3 -m pip install -r requirements.txt
```

### To run the API service
```
python3 -m uvicorn main:app --reload
```

### To load data
Ensure you have a running mongodb instance
i.e.:
```
docker run --name mongodb -d -p 27017:27017 mongo
```
Once your API service is running (see step above), run the populate script
```
cd data/
python3 populate.py
```

