def get_filelist(file_extension='.png'):
    import os
    import os.path as osp
    import natsort as nt
    all_directory = os.listdir()
    # initilization
    file_list = []

    for file in all_directory:
        if osp.isfile(file) and file.endswith(file_extension):
        # if osp.isfile(file) and file.endswith(file_extension) and file.startswith('prod'):
            file_list.append(file)
    file_list = nt.natsorted(file_list)
    return file_list

def file2gif(file_list):
    import imageio
    import os
    images = []
    for file in file_list:
        images.append(imageio.imread(file))
    imageio.mimsave('rdf.gif',images,duration =0.5)

def main():
    file_list = get_filelist()
    file2gif(file_list)


#   Useful for debugging
# np.savetxt('test.txt',position[:,:,0])
# np.savetxt('Lindemann.txt',LindemannIndex_cluster)

if __name__ =='__main__':
    main()
