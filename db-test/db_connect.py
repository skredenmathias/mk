import psycopg2
import sqlite3
import pandas as pd

# #  Create empty sqlite3 database (Could be input later?)
# sl_conn = sqlite3.connect('titanic.sqlite3')

dbname = 'stoic_poitras'
user = 'SA'
password = 'Password1!'
host = 'localhost'
'''
# # Create a cursor
# sl_curs = sl_conn.cursor()
import pypyodbc 

db_host = '172.17.0.1,1433'
db_name = 'stoic_poitras'
db_user = 'SA'
db_password = 'Password1!'

connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'

db = pypyodbc.connect(connection_string)
# SQL = 'CREATE TABLE saleout (id COUNTER PRIMARY KEY,product_name VARCHAR(25));'
# db.cursor().execute(SQL)
df = pd.read_sql_query('select * from table', db)
'''

# docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Password1!" -p 1433:1433 markedskraft
# Error state 38 (docker run -e "MSSQL_SA_PASSWORD=Password1!" -p 1433:1433 markedskraft)
# Run?: -i setup.sql
# Run: -e "ACCEPT_EULA=Y"


## The database specified in the connection string, or selected in the
## Options > Connection Properties tab of the SSMS connection dialog,
## is no longer valid or online (it might be set to AutoClose or the 
## user may simply not have permission).

import _mssql
'''
conn = _mssql.connect(server='localhost:1433', user='SA', password="Password1!",
    database='markedskraft')
'''

conn = _mssql.connect(server='localhost:1433', user='SA', password="Password1!", database='markedskraft')

# cursor = conn.cursor()
# df = pd.read_sql_query('SELECT * FROM table', conn)

# True
print(conn.connected)
# None
print(conn.identity)

if conn.select_db("markedskraft") == True:
    print("connected")
else:
    print("NOT")

all_tables = conn.execute_query("SELECT table_name FROM information_schema.tables;")
databases = conn.execute_query("SELECT name FROM sys.databases;")
columns = conn.execute_query("select * from information_schema.columns")
# conn.execute_query("SHOW TABLES;")

# list_tables = conn.execute_query("SELECT * FROM dbo")
# print(list_tables)

print(databases) # None
print(all_tables) # None
print(columns) # None

# query = "SELECT * FROM table"
# cursor.execute(query)
# cursor.fetchall()
# cursor.close()

# df.from_sql()

# cnxn = pypyodbc.connect("Driver={SQL Server};"
#                         "Server=localhost:1433;"
#                         "Database=stoic_poitras;"
#                         "uid=User;pwd=Password1!")
# df = pd.read_sql_query('select * from table', cnxn)


# conn = pyodbc.connect(
#     'Driver={SQL Server};'
#     'Server=DESKTOP-TLF7IMQ\SQLEXPRESS;'
#     'Database=retail;'
#     'Trusted_Connection=yes;'
# )
# cursor = conn.cursor()
# cursor.execute('SELECT TOP 5 * FROM dbo.table_transactions')
# for row in cursor: print(row)
# conn.close()




# Access Heroku database
dbname = 'stoic_poitras'
user = 'SA'
password = 'Password1!'
host = 'localhost'

# pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=1433)

# # Open postgres cursor
# pg_curs = pg_conn.cursor()

# # Create our table in pg
# # pg_curs.execute("DROP TABLE IF EXISTS titanic")
# # pg_curs.execute(create_table_statement)
# # pg_conn.commit()
# pg_curs.execute("SELECT * FROM markedskraft")





# New code
# USE MASTER
# GO

# ALTER DATABASE DBASE
# SET SINGLE_USER WITH
# ROLLBACK IMMEDIATE    
# GO

# RESTORE DATABASE DBASE
# FROM DISK = './SimpleLog.bak'
# WITH
# MOVE 'DBASE' TO 'C:\Program Files\Microsoft SQL Server\MSSQL10_50.DBASE\MSSQL\DATA\DBASE.MDF',
# MOVE 'DBASE_LOG' TO 'C:\Program Files\Microsoft SQL Server\MSSQL10_50.DBASE\MSSQL\DATA\DBASE_1.LDF', REPLACE    
# GO

# ALTER DATABASE DBASE SET MULTI_USER
# GO