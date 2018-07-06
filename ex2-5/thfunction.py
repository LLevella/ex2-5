import os
import subprocess

import Queue
import threading
 
def thconv_files():
    while True:
        item = q.get()
        if item is None:
            break
        item = q.get()
        in_dir = item[0]
        out_dir = item[1]
        file_name = item[2]
        in_file = os.path.join(in_dir, file_name)
        out_file = os.path.join(out_dir, file_name)
        subprocess.run("convert " + in_file + " -resize 200 " + out_file)
        thr_name = threading.current_thread()
        print('{} converted {}'.format(thr_name, file_name))
        q.task_done()

def thmain(dir_list):
    
    q = queue.Queue()
    
    threads = []
    nth = 4

    for i in range(nth):
        t = threading.Thread(target=thconv_files)
        t.start()
        threads.append(t)

    for file_name in os.listdir(dir_list[-1]):
        item = []
        item.append(dir_list[-1])
        item.append(dir_list[-3])
        item.append(file_name)
        q.put(item)

    q.join()
    for i in range(nth):
        q.put(None)
    for t in threads:
        t.join()