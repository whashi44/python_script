# code structure:
# get list of directory
# create a directory"dump_deposit"
# change directory in to each list of directory
# grab file with specified file extension
# copy and paste it to the "dump_deposit"
# print out what file it moved

import shutil
import os
from pathlib import Path
import os.path as osp
import re
import natsort as nt

file_extension = ".lammps"
file_prefix = 'datatable'
all_directory = os.listdir()
folder_list = []
file_list = []

path = 'data_deposit'

try:
    os.mkdir(path)
except OSError:
    print(f'Creation of the directroy {path} failed')
else:
    print(f'Successfully created the directory {path} at {os.getcwd()}')


for folder in all_directory:
    if osp.isdir(folder):
        current_folder = os.listdir(folder)
        for file in current_folder:
            if file.endswith(file_extension) and file.startswith(file_prefix):
            # if file.startswith(file_prefix):
                original = osp.join(os.getcwd(),folder,file)
                target = osp.join(os.getcwd(),path)
                shutil.move(original,target)
                print(f'Copying file {file} to {path}')
# path = 'dump_deposit'
