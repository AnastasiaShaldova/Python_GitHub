import os
import shutil
from os import walk, listdir

for root, dirs, files in walk('my_project'):
    try:
        if "templates" in dirs:
            for i in listdir(os.path.join(root, 'templates')):
                shutil.copytree(os.path.join(root, 'templates', i), os.path.join('my_project', 'templates', i))
    except (FileExistsError, EOFError) as e:
        print(f'concrete error: {e}')
        exit(1)
