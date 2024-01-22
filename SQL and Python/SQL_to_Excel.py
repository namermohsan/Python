#pip install pandas
#pip install openpyxl
#pip install pyodbc

import pyodbc
import pandas as pd

# Set up the connection string
server = 'DESKTOP-T3GPF7I'
database = input('What database you want to connect to ?: ')
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

# Connecting to the database
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

print('Connected to the database successfully!')

# Execute the select query
table_name = input('Please enter the name of the table name you want to write to excel: ')
query = f"SELECT * FROM {table_name}"

# Fetch the data and store it in a pandas DataFrame
df = pd.read_sql(query, conn)

# Write the DataFrame to an Excel file
file_name = input('Please enter the name of the excel file you want (default output.xlsx)') or 'output.xlsx'
df.to_excel(file_name, index=False)

print('Data written successfully to excel file')
