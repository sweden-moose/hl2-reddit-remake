# Program for image compression
# requires a 6-7 minutes to compress all pictures (5k+)
# create folder "compressed" in your reddit pictures path
# Dont forget to change username

import os
from PIL import Image

qualit = 20  # precentage for quality (for the most shitty and funny exp, type 1)
username = 'sweden-moose'  # username of your PC
path = f'C:/Users/{username}/reddit_pics/'  # path to reddit pictures folder
files = os.listdir(path)
b = 0
for i in files:
    if i == 'compressed':
        continue
    png = Image.open(path + i)
    if i[-3:] == 'png':
        png.load()  # required for png.split()
        background = Image.new("RGB", png.size, (255, 255, 255))
        try:
            background.paste(png, mask=png.split()[3])  # 3 is the alpha channel
        except BaseException:
            try:
                png = png.resize((512, 512), Image.ANTIALIAS)
                png.save(f'C:/Users/{username}/reddit_pics/compressed/' + f'{b}.jpg', 'JPEG', quality=qualit)
                b += 1
            except BaseException:
                continue
            continue
        background = background.resize((512, 512), Image.ANTIALIAS)
        background.save(f'C:/Users/{username}/reddit_pics/compressed/' + f'{b}.jpg', 'JPEG', quality=qualit)
        b += 1
    else:
        try:
            png = png.resize((512, 512), Image.ANTIALIAS)
            png.save(f'C:/Users/{username}/reddit_pics/compressed/' + f'{b}.jpg', 'JPEG', quality=qualit)
            b += 1
        except BaseException:
            continue
