"""
Creates a backup directory and
copies the files in current directory to the new backup file
"""
import os
from datetime import datetime
from settings import game_root, datafiles

backup_folder = str(datetime.now()).replace(' ', '_').replace(':','-').replace('.','-')

if not os.path.exists('backups/%s' % backup_folder):
    print 'Created directory backups/%s' % backup_folder
    os.system('mkdir "backups/%s"' % backup_folder)

for file in datafiles:
    print 'Copying %s to backups/%s' % (file, backup_folder)
    os.system('cp %s backups/%s/' % (file, backup_folder))

print '\n\n'

# checking files created
for file in datafiles:
    if not os.path.exists('backups/%s/%s' % (backup_folder, file)):
        print 'ERROR: %s file was not copied to backups/%s' % (file, backup_folder)
    else:
        print 'OK - %s file was backed up' % file

