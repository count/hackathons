from scipy.io import loadmat
import os

DIR = '/path/to/Boroughs/'
allcoords = {}

for filename in os.listdir(DIR):
    try:
        borough = filename[:filename.index('.mat')]
        csvfile = DIR + borough + '.csv'
        data = loadmat(DIR + filename)
        coords = data['coords']
        allcoords[borough] = coords
        with open(csvfile, 'w') as outfile:
            outfile.write('Latitude,Longitude\n')
            for coord in coords:
                outfile.write(str(coord[1]) + ',' + str(coord[0]) + '\n')
    except:
        print('Skipping ' + filename)
            
with open(DIR + 'AllBoroughs.csv', 'w') as outfile:
    outfile.write('Latitude,Longitude,Borough\n')
    for borough in allcoords.keys():
        coords = allcoords[borough]
        for coord in coords:
            outfile.write(str(coord[1]) + ',' + str(coord[0]) + ',' + borough + '\n')