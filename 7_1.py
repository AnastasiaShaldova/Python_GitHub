import os

dir_name = os.path.join('my_project')
dir_names = ['settings', 'mainopp', 'adminapp', 'authapp']


def check(path):
    if not os.path.exists(path):
        os.mkdir(path)


check(dir_name)

for i in dir_names:
    foloder = os.path.join(dir_name, i)
    check(foloder)
