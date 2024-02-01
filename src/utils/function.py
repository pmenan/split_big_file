# encoding: utf-8

from io import StringIO
import random

# chargement du fichier à splitter 
def load_file(path:str, file_name:str, mode:str):
    """
    on chagre le fichier principal à splitter

    param:
        path : chemin absolu ou rélatif du fichier source
        file_name : nom du fichier
        mode : mode d'ouverture du fichier (r, x, ...)
    
    return:
        un fichier
    """
    file = open(path+file_name, mode)
    return file

# Extraction de la ligne d'entête (1ère ligne) et de pied de page (dernière ligne)
def extract_line(initial_file, path:str, file_name_tmp:str, mode:str):
    """
    On extrait la 1ère et la dernière ligne du fichier.
    ces lignes seront présentes dans sous fichier après l'opération du splitte(1ère ligne et dernière ligne des sous fichiers)
    On enregistre les autres lignes dans un fichier temporaire qui sera utilsé pour le split

    param:
        initial_file : fichier courant
        path : chemin absolu ou rélatif du fichier source
        file_name_tmp : nom du fichier temporaire
        mode : mode d'ouverture du fichier (r, x, ...)
    
    return:
        un tuple (1ere ligne = entete, dernière ligne = pied_page, fichier temporaire de travail = file_tmp)
    """
    entete = ''
    pied_page = ''
    file_buffer = StringIO(initial_file.read())
    file_tmp = load_file(path, file_name_tmp, mode)
    for line in file_buffer:
        if line.startswith('00.00'):
            entete = line
        elif line.startswith('99.00'):
            pied_page = line
        else:
            file_tmp.write(line)
    return entete, pied_page

# Splitte des données enregistrées dans le fichier temporaire

def split_file(path_split:str, path_file_tmp:str, file_name_tmp:str, mode_file_tmp:str, mode_file_split:str, entete, pied_page):
    """
    On split le fichier de travail temporaire créée à l'étape précédente
    On construit chaque sous fichier en lui ajoutant la ligne d'entete + le split + la dernière ligne 

    param:
        path_split : chemin de stockage des sous fichiers
        mode : mode d'ouverture des fichiers avant écriture
        file_tmp : fichier temporaire de travail
        entete : 1ère ligne
        pied_page : dernière ligne

    return:
        None
    """
    file_tmp = load_file(path_file_tmp, file_name_tmp, mode_file_tmp)
    file_tmp_buffer = StringIO(file_tmp.read())
    split_data = file_tmp_buffer.getvalue().split('50.002')
    for data in range(1, len(split_data)):
        random_number = random.randint(100, 200)
        file_split_name = 'split_'+str(random_number)+'.txt'
        file = load_file(path_split, file_split_name, mode_file_split)
        file.write(entete)
        file.write(split_data[data])
        file.write(pied_page)
        file.close()

