# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:14:18 2017

@author: tamelill
"""

def write_file(query,name = "data"):
    name = name + ".txt"
    path = "genData\\" + name
    file = open(path,"w+")
    file.write("Name" + "; " + "Titel" + "; " + "Description" + "; " + "Status"+ "; " + "Date" + "\n")
    for element in query:
        file.write(element[1] + "; " +  str(element[2]) + "; " +  str(element[6]) + "; " + str(element[5]) + "; " +  str(element[3])+ "\n")
        
    file.close()

def write_cmd(query):
    for element in query:
        print(element[1] + "; " +  str(element[2]) + "; " +  str(element[6]) + "; " + str(element[5]) + "; " +  str(element[3])+ "\n")
        