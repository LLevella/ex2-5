import os
import subprocess
from multiprocessing import Process, Pipe, current_process

def mpconv_files(in_dir, out_dir, file_name):
    in_file = os.path.join(in_dir, file_name)
    out_file = os.path.join(out_dir, file_name)
    subprocess.run("convert " + in_file + " -resize 200 " + out_file)
    proc_name = current_process().name
    print('{} converted {}'.format(proc_name, file_name))

def mpmain(dir_list):
    procs = []
    for file_name in os.listdir(dir_list[-1]):
        proc = Process(target=mpconv_files, args=(dir_list[-1], dir_list[-2], file_name,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()