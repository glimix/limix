from os.path import dirname, realpath, join

def hdf5_file_example():
    dir_path = dirname(realpath(__file__))
    return join(dir_path, 'data', 'hdf5', 'data.h5')
