import os
import subprocess

dest_folder = '11523'
path = '.\projects'
for root, subdirs,files in os.walk(path):
    for d in subdirs:
        if d == dest_folder:
            try:
                subprocess.Popen(f'explorer "{root}\{d}"')
            except:
                print('Not found')

