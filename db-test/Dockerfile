FROM microsoft/mssql-server-linux:latest

# Create work directory
RUN mkdir -p /usr/work
RUN mkdir -p /usr/work/backup
WORKDIR /usr/work

# Copy scripts from windows folder to Docker container
COPY . /usr/work/

# Copy .bak file to folder "backup" in working directory in container
# make sure SimpleLog.bak is in same folder as Dockerfile
COPY ./SimpleLog.bak /usr/work/backup/

# Grant permissions for the import-data script to be executable
RUN chmod +x /usr/work/import-data.sh

# Expose port. Port must be same port as DB in Docker container uses
# Database connection will be localhost:1433, if you write "EXPOSE 1433"
EXPOSE 1433
CMD /bin/bash sleep 90
CMD /bin/bash /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Password1!" -i setup.sql
# CMD /bin/bash ./entrypoint.sh