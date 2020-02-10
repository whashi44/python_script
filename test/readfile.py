
import os
import os.path as osp
import natsort as nt
import re
import numpy as np
# import time

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

# for file in file_list:
#     with open(file) as f:
#         item = f.readline()
#         timestep = int(f.readline())
#         item = f.readline()
#         num_atom = int(f.readline())
#         item = f.readline()
#         words = f.readline().split()
#         xli,xhi = float(words[0]),float(words[1])
#         words = f.readline().split()
#         yli,yhi = float(words[0]),float(words[1])
#         words = f.readline().split()
#         zli,zhi = float(words[0]),float(words[1])
#         item = f.readline().split()

#         words = f.readline().split()
#         ncol = len(words)
#         for i in range(1,num_atom):
#             words += f.readline().split()
#         floats = map(float,words)
#         atom_data =np.array(list(floats),np.float)
#         atom_data = atom_data.reshape(num_atom,ncol)
#         print(np.shape(atom_data))
t = -1
n = -1
position = []
for file in file_list:
    with open(file) as f: 
         for line in f:
            if line.startswith("ITEM: TIMESTEP"):
                t+=1   
            if line.startswith("ITEM: NUMBER OF ATOMS"):
                num_atom = next(f)
                n+=1
            if line.startswith("ITEM: ATOMS"):
                col_info = line.split()
                num_col = len(col_info)-2    
                for atom in range(int(num_atom)):
                    atom_property = next(f).split()
                    xyz = [float(atom_property[2]),float(atom_property[2]),float(atom_property[2])]
                    position = position.append(xyz)
    
    print(t)
    print(n)
    print(col_info,num_col)
    print(x)         
# ----------Calculation Begins-------------
# for file in file_list:
#     print("Calculating the Lindemann Index for file",file)
#
#
#     pipeline = import_file(file, sort_particles=True)
#     frames = pipeline.source.num_frames
#     data = pipeline.compute()
#     num_particle = data.particles.count
#     num_distance = num_particle - 1
#     distance = np.zeros((frames,1))
#     distance_square = np.zeros((frames,1))
#     distance_square_average = np.zeros((num_distance,num_distance))
#     distance_average = np.zeros((num_distance,num_distance))
#
#     shift = 0
#
#     for col in range(num_distance):
#         for row in range(shift, num_distance):
#             for frame in range(frames):
#                 data = pipeline.compute(frame)
#                 positions = np.array(data.particles['Position'])
#                 delta_x = positions[row + 1, 0] - positions[shift, 0]
#                 delta_y = positions[row + 1, 1] - positions[shift, 1]
#                 delta_z = positions[row + 1, 2] - positions[shift, 2]
#                 distance[frame] = np.sqrt(delta_x**2 + delta_y**2 + delta_z**2)
#             distance_square = distance[:]**2
#             distance_average[row,col] = np.mean(distance[:])
#             distance_square_average[row,col] = np.mean(distance_square[:])
#         shift += 1
#         # print(frame)
#     coefficient = 2 / ((num_particle) * (num_particle - 1))
#     distance_average_square = distance_average[:]**2
#     LindemannIndex_individual = np.sqrt(distance_square_average - distance_average_square) / distance_average
#     LindemannIndex_individual = np.nan_to_num(LindemannIndex_individual[:])
#     LindemannIndex_cluster = coefficient * np.sum(LindemannIndex_individual)
#     print("LindemannIndex for file:", file, "is: ", LindemannIndex_cluster)
