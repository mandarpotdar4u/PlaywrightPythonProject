import pyodbc
import pytest

from utilities import azuresqldbconnection


@pytest.mark.db
def test_azuredb():
    try:
        # Open the connection
        conn = pyodbc.connect(azuresqldbconnection.connection_string)
        print("Connection successful!")

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query
        cursor.execute("SELECT TOP 10 * FROM [dbo].[LocalTempTable]")
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error: {e}")
    #
    # finally:
    #     # Close the connection
    #     # conn.close()
