import os
import yaml



def check(path):
    if not os.path.exists(path):
        os.mkdir(path)



# with open('config.yaml', 'r', encoding='utf-8') as f:
    print(dir(f))
    my_file = yaml.load_all(f, l)
    print(my_file)

    # for line, file in my_file:
    #     line = line.strip().split()
    #     filename = "_".join([i for i in line])
    #     os.mkdir(filename)



    # def build(folder):
    #     if folder:
    #         for d in folder:
    #             name = d[0]
    #             path = os.path.join(folder)
    #             check(path)
    #             build(path, d[1])


    # for item, doc in folder.items():
    #     print(item, ":", doc)


