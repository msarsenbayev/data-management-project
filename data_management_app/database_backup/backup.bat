@echo off
set "backup_folder=C:\backup\"
set "date_time=%date:/=-%_%time::=-%"
set "filename=%C:\Users\Massan\Desktop\1.London_Met_Modules\7.MSc_Final_Project\1.Project_Files\Django\data_management_project\data_management_app\database_backup%backup_%date_time%.backup"
echo "Backing up database to %filename%..."
"C:\Program Files\PostgreSQL\13\bin\pg_dump.exe" --dbname=postgres --format=c --file="%filename%" --username=postgres --host=127.0.0.1 --port=5432
echo "Backup complete."