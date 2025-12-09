mkdir data
cd data && mkdir raw && mkdir processed && mkdir external

cd ..
mkdir notebooks
cd notebooks && mkdir exploratory && mkdir modeling
	

cd ..
mkdir src
cd src && mkdir components && mkdir pipeline && touch __init__.py && touch utils.py
cd components && touch __init__.py && touch data_ingestion.py && touch data_transformation.py && touch model_trainer.py
cd ../pipeline && touch __init__.py && touch training_pipeline.py & cd ..


cd ..
mkdir tests
cd tests && touch __init__.py && touch test_components.py


cd ..
mkdir models

mkdir config
cd config && touch config.yaml

cd ..
touch requirements.txt && touch setup.py && touch README.md

