from ovito.io import import_file
from ovito.modifiers import CoordinationAnalysisModifier, SelectTypeModifier
import numpy as np
import os
import os.path as osp
import natsort as nt
import re
from matplotlib import pyplot as plt
from tqdm import tqdm

# file_extension = input('Enter the desired file extension: ')
file_extension = ".lammpstrj"
all_directory = os.listdir()
# initilization
file_list = []
num_list = []

for file in all_directory:
    if osp.isfile(file) and file.endswith(file_extension) and file.startswith('prod'):
        file_list.append(file)
        num_list.append(re.findall(r'\d+', file)) #re for getting number from file name
file_list = nt.natsorted(file_list)
num_list = nt.natsorted(num_list)
num_file = len(file_list)

for count,file in enumerate(file_list,0):
    print(f'Calculating RDF for {file}')
    pipeline = import_file(file, sort_particles=True)
    #nbins = 100, r_cutoff = 10, so delta_r = 0.1, same as VMD
    modifier = CoordinationAnalysisModifier(cutoff = 18, number_of_bins = 100, partial = True)
    pipeline.modifiers.append(modifier)
    total_rdf = np.zeros((modifier.number_of_bins,7)) #7 col, radius, 1-1,1-2,1-3,2-2,2-3,3-3

    for frame in tqdm(range(pipeline.source.num_frames)):
        data = pipeline.compute(frame)
        total_rdf += data.tables['coordination-rdf'].as_table()
    total_rdf /= pipeline.source.num_frames
    # print(type(total_rdf))
    # print(np.shape(total_rdf))
    delta_r = modifier.cutoff/modifier.number_of_bins
    print(f'Cutoff radius is {modifier.cutoff} \n number of bins is {modifier.number_of_bins} \n which makes it delta r as {delta_r} ')
    fig, axs = plt.subplots(nrows=2,ncols=3,constrained_layout=True)
    axs[0,0].plot(total_rdf[:,0],total_rdf[:,1])
    axs[0,0].set_title('Na-Na')
    axs[0,0].set_ylabel('g(r)')
    axs[1,0].plot(total_rdf[:,0],total_rdf[:,2])
    axs[1,0].set_title('Na-N')
    axs[1,0].set_ylabel('g(r)')
    axs[0,1].plot(total_rdf[:,0],total_rdf[:,3])
    axs[0,1].set_title('Na-O')
    axs[0,1].set_ylabel('g(r)')
    axs[1,1].plot(total_rdf[:,0],total_rdf[:,4])
    axs[1,1].set_title('N-N')
    axs[1,1].set_ylabel('g(r)')
    axs[0,2].plot(total_rdf[:,0],total_rdf[:,5])
    axs[0,2].set_title('N-O')
    axs[0,2].set_ylabel('g(r)')
    axs[1,2].plot(total_rdf[:,0],total_rdf[:,6])
    axs[1,2].set_title('O-O')
    axs[1,2].set_ylabel('g(r)')
    # plt.figure(1)
    # plt.plot(total_rdf[:,0],total_rdf[:,1])
    # plt.ylabel('r[Angstrom]')
    # plt.xlabel('g(r)')
    # plt.title('Na-Na')
    # plt.figure(2)
    # plt.plot(total_rdf[:,0],total_rdf[:,2])
    # plt.ylabel('r[Angstrom]')
    # plt.xlabel('g(r)')
    # plt.title('Na-N')
    # plt.figure(3)
    # plt.plot(total_rdf[:,0],total_rdf[:,4])
    # plt.ylabel('r[Angstrom]')
    # plt.xlabel('g(r)')
    # plt.title('N-N')
    # plt.figure(4)
    # plt.plot(total_rdf[:,0],total_rdf[:,6])
    # plt.ylabel('r[Angstrom]')
    # plt.xlabel('g(r)')
    # plt.title('O-O')
    file_no_extension = osp.splitext(file)[0]
    plt.savefig(file_no_extension)
    # plt.show()

    file_name = f'rdf_{str(*num_list[count])}K.txt'
    with open(file_name,'w') as rdf_file: #write file
        parameter = f'Cutoff radius: {modifier.cutoff}, bin#: {modifier.number_of_bins}, delta_r: {delta_r} \n'
        rdf_file.write(parameter)
        category = 'r Na-Na Na-N Na-O N-N N-O O-O\n'
        rdf_file.write(category)
    with open(file_name,'ab') as rdf_file: #append file with bytes mode
        np.savetxt(rdf_file,total_rdf)
