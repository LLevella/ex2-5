import os
import subprocess

def create_dir_name(dir_list):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for i, dir_elem in enumerate (dir_list):
        dir_list[i] = os.path.join(current_dir, dir_elem)
    return dir_list

def create_new_dir (dir_list, ind_list):
    for i, dir_elem in enumerate(dir_list):
        if (i in ind_list) and not os.path.exists(dir_elem):
            os.mkdir(dir_elem)

def copy_files(in_dir, out_dir):
    if os.path.exists(in_dir):
        subprocess.run("xcopy " + in_dir + " " + out_dir)
