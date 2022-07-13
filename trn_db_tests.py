import pytest
import time
import pandas as pd
import pyodbc
import traceback

# pytest_plugins = ["docker_compose"]

# def waitDb(server, database, username, password, maxAttempts, waitBetweenAttemptsSeconds):
#     """
#     Returns True if the connection is successfully established before the maxAttempts number is reached
#     Conversely returns False
#     pyodbc.connect has a built-in timeout. Use a waitBetweenAttemptsSeconds greater than zero to add a delay on top of this timeout
#     """
#     for attemptNumber in range(maxAttempts):
#         cnxn = None
#         try:
#             cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#             cursor = cnxn.cursor()
#         except Exception as e:
#             print(traceback.format_exc())
#         finally:
#             if cnxn:
#                 print("The DB is up and running: ")
#                 return True
#             else:
#                 print("DB not running yet on attempt number " + str(attemptNumber))
#             time.sleep(waitBetweenAttemptsSeconds)
#     print("Max attempts waiting for DB to come online exceeded")
#     return False
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
# def test_that_waits_for_db_before_getting_triggered(wait_db_wrapper):
#     """
#     The DB is now good to go and tests can interact with it
#     The only assertion performed here is if waitDb returned True and a
#     """
#     isDbUp = wait_db_wrapper
#     assert isDbUp

server = 'localhost,54866'
database = 'TRN'
username = 'test_user'
password = '1234'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
# cursor = cnxn.cursor()
# res = cursor.execute('SELECT * FROM hr.regions').fetchall()
# for row in res:
#     print(row[0], row[1])

df = pd.read_sql("SELECT * FROM hr.regions", cnxn)
print(df.head())