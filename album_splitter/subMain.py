import os
import win32clipboard
#print('Youtube split Downloader'.center(90, '_'))
#URL = input('Enter youtube url :  ')
win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
command = f'cmd /k python __main__.py -yt {URL}'
os.system(command)