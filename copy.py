"""Copies the original datafiles from the game root to local directory."""
import os
from settings import game_root, datafiles

for file in datafiles:
    print 'Copying %s/%s to .' % (game_root, file)
    os.system('cp %s/%s .' % (game_root, file))

