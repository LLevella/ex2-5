import os
import subprocess

import myfunclib
import mpfunction

def convert_files(in_dir, out_dir, file_name):
    in_file = os.path.join(in_dir, file_name)
    out_file = os.path.join(out_dir, file_name)
    subprocess.run("convert " + in_file + " -resize 200 " + out_file)
    print ('{} converted'.format(in_file))


if __name__ == '__main__':
    dir_list =  myfunclib.create_dir_name(["output", "copy", "outputth", "outputmp", "Source"])
    myfunclib.create_new_dir(dir_list, [1, 2, 3, 4])
    myfunclib.copy_files(dir_list[-1], dir_list[1])

    for file_name in os.listdir(dir_list[-1]):
        convert_files(dir_list[-1], dir_list[0], file_name)
   
    print("multiprocessing")
    mpfunction.mpmain(dir_list)
