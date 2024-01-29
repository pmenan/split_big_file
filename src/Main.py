# coding: utf-8
import os
from io import StringIO


#Lire le fichier principal
path = 'D:/git_repo/split_big_file/data/M50_TEST.TXT'
file = open(path, 'r')
print(file.read())
#file_buffer = StringIO( file.read())
#print(file_buffer.getvalue())
file.close