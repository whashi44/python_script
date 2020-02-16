import os
import os.path as osp
import natsort as nt
import re
import numpy as np
# import time

# ----------Scan and Store file ----------------
# file_extension = input('Enter the desired file extension: ')
file_prefix = "log"
all_directory = os.listdir()
file_list = []
num_list = []
data = []
trigger ='Performance:'
for file in all_directory:
    if file.startswith(file_prefix):
        file_list.append(file)
        num_list.append(re.findall(r'\d+', file))

file_list = nt.natsorted(file_list)
num_array = np.zeros((len(file_list),3))
num_array[:,0:2] = np.array(nt.natsorted(num_list))
# print(np.shape(num_list))
for file in file_list:
    with open(file) as f:
        for line in f:
            if line.startswith(trigger):
                data.append(line.split()[1])
num_array[:,2] = np.array(data)
print(num_array)
# print(nsperday_list)
