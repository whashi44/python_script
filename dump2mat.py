from ovito.io import import_file
from ovito.io import export_file
from ovito.data import Particles
import numpy as np
import scipy.io as sio
import os
import os.path as osp
import natsort as nt
import re


# ----------Scan and Store file ----------------
# file_extension = input('Enter the desired file extension: ')
file_extension = ".lammpstrj"
all_directory = os.listdir()
file_list = []
num_list = []

for file in all_directory:
    if osp.isfile(file) and file.endswith(file_extension):
        file_list.append(file)
        num_list.append(re.findall(r'\d+', file))
file_list = nt.natsorted(file_list)
num_list = nt.natsorted(num_list)
num_file = len(file_list)

for file in file_list:
    pipeline = import_file(file, sort_particles=True)
    mat_file_name = '%s.mat' % file
    data = pipeline.compute()
    num_particle = data.particles.count
    num_dim = 3
    frames = pipeline.source.num_frames
    positions = np.zeros(((num_particle, num_dim, frames)))

    for frame in range(frames):
        data = pipeline.compute(frame)
        # print(np.shape(data.particles['Position']))
        # positions[:, :, frame,T] = np.array(data.particles['Position'])
        positions[:, :, frame] = np.array(data.particles['Position'])
    sio.savemat(mat_file_name, {'position': positions})
    print('Data has been exported to .mat file as ' + mat_file_name)
