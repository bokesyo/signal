import os

# get the address of this directory
path = os.getcwd()
print(path)

# get all the files in this directory
file_list = os.listdir(path)
print(file_list)

dir_list = [] # all sub-directories
for i in file_list:
    if '.' not in i:
        # that means the object is not a file, it is a directory
        dir_list.append(i)

# a list containing all directories
print(dir_list)

# for all samples: ( a directory per sample )
for i in dir_list:

    this_path = os.path.join(path, i)  # absolute address of this sample
    file_list = os.listdir(this_path)  # all files in this directory
    # print(file_list)
    new_list = []

    for j in file_list:
        if 'wav' in j.split('.'):
            new_list.append(j)
    print(new_list)  # filter all wav files in this directory

    for k in new_list:
        number = k.split('.')[0]
        this_file_path = os.path.join(this_path, k)
        print(number, this_file_path)

        tar_dir = os.path.join(path, number)
        print(tar_dir)

        if not os.path.isdir(tar_dir):
            os.mkdir(tar_dir)

        identity = i.split('_')[0]  # whose voice
        source = this_file_path  # source voice address
        name = identity + '_' + k
        target = os.path.join(tar_dir, name)  # target voice address

        # print(target, 'TAR')
        # print(source, 'SCE')
        command = 'cp ' + source + ' ' + target
        print(command)
        os.system(command)
