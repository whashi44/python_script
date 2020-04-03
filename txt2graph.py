#standard library
import os,sys,re,time
import os.path as osp
import panda as pd
from importlib import import_module
from pprint import pprint

def get_filelist(file_extension='.txt'):
    file_list = []

    print(f'Using {file_extension} as target file extension')
    all_directory = os.listdir()

    for file in all_directory:
        if osp.isfile(file) and file.endswith(file_extension):
        # if osp.isfile(file) and file.endswith(file_extension) and file.startswith('prod'):
            file_list.append(file)
    file_list = nt.natsorted(file_list)
    return file_list

def main():
    file_list = get_filelist()
    print(f'Found the lists of files {file_list}')
    wiht open('converted.txt','w') as write_file:
        write_file.write('Organized RDF is \n')

    for count,file in enumerate(file_list):
        print(f"Extracting data from file: {file}")
        data = pd.read_csv(file)

if __name__ =='__main__':
    main()
