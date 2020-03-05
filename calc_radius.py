#standard library
import os,sys,re,time
import os.path as osp
from importlib import import_module
from pprint import pprint

# test
# from numba import jit

def import_library():
    named_libs = [('numpy','np'),('natsort','nt'),
    ('ovito','ov'),('tqdm','tqdm')]
    input_flag = input("Would you like to import missing modules to your user folder? y/n: ")
    import_flag = bool(input_flag=='y')

    for name,short in named_libs:
        try:
            lib = import_module(name)
        except ModuleNotFoundError | ImportError:
            if import_flag==False:
                print(sys.exc_info())
            elif import_flag == True:
                from pip._internal import main as pip
                print(f'Installing {name} to your local user folder\n\n\n')
                pip(['install','--user',f'{name}'])
        else:
            globals()[short] = lib

def get_filelist(file_extension='.lammpstrj'):
    all_directory = os.listdir()
    # initilization
    file_list = []

    for file in all_directory:
        if osp.isfile(file) and file.endswith(file_extension):
        # if osp.isfile(file) and file.endswith(file_extension) and file.startswith('prod'):
            file_list.append(file)
    file_list = nt.natsorted(file_list)
    return file_list

def get_numlist(file_list):
    num_list = []

    for file in file_list:
            num_list.append(re.findall(r'\d+', file)) #re for getting number from file name
    num_list = nt.natsorted(num_list)

    return num_list

def main():
    calc_lindex()
#   Useful for debugging
# np.savetxt('test.txt',position[:,:,0])
# np.savetxt('Lindemann.txt',LindemannIndex_cluster)

if __name__ =='__main__':
    main()
