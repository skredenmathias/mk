PRINT N'Setting up SQL.'; 

CREATE DATABASE markedskraft;
GO
USE markedskraft;
GO

PRINT N'database created.'; 

RESTORE DATABASE [markedskraft] 
FROM DISK = N'/usr/work/backup/SimpleLog.bak' 
WITH FILE = 1, 
NOUNLOAD, REPLACE, STATS = 5

PRINT N'database restored.'; 
