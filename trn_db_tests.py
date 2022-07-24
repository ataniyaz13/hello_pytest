import pytest
import pyodbc
from contextlib import contextmanager
from variables import server, database, username, password


# class MsDb:
#     """ Collection of helper methods to query the MS SQL Server database.
#     """
#
#     def __init__(self, username, password, server, initial_db='dev_db'):
#         self.username = username
#         self._password = password
#         self.server = server
#         self.db = initial_db
#         conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server +\
#                    ';DATABASE=' + self.db + \
#                    ';UID=' + self.username + \
#                    ';PWD=' + self._password + ';'
#         print('Connected to DB:', conn_str)
#         self._connection = pyodbc.connect(conn_str)
#         pyodbc.pooling = False
#
#     def __repr__(self):
#         return f"MS-SQLServer('{self.username}', <password hidden>, '{self.server}', '{self.db}')"
#
#     def __str__(self):
#         return f"MS-SQLServer Module for STP on {self.server}"
#
#     def __del__(self):
#         self._connection.close()
#         print("Connection closed.")
#
#     @contextmanager
#     def cursor(self, commit: bool = False):
#         """
#         A context manager style of using a DB cursor for database operations.
#         This function should be used for any database queries or operations that
#         need to be done.
#
#         :param commit:
#         A boolean value that says whether to commit any database changes to the database. Defaults to False.
#         :type commit: bool
#         """
#         cursor = self._connection.cursor()
#         try:
#             yield cursor
#         except pyodbc.DatabaseError as err:
#             print("DatabaseError {} ".format(err))
#             cursor.rollback()
#             raise err
#         else:
#             if commit:
#                 cursor.commit()
#         finally:
#             cursor.close()
#
#
# ms_db = MsDb(username=username, password=password, server=server, initial_db=database)

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 'host.docker.internal,54866' + ';DATABASE=' + 'TRN' + ';UID=' + 'test_user' + ';PWD=' + '1234' + ';')
cursor = conn.cursor()
cursor.execute('select count(employee_id) from hr.employees')
output = cursor.fetchall()
print(output)
class TestTrnDB:
    @pytest.mark.jobs_table_tests
    def test_jobs_average_salary(self):
        """
        Verify average min salary from jobs table

        *Setup:*
        0. Connect 'TRN' DB

        *Test Steps:*
        1. Query average min_salary from jobs table.

        *Expected result:*
        0. Jobs table is present in TRN DB.
        1. Query executed successfully.
        2. Jobs table average min_salary was calculated as expected.
        """
        with ms_db.cursor() as cursor:
            cursor.execute('select cast(avg(min_salary) as int) from hr.jobs')
            output = cursor.fetchall()
            result = output[0][0]
            assert result == 6568

    @pytest.mark.jobs_table_tests
    def test_highest_paid_job(self):
        """
        Verify highest paid job from jobs table

        *Setup:*
        0. Connect 'TRN' DB

        *Test Steps:*
        1. Query job_title with maximum max_salary from jobs table.

        *Expected result:*
        0. Jobs table is present in TRN DB.
        1. Query executed successfully.
        2. Jobs table job_title with maximum max_salary was calculated as expected.
        """
        with ms_db.cursor() as cursor:
            cursor.execute('select job_title from hr.jobs where max_salary = (select max(max_salary) from hr.jobs)')
            output = cursor.fetchall()
            result = output[0][0]
            assert result == 'President'

    @pytest.mark.employees_table_tests
    def test_employees_count(self):
        """
        Verify employees count from employees table

        *Setup:*
        0. Connect 'TRN' DB

        *Test Steps:*
        1. Query count employees from employees table.

        *Expected result:*
        0. Employees table is present in TRN DB.
        1. Query executed successfully.
        2. Employees count was calculated as expected.
        """
        with ms_db.cursor() as cursor:
            cursor.execute('select count(employee_id) from hr.employees')
            output = cursor.fetchall()
            result = output[0][0]
            assert result == 40

    @pytest.mark.employees_table_tests
    def test_earliest_hired_employee(self):
        """
        Verify earliest hired employee from employees table

        *Setup:*
        0. Connect 'TRN' DB

        *Test Steps:*
        1. Query earliest hired employee from employees table.

        *Expected result:*
        0. Employees table is present in TRN DB.
        1. Query executed successfully.
        2. Employee_id was calculated as expected.
        """
        with ms_db.cursor() as cursor:
            cursor.execute(
                'select employee_id from hr.employees where hire_date = (select max(hire_date) from hr.employees)')
            output = cursor.fetchall()
            result = output[0][0]
            assert result == 179

    @pytest.mark.countries_table_tests
    def test_countries_count_from_europe_and_asia(self):
        """
        Verify european and asian countries count from countries table

        *Setup:*
        0. Connect 'TRN' DB

        *Test Steps:*
        1. Query european and asian countries count from countries table.

        *Expected result:*
        0. Countries table is present in TRN DB.
        1. Query executed successfully.
        2. Countries count was calculated as expected.
        """
        with ms_db.cursor() as cursor:
            cursor.execute('select count(*) from hr.countries where region_id in (1, 3)')
            output = cursor.fetchall()
            result = output[0][0]
            assert result == 14

    @pytest.mark.countries_table_tests
    def test_countries_region_id_in_range_of_expected_values(self):
        """
        Verify countries region id in expected range of values from countries table

        *Setup:*
        0. Connect 'TRN' DB

        *Test Steps:*
        1. Query region ids from coutries table out of expected range.

        *Expected result:*
        0. Countries table is present in TRN DB.
        1. Query executed successfully.
        2. Countries ids are in range of expected values.
        """
        with ms_db.cursor() as cursor:
            cursor.execute('select count(*) from hr.countries where region_id > 4 and region_id < 1')
            output = cursor.fetchall()
            result = output[0][0]
            assert result == 0
