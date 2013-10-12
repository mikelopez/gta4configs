game_root = "d:/Rockstar Games/Grand Theft Auto IV/common/data"
datafile_dir = "common/data"
df = ['vehicles.ide',
      'handling.dat',
      'carcols.dat',
      'vehOff.csv']

for i in df:
    datafiles.append('%s/%s' % (datafile_dir, i))
    
