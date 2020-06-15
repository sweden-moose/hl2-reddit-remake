import os
from shutil import copyfile

username = 'sweden-moose'  # username of your PC
path_cmd = f'C:\\Users\\{username}\\Desktop\\VTFCmd_BatchScript-Generator_v2.1\\bin\\'  # path to VTFCmd converter (backslash for CMD)
path_img = f'C:/Users/{username}/reddit_pics/compressed/'  # path to compressed images
path_mat = f'C:/Program Files (x86)/Steam/steamapps/common/Half-Life 2/hl2/custom/'  # path to your HL2 custom folder


def add_dirs(path):  # get all dirs of HL2
    all = []
    g = os.listdir(path)
    for i in g:
        if '.' in i[-6:]:
            continue
        else:
            all.append(path + '/' + i)
            all += add_dirs(path + '/' + i)
    return all


def get_files(path):  # get names of all HL2 textures
    g = os.listdir(path)
    files = []
    for i in g:
        if '.' in i[-6:]:
            files.append(i)
    return files


try:
    os.makedirs(path_mat + 'reddit')
except BaseException:
    print('reddit folder already exist')

all_files = {}
dirs = add_dirs('materials')  # Path to your HL2 game "materials" folder
dirs.sort(key=lambda x: len(x))
for i in dirs:
    all_files.update({i: get_files(i)})
count = 0
for i in all_files:
    count += len(all_files[i])
print('Total files:', count)
for i in all_files:
    try:
        os.makedirs(path_mat + 'reddit/' + i)
    except BaseException:
        break
cur = 0
for j in all_files:
    for i in all_files[j]:
        if '.' not in i[-6:]:
            continue
        try:
            copyfile(path_img + f'{cur}.jpg',
                     path_mat + 'reddit/' + j + '/' + f'{cur}.jpg')  # copy images to textures folders
        except:
            cur += 1
            continue
        os.rename('C:/test/' + j + '/' + str(cur) + '.jpg',
                  path_mat + 'reddit/' + j + '/' + i[:-3] + 'jpg')  # rename this images to textures
        cur += 1

for i in all_files:  # really long converter, tooks about 1.5h on my PC
    tempy = i.replace('/', '\\')
    os.system(
        f'{path_cmd}vtfcmd.exe -folder \"C:\\test\\{tempy}\\*.jpg\"')  # convert all images in folder to VTF texture
    cur_files = os.listdir('C:/test/' + i)
    for j in cur_files:  # remove .jpg, we dont need it anymore
        if j[-3:] == 'jpg':
            os.remove(path_mat + 'reddit/' + i + '/' + j)
