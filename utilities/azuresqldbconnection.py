import pyodbc

# Define the connection parameters
server = 'qadb2024.database.windows.net'
database = 'QADB'
username = 'admin01'
password = 'admin@1234'
driver = '{ODBC Driver 18 for SQL Server}'
Encrypt = 'yes'

# Create the connection
connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'