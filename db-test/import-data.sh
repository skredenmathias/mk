# wait for the SQL Server to come up
echo "Waiting for DB to start"
sleep 90s

#run the setup script to create the DB and the schema in the DB
echo "Running setup.sql"
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Password1!" -i setup.sql --accept-eula

# connecting to DB
# use password above :"Password1!"
# use localhost:port from dockerfile, in this case 1433 (because of EXPOSE 1433)

# import the data from the csv file
# /opt/mssql-tools/bin/bcp heroes.dbo.HeroValue in "/usr/work/heroes.csv" -c -t',' -S localhost -U SA -P "Password1!" -d heroes

# restore database from bak file
# source: https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-backup-and-restore-database?view=sql-server-ver15
echo "Restoring backup from /backup/SimpleLog.bak"
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -Q "RESTORE DATABASE [markedskraft] FROM DISK = N'/usr/work/backup/SimpleLog.bak' WITH FILE = 1, NOUNLOAD, REPLACE, NORECOVERY, STATS = 5"

# is markedskraft working as a name for the db?

echo "Success ?"
