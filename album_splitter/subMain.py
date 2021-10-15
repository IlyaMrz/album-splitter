import os
import win32clipboard

win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

if not "youtube.com/watch" in URL:
    print('Youtube split Downloader'.center(90, '_'))
    URL = input('Enter youtube url :  ')
    
command = f'cmd /k python __main__.py -yt {URL}'
os.system(command)