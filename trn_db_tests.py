import pytest
import time
import pandas as pd
import pyodbc
import traceback
from variables import server, database, username, password

def connect_db(server, database, username, password, maxAttempts, waitBetweenAttemptsSeconds):
    """
    Establish connection to db before the maxAttempts number is reached
    Conversely returns False
    pyodbc.connect has a built-in timeout. Use a waitBetweenAttemptsSeconds greater than zero to add a delay on top of this timeout
    """
    for attemptNumber in range(maxAttempts):
        cnxn = None
        try:
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            cursor = cnxn.cursor()
        except Exception as e:
            print(traceback.format_exc())
        finally:
            if cnxn:
                print("The DB is up and running: ")
                return cursor
            else:
                print("DB not running yet on attempt number " + str(attemptNumber))
            time.sleep(waitBetweenAttemptsSeconds)
    print("Max attempts waiting for DB to come online exceeded")
    return False
#
# # Invoking this fixture: 'function_scoped_container_getter' starts all services
# @pytest.fixture(scope="function")
# def wait_db_wrapper():
#     """Wait for the api from my_api_service to become responsive"""
#     server = 'localhost,54866'
#     database = 'TRN'
#     username = 'test_user'
#     password = '1234'
#     return waitDb(server, database, username, password, 3, 5)
#
#
@pytest.mark.regions_table_test
def test_counts():
    """
    The DB is now good to go and tests can interact with it
    The only assertion performed here is if waitDb returned True and a
    """
    cursor = connect_db(server, database, username, password, 3, 5)
    res = cursor.execute('SELECT count(*) FROM hr.regions').fetchall()
    result = res[0][0]
    assert result == 4

