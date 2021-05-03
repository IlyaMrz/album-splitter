import os
print('Youtube split Downloader'.center(90, '_'))
URL = input('Enter youtube url :  ')
command = f'cmd /k python split.py -yt {URL}'
os.system(command)