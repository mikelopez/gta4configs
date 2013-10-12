"""
Copies the original datafiles from the game
root to local directory of this project
"""
import os
from settings import game_root, datafiles, datafile_dir

for file in datafiles:
    filename = file.split('/')[-1]
    print 'Copying %s/%s to %s' % (game_root, file, file)
    os.system('cp "%s/%s" %s' % (game_root, file, file))


