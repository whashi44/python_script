#standard library
import os
import os.path as osp
import re
import time
#packages
from tqdm import tqdm
try:
    from ovito.io import import_file

except ImportError:
    from pip._internal import main as pip
    print("I need to install ovito to your local user folder")
    pip(['install','--user','ovito'])
try:
    import natsort as nt
except ImportError:
    from pip._internal import main as pip
    print("I need to install natsort to your local user folder")
    pip(['install','--user','natsort'])
try:
    import numpy as np
except ImportError:
    from pip._internal import main as pip
    print("I need to install numpy to your local user folder")
    pip(['install','--user','numpy'])

# ----------Scan and Store file ----------------
t = time.time()
# file_extension = input('Enter the desired file extension: ')
file_extension = ".lammpstrj"
all_directory = os.listdir()
# initilization
file_list = []
num_list = []

for file in all_directory:
    if osp.isfile(file) and file.endswith(file_extension):
    # if osp.isfile(file) and file.endswith(file_extension) and file.startswith('prod'):

        file_list.append(file)
        num_list.append(re.findall(r'\d+', file)) #re for getting number from file name
file_list = nt.natsorted(file_list)
num_list = nt.natsorted(num_list)
num_file = len(file_list)

load_time = time.time() - t

with open('Lindemann.txt','w') as write_file:
    write_file.write('Lindemann Index is \n')

# ----------Calculation Part -------------
LindemannIndex_cluster = np.zeros(len(file_list))
for count,file in enumerate(file_list,0):
    t = time.time()
    print("Calculating the Lindemann Index for file",file)
    #   importing the files
    pipeline = import_file(file, sort_particles=True)
    num_frame = pipeline.source.num_frames
    data = pipeline.compute()
    #   Initilizations
    num_particle = data.particles.count
    num_distance = num_particle - 1
    distance = np.zeros((num_distance,num_frame))
    distance_average = np.zeros((num_distance,num_distance))
    distance_square_average = np.zeros((num_distance,num_distance))
    position = np.zeros(((num_particle,3,num_frame)))
    for frame in range(num_frame):
        data = pipeline.compute(frame)
        position[:,:,frame] = np.array(data.particles['Position'])
    difference = np.diff(position,axis = 0) #position axis = 0
    #   LI calculation
    for k in tqdm(range(num_distance), desc = 'Calculation'):
        xyz = np.cumsum(difference[k:,:,:],axis=0)  #position axis = 0
        distance = np.sqrt(np.sum(xyz**2,axis = 1))  #coordinate axis = 0
        distance_average[k:,k] = np.mean(distance, axis = 1) #due to the sum function, now the time axis = 1
        distance_square_average[k:,k] = np.mean(distance**2, axis = 1)
    coefficient = 2 / ((num_particle) * (num_particle - 1))
    distance_average_square = distance_average[:]**2
    with np.errstate(divide='ignore', invalid='ignore'): #supprsessing 0 division error warning
        LindemannIndex_individual = np.sqrt(distance_square_average - distance_average_square) / distance_average
    LindemannIndex_individual = np.nan_to_num(LindemannIndex_individual[:])
    LindemannIndex_cluster[count] = coefficient * np.sum(LindemannIndex_individual)

    calc_time = time.time() - t
    # print("LindemannIndex for set temperature ", *num_list[count], "K is: ", LindemannIndex_cluster[count]) #* to print as space instead pf ['']
    print("LindemannIndex for set temperature {}K is: {}".format(*num_list[count],LindemannIndex_cluster[count])) #* to print as space instead pf ['']
    with open('Lindemann.txt','a+') as write_file:
        LI = '{}\n'.format(np.array2string(LindemannIndex_cluster[count]))
        write_file.write(LI)

#   Useful for debugging
# np.savetxt('test.txt',position[:,:,0])
# np.savetxt('Lindemann.txt',LindemannIndex_cluster)
