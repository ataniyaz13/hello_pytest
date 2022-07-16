# Environment setup

## Create virtual environment for tests execution
```bash
Ubuntu:
cd hello_pytest
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

Windows:
cd hello_pytest
python -m venv venv && source venv/Scripts/activate.bat
pip install -r requirements.txt
```

## Deploy and configure Data Quality solution
Follow [instructions](../README.md)


## Run pytest tests execution
Start tests with `pytest` 
```
pytest trn_db_tests.py -v --html=pytest_report.html
```