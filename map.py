import pygame
import os
from os import listdir
from os.path import isfile, join
from csv import reader



def csv_to_list(level_number):
    path = join("map",level_number) #str with the path to the directory
    files = [f for f in listdir(path) if isfile(join(path, f))]

    level_map = {}

    for file in files:
        map_1 = []
        with open(join(path, file)) as f:
            qqq = reader(f, delimiter=',')
            for row in qqq:
                map_1.append(list(row))
    
        level_map[file.replace(".csv", "")] = map_1
    return level_map


q = csv_to_list('0')#print(q['blocks'])
path = join("map", '0') #str with the path to the directory

print(path)
