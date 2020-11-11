import psycopg2
import sqlite3
import pandas as pd

# #  Create empty sqlite3 database (Could be input later?)
# sl_conn = sqlite3.connect('titanic.sqlite3')

# # Create a cursor
# sl_curs = sl_conn.cursor()

# Access Heroku database
dbname = 'd1uqcrltouetf1'
user = 'blrwuhctjooprk'
password = 'b06d888cc4aa6cb0267f011223c88c87a75355231f1e6209be61224fd9e3d169'
host = 'ec2-54-170-123-247.eu-west-1.compute.amazonaws.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Open postgres cursor
pg_curs = pg_conn.cursor()

# Create our table in pg
# pg_curs.execute("DROP TABLE IF EXISTS titanic")
# pg_curs.execute(create_table_statement)
pg_conn.commit()





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
GO