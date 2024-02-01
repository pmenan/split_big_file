# coding: utf-8
import os
from io import StringIO
import random

############################################# Version 1 : spilt de fichier sans utilisation de fonction ###########################################

#Lire le fichier principal
#path = 'D:/git_repo/split_big_file/data/M50_TEST.TXT'
#tmp_file_path = 'D:/git_repo/split_big_file/data/tmp_file.txt'
#entete = ''
#pied_page = ''
#file = open(path, 'r')
#file_buffer = StringIO(file.read()) 
#file_tmp = open(tmp_file_path, 'x')
#for line in file_buffer:
#    if line.startswith('00.00'):
#        entete = line
#    elif line.startswith('99.00'):
#        pied_page = line
#    else:
#        file_tmp.write(line)
#
#file_tmp.close()
#file_tmp = open(tmp_file_path, 'r')
#file_tmp_buffer = StringIO(file_tmp.read())   
#split_data = file_tmp_buffer.getvalue().split('50.002')
##print(entete)
##print(pied_page)
##print(len(split_data))
#for data in range(1, len(split_data)):
#    random_number = random.randint(100, 200)
#    path_split = 'D:/git_repo/split_big_file/data/file_splitted/split_'+str(random_number)+".txt"
#    file = open(path_split, 'x')
#    file.write(entete)
#    file.write(split_data[data])
#    file.write(pied_page)
#    file.close()
#
#file.close


############################################ version 2 : Utilsation des fonctions développées dans utils.function  #######################################
from utils.function import *

# Ouverture du fichier source - fihier à splitter
try:
    file = load_file('D:/git_repo/split_big_file/data/','M50_TEST.TXT', 'r')
except:
    print("Erreur : Ouverture du fichier source KO")
print("Ouverture du fichier source OK \n")

# préparation du splitt
try:
    entete, pied_page = extract_line(file, 'D:/git_repo/split_big_file/data/', 'tmp_file.txt', 'x')
except:
    print("Erreur : Préparation du splitt KO")
print("Préparation splitte OK \n")

# Création des sous fichiers
try:
    split_file('D:/git_repo/split_big_file/data/file_splitted/', 'D:/git_repo/split_big_file/data/', 'tmp_file.txt', 'r', 'x', entete, pied_page)
except:
    print("Erreur : création des sous fichier KO")
print("Création des sous fichiers OK")