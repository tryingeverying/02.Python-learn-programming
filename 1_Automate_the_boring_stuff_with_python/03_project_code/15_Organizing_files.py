import os

for foldername,subfolders,filenames in os.walk(r'F:\Programming\Python\2_Python_Crash_Course'):
    
    print('The current folder is ' + foldername)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + foldername + ': ' + subfolder)
    for filename in filenames:
        print('FILE InSIDE ' + foldername + ': '+ filename)
    print('') 
import zipfile

